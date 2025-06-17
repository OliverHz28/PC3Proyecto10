import os
import tempfile
from scripts.check_pr import validar_titulo, verificar_changelog, validar_commits


# Test para verificar que el titulo de PR tiene el formato correcto
def test_titulo_valido():
    with tempfile.TemporaryDirectory() as temp_dir:
        pr_id = "123"
        carpeta_pr = os.path.join(temp_dir, pr_id)
        os.makedirs(carpeta_pr)
        archivo = os.path.join(carpeta_pr, f"pr_{pr_id}_title.txt")

        with open(archivo, "w", encoding="utf-8") as f:
            f.write("PROY-123: primer pull request")

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
