import os
import tempfile
from scripts.check_pr import (validar_titulo, verificar_changelog,
                              validar_commits, ejecutar_lint,
                              ejecutar_tests, generar_pr_repor)
from unittest.mock import patch, MagicMock


# Test para verificar que el titulo de PR tiene el formato correcto
def test_titulo_valido():
    with tempfile.TemporaryDirectory() as temp_dir:
        pr_id = "123"
        carpeta_pr = os.path.join(temp_dir, pr_id)
        os.makedirs(carpeta_pr)
        archivo = os.path.join(carpeta_pr, f"pr_{pr_id}_title.txt")

        with open(archivo, "w", encoding="utf-8") as f:
            f.write("feat[#123]: primer pull request")

        ok, msg = validar_titulo(carpeta_pr)
        assert ok is True


# Test para verificar que el titulo de PR no tiene el formato correcto
def test_titulo_mal_formato():
    with tempfile.TemporaryDirectory() as temp_dir:
        pr_id = "124"
        carpeta_pr = os.path.join(temp_dir, pr_id)
        os.makedirs(carpeta_pr)
        archivo = os.path.join(carpeta_pr, f"pr_{pr_id}_title.txt")

        with open(archivo, "w", encoding="utf-8") as f:
            f.write("PR que no tiene el formato correcto")  # Mal formato

        ok, msg = validar_titulo(carpeta_pr)
        assert ok is False


# No existe el archivo PR ID
def test_archivo_inexistente():
    with tempfile.TemporaryDirectory() as temp_dir:
        pr_id = "124"
        carpeta_pr = os.path.join(temp_dir, pr_id)
        os.makedirs(carpeta_pr)

        ok, msg = validar_titulo(carpeta_pr)
        assert ok is False


# test para verificar que el archivo de titulo del PR esta vacio
def test_titulo_vacio():
    with tempfile.TemporaryDirectory() as temp_dir:
        pr_id = "125"
        carpeta_pr = os.path.join(temp_dir, pr_id)
        os.makedirs(carpeta_pr)
        archivo = os.path.join(carpeta_pr, f"pr_{pr_id}_title.txt")

        with open(archivo, "w", encoding="utf-8") as f:
            f.write("   \n")

        ok, msg = validar_titulo(carpeta_pr)
        assert ok is False


# test para verificar que el archivo CHANGELOG.md contiene la seccion del PR actual
def test_changelog_contiene_pr():
    with tempfile.TemporaryDirectory() as temp_dir:
        pr_id = "125"
        carpeta_pr = os.path.join(temp_dir, pr_id)
        os.makedirs(carpeta_pr)

        changelog_path = os.path.join(temp_dir, "CHANGELOG.md")
        with open(changelog_path, "w", encoding="utf-8") as f:
            f.write(f"# Cambios\n\n## PR {pr_id}\n- test PR\n")

        carpeta_actual = os.getcwd()
        os.chdir(os.path.join(temp_dir, pr_id))
        try:
            ok, _ = verificar_changelog(carpeta_pr)
        finally:
            os.chdir(carpeta_actual)

        assert ok


# test para verificar que el archivo CHANGELOG.md no contiene la seccion del PR actual
def test_changelog_sin_seccion():
    with tempfile.TemporaryDirectory() as temp_dir:
        pr_id = "126"
        carpeta_pr = os.path.join(temp_dir, pr_id)
        os.makedirs(carpeta_pr)

        changelog_path = os.path.join(temp_dir, "CHANGELOG.md")
        with open(changelog_path, "w", encoding="utf-8") as f:
            f.write("# Cambios\n\n## PR 999\n- test PR\n")

        carpeta_actual = os.getcwd()
        os.chdir(carpeta_pr)
        try:
            ok, msg = verificar_changelog(carpeta_pr)
        finally:
            os.chdir(carpeta_actual)

        assert ok is False


# Archivo de commits no existe
def test_validar_commits_archivo_inexistente():
    with tempfile.TemporaryDirectory() as temp_dir:
        carpeta_pr = os.path.join(temp_dir, "201")
        os.makedirs(carpeta_pr)

        ok, errores = validar_commits(carpeta_pr)
        assert ok is False


# No existe el archivo CHANGELOG.md
def test_changelog_no_existe():
    with tempfile.TemporaryDirectory() as temp_dir:
        pr_id = "201"
        carpeta_pr = os.path.join(temp_dir, pr_id)
        os.makedirs(carpeta_pr)

        # No se crea CHANGELOG.md

        carpeta_actual = os.getcwd()
        os.chdir(carpeta_pr)
        try:
            ok, msg = verificar_changelog(carpeta_pr)
        finally:
            os.chdir(carpeta_actual)

        assert ok is False


# Test para verificar que los commits tienen el formato correcto
def test_commits_todos_validos():
    with tempfile.TemporaryDirectory() as temp_dir:
        carpeta_pr = os.path.join(temp_dir, "127")
        os.makedirs(carpeta_pr)

        commits = """feat[#123]: primer commit
                    fix[#124]: segundo commit
                    refactor[#125]: tercer commit"""
        with open(os.path.join(carpeta_pr, "commits.txt"), "w", encoding="utf-8") as f:
            f.write(commits)

        ok, errores = validar_commits(carpeta_pr)
        assert ok is True
        assert errores == []


# Test para verificar que los commits tienen errores de formato
def test_commits_con_errores():
    with tempfile.TemporaryDirectory() as temp_dir:
        carpeta_pr = os.path.join(temp_dir, "128")
        os.makedirs(carpeta_pr)

        commits = """commit sin formato
                    feat123: falta corchetes
                    fix[#789]: commit correcto"""
        with open(os.path.join(carpeta_pr, "commits.txt"), "w", encoding="utf-8") as f:
            f.write(commits)

        ok, errores = validar_commits(carpeta_pr)
        assert ok is False
        assert len(errores) == 2
        assert "fila 1" in errores[0]
        assert "fila 2" in errores[1]


# test para ejecutar el linter y verificar que se ejecuta correctamente
def test_ejecutar_lint_exito():
    with patch("subprocess.run") as mock_run:
        mock_result = MagicMock()
        mock_result.returncode = 0
        mock_result.stdout = "Lint exitoso"
        mock_run.return_value = mock_result

        ok, salida = ejecutar_lint()
        assert ok is True


# test para verificar que el linter falla
def test_ejecutar_lint_error():
    with patch("subprocess.run") as mock_run:
        mock_result = MagicMock()
        mock_result.returncode = 1
        mock_result.stdout = ""
        mock_result.stderr = "Error de linting"
        mock_run.return_value = mock_result

        ok, salida = ejecutar_lint()
        assert ok is False


# test para verificar que el script de lint no existe
def test_ejecutar_lint_script_inexistente():
    with patch("subprocess.run", side_effect=FileNotFoundError):
        ok, salida = ejecutar_lint()
        assert ok is False


# test para ejecutar los tests y verificar que se ejecutan correctamente
def test_ejecutar_tests_exito():
    with patch("subprocess.run") as mock_run:
        mock_result = MagicMock()
        mock_result.returncode = 0
        mock_result.stdout = "tests pasaron"
        mock_run.return_value = mock_result

        ok, salida = ejecutar_tests()
        assert ok is True


# test para verificar que los tests fallan
def test_ejecutar_tests_falla():
    with patch("subprocess.run") as mock_run:
        mock_result = MagicMock()
        mock_result.returncode = 1
        mock_result.stdout = "1 test falló"
        mock_result.stderr = "Traceback (ultima llamada mas reciente):"
        mock_run.return_value = mock_result

        ok, salida = ejecutar_tests()
        assert not ok
        assert "1 test falló" in salida
        assert "Traceback" in salida


# test para verificar que pytest no se encuentra
def test_ejecutar_tests_no_encontrado():
    with patch("subprocess.run", side_effect=FileNotFoundError):

        ok, _ = ejecutar_tests()
        assert not ok


# test para verificar que se genera el reporte de PR correctamente
def test_generar_reporte_contenido(tmp_path):
    ruta = tmp_path / "reporte.md"
    datos = {
        "titulo": (True, "OK"),
        "changelog": (False, "FALLO: no existe CHANGELOG.md"),
        "commits": (False, ["línea 2: 'mal commit'"]),
        "lint": (True, "salida del linter"),
        "tests": (False, "falló la prueba 3"),
    }

    generar_pr_repor(
        str(ruta),
        datos["titulo"],
        datos["changelog"],
        datos["commits"],
        datos["lint"],
        datos["tests"],
    )

    assert ruta.exists()
