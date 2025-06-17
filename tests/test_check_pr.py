import os
import tempfile
from scripts.check_pr import validar_titulo

# Verifica que el titulo de PR tiene el formato correcto
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
        assert msg == "OK"
