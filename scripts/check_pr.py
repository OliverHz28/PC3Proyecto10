import os
import re
import subprocess
from typing import Tuple, List


def validar_titulo(carpeta_pr: str) -> Tuple[bool, str]:
    pr_id = os.path.basename(carpeta_pr)
    archivo_titulo = os.path.join(carpeta_pr, f"pr_{pr_id}_title.txt")

    if not os.path.isfile(archivo_titulo):
        return False, f"FAIL: Falta el archivo {archivo_titulo}"

    titulo = open(archivo_titulo, encoding="utf-8").read().strip()

    if not titulo:
        return False, f"FAIL: El archivo {archivo_titulo} esta vacio"

    patron = re.compile(r"^[A-Z]{2,5}-\d+: .+")
    if patron.match(titulo):
        return True, "OK"

    return False, f"FAIL: '{titulo}' no cumple con el formato requerido"


def verificiar_changelog(carpeta_pr: str) -> Tuple[bool, str]:

    archivo_changelog = "../CHANGELOG.md"

    if not os.path.isfile(archivo_changelog):
        return False, "FAIL: no existe CHANGELOG.md"

    contenido = open(archivo_changelog, encoding="utf-8").read()
    seccion_pr = f"## PR {os.path.basename(carpeta_pr)}"

    if seccion_pr in contenido:
        return True, "OK"

    return False, f"FAIL: No se encontro la seccion '{seccion_pr}'"


def validar_commits(carpeta_pr: str) -> Tuple[bool, List[str]]:
    archivo_commits = os.path.join(carpeta_pr, "commits.txt")
    if not os.path.isfile(archivo_commits):
        return False, ["no existe el archivo commits.txt"]

    incorrectos: List[str] = []
    patron = re.compile(r"^(feat|fix|docs|style|refactor|perf|test|chore)\[#\d+\]: .+")

    for fila, commit in enumerate(open(archivo_commits, encoding="utf-8"), 1):
        if not patron.match(commit.strip()):
            incorrectos.append(f"fila {fila}: '{commit.strip()}'")

    return (len(incorrectos) == 0, incorrectos)


def ejecutar_lint() -> Tuple[bool, str]:
    try:
        resultado = subprocess.run(
            ["bash", "lint_all.sh"],
            capture_output=True,
            text=True)
        if resultado.returncode == 0:
            return True, resultado.stdout.strip()
        else:
            return False, resultado.stderr.strip() or resultado.stdout.strip()
    except FileNotFoundError:
        return False, "no existe el script lint_all.sh"
