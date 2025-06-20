import os
import re
import sys
import subprocess
from typing import Tuple, List


# Valida el titulo del Pull Request verificando que el archivo correspondiente exista
# y que cumpla con el patron esperado
def validar_titulo(carpeta_pr: str) -> Tuple[bool, str]:
    pr_id = os.path.basename(carpeta_pr)
    archivo_titulo = os.path.join(carpeta_pr, f"pr_{pr_id}_title.txt")

    if not os.path.isfile(archivo_titulo):
        return False, f"FAIL: Falta el archivo {archivo_titulo}"

    titulo = open(archivo_titulo, encoding="utf-8").read().strip()

    if not titulo:
        return False, f"FAIL: El archivo {archivo_titulo} esta vacio"
    patron = re.compile(
        r"^(feat|fix|docs|style|refactor|perf|test|chore|merge)\[#\d+\]: .+")
    if patron.match(titulo):
        return True, "OK"

    return False, f"FAIL: '{titulo}' no cumple con el formato requerido"


def validar_pr_body(carpeta_pr: str) -> Tuple[bool, str]:
    pr_id = os.path.basename(carpeta_pr)
    archivo = os.path.join(carpeta_pr, f"pr_{pr_id}_body.md")

    if not os.path.isfile(archivo):
        return False, "FAIL: falta pr_<id>_body.md"

    with open(archivo, encoding="utf-8") as f:
        contenido = f.read().strip()

    if len(contenido) < 200:
        return False, "FAIL: descripcion < 200 caracteres"
    if "## Resumen" not in contenido:
        return False, "FAIL: falta seccion '## Resumen'"
    if "## Cambios" not in contenido:
        return False, "FAIL: falta seccion '## Cambios'"

    return True, "OK"


# Verifica que el archivo CHANGELOG.md contenga una seccion para el PR actual
def verificar_changelog(carpeta_pr: str) -> Tuple[bool, str]:
    archivo_changelog = "CHANGELOG.md"

    if not os.path.isfile(archivo_changelog):
        return False, "FAIL: no existe CHANGELOG.md"

    with open(archivo_changelog, encoding="utf-8") as f:
        contenido = f.read()

    pr_id = os.path.basename(carpeta_pr)
    seccion_pr = f"## PR {pr_id}"

    if seccion_pr not in contenido:
        return False, f"FAIL: No se encontró la sección '{seccion_pr}' en CHANGELOG.md"

    pr_ids = re.findall(r"^## PR (\d+)", contenido, re.MULTILINE)
    duplicados = []
    vistos = set()
    for id_ in pr_ids:
        if id_ in vistos and id_ not in duplicados:
            duplicados.append(id_)
        vistos.add(id_)

    if duplicados:
        return False, (
            f"FAIL: PRs duplicados encontrados en CHANGELOG.md: "
            f"{', '.join(duplicados)}"
        )

    return True, "OK"


# Verifica que todos los commits en commits.txt sigan un patron
def validar_commits(carpeta_pr: str) -> Tuple[bool, List[str]]:
    archivo_commits = os.path.join(carpeta_pr, "commits.txt")
    if not os.path.isfile(archivo_commits):
        return False, ["no existe el archivo commits.txt"]

    incorrectos: List[str] = []
    patron = re.compile(
        r"^(feat|fix|docs|style|refactor|perf|test|chore|merge)\[#\d+\]: .+")

    for fila, commit in enumerate(open(archivo_commits, encoding="utf-8"), 1):
        if not patron.match(commit.strip()):
            incorrectos.append(f"fila {fila}: '{commit.strip()}'")

    return (len(incorrectos) == 0, incorrectos)


# Detecta lineas duplicadas en los archivos Python del proyecto
def detectar_lineas_duplicadas_py() -> List[str]:
    ruta_src = os.path.abspath("src")

    if not os.path.isdir(ruta_src):
        return []

    from collections import defaultdict
    lineas: defaultdict[str, List[str]] = defaultdict(list)

    for raiz, _, archivos in os.walk(ruta_src):
        for archivo in archivos:
            if archivo.endswith(".py"):
                ruta_archivo = os.path.join(raiz, archivo)
                with open(ruta_archivo, encoding="utf-8") as f:
                    for numero, linea in enumerate(f, 1):
                        linea = linea.strip()
                        if linea and not linea.startswith("#"):
                            clave = linea
                            ubicacion = f"{archivo}:{numero}"
                            if ubicacion not in lineas[clave]:
                                lineas[clave].append(ubicacion)

    duplicadas = [
        f"'{linea}' aparece en {', '.join(ubicaciones)}"
        for linea, ubicaciones in lineas.items() if len(ubicaciones) > 1
    ]

    return duplicadas


# Ejecuta el script lint_all.sh para validar la calidad del codigo
def ejecutar_lint() -> Tuple[bool, str]:
    try:
        resultado = subprocess.run(
            ["bash", "scripts/lint_all.sh"],
            capture_output=True,
            text=True)
        if resultado.returncode == 0:
            return True, resultado.stdout.strip()
        else:
            return False, resultado.stderr.strip() or resultado.stdout.strip()
    except FileNotFoundError:
        return False, "no existe el script lint_all.sh"


# ejecuta los tests usando pytest y devuelve el resultado
def ejecutar_tests() -> Tuple[bool, str]:
    try:
        resultado = subprocess.run(
            ["pytest", "--maxfail=1", "--disable-warnings", "-q"],
            capture_output=True,
            text=True,

        )
        if resultado.returncode == 0:
            return True, resultado.stdout.strip()
        else:
            return False, resultado.stdout.strip() + "\n" + resultado.stderr.strip()
    except FileNotFoundError:
        return False, "No se encontro pytest"


# Genera el reporte de validacion del PR en formato Markdown
def generar_pr_repor(ruta_report: str, titulo, changelog, commits,
                     lint, tests, pr_body, sugerencias):
    with open(ruta_report, "w", encoding="utf-8") as f:
        f.write("# Informe de Validacion\n\n")
        f.write("## Titulo\n")
        f.write(f"{titulo[1]}\n\n")

        f.write("## Descripcion del PR\n")
        if pr_body[0]:
            f.write("OK\n\n")
        else:
            f.write(f"{pr_body[1]}\n\n")

        f.write("## Changelog\n")
        f.write(f"{changelog[1]}\n\n")

        f.write("## Commits\n")
        if commits[0]:
            f.write("OK\n\n")
        else:
            f.write("FAIL: Commits con errores de formato:\n")
            for error in commits[1]:
                f.write(f"- {error}\n")
            f.write("\n")

        f.write("## Lint\n")
        f.write(f"{'OK' if lint[0] else 'FAIL'}\n")
        f.write(f"```\n{lint[1]}\n```\n\n")

        f.write("## Tests\n")
        f.write(f"{'OK' if tests[0] else 'FAIL'}\n")
        f.write(f"```\n{tests[1]}\n```\n")

        if sugerencias:
            f.write("## Mejoras sugeridas\n")
            for sugerencia in sugerencias:
                f.write(f"- {sugerencia}\n")


def main():  # pragma: no cover

    ruta_base = "pr_simulation"
    if not os.path.isdir(ruta_base):
        print("No existe la carpeta pr_simulation")
        sys.exit(1)
    # iteramos sobre cada carpeta de PR y lo valida
    for nombre_carpeta in sorted(os.listdir(ruta_base)):
        ruta_pr = os.path.join(ruta_base, nombre_carpeta)
        if not os.path.isdir(ruta_pr):
            continue

        print(f"\nValidando PR {nombre_carpeta}")

        titulo = validar_titulo(ruta_pr)
        changelog = verificar_changelog(ruta_pr)
        commits = validar_commits(ruta_pr)
        lint = ejecutar_lint()
        tests = ejecutar_tests()
        pr_body = validar_pr_body(ruta_pr)
        sugerencias = detectar_lineas_duplicadas_py()

        generar_pr_repor(
            os.path.join(ruta_pr, "pr_report.md"),
            titulo,
            changelog,
            commits,
            lint,
            tests,
            pr_body,
            sugerencias
        )
    # indica donde se guardo el pr_report.md
        print("pr_report.md generado en:", os.path.join(ruta_pr, "pr_report.md"))


if __name__ == "__main__":  # pragma: no cover
    main()
