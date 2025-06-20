import sys
import os
import subprocess
import shutil

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from src.logger import obtener_logger

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))


def ejecutar_lint_y_guardar_log(ruta_pr: str) -> bool:
    logs_dir = os.path.join(ruta_pr, "logs")
    os.makedirs(logs_dir, exist_ok=True)
    lint_log_path = os.path.join(logs_dir, "lint.log")
    logger = obtener_logger(name="lint_logger", log_file=lint_log_path)

    raiz_proyecto = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))

    try:
        resultado = subprocess.run(
            ["bash", "scripts/lint_all.sh"],
            stdout=subprocess.PIPE,
            stderr=subprocess.STDOUT,
            text=True,
            cwd=raiz_proyecto
        )
        with open(lint_log_path, "w", encoding="utf-8") as log_f:
            log_f.write(resultado.stdout)
        logger.info("Lint ejecutado correctamente.")

        # Mover bandit_report.json si existe
        ruta_bandit = os.path.join(raiz_proyecto, "bandit_report.json")
        if os.path.isfile(ruta_bandit):
            destino = os.path.join(logs_dir, "bandit_report.json")
            shutil.move(ruta_bandit, destino)
            logger.info("bandit_report.json movido a logs.")

        return resultado.returncode == 0
    except Exception as e:
        logger.error(f"Error al ejecutar lint_all.sh: {e}")
        with open(lint_log_path, "w", encoding="utf-8") as log_f:
            log_f.write(f"Error al ejecutar lint_all.sh: {e}")
        return False


def ejecutar_tests_y_guardar_log(ruta_pr: str) -> bool:
    logs_dir = os.path.join(ruta_pr, "logs")
    os.makedirs(logs_dir, exist_ok=True)
    tests_log_path = os.path.join(logs_dir, "tests.log")
    logger = obtener_logger(name="tests_logger", log_file=tests_log_path)

    raiz_proyecto = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))

    try:
        resultado = subprocess.run(
            ["python3", "-m", "pytest", "--maxfail=1", "--disable-warnings", "-q"],
            stdout=subprocess.PIPE,
            stderr=subprocess.STDOUT,
            text=True,
            cwd=raiz_proyecto
        )
        with open(tests_log_path, "w", encoding="utf-8") as log_f:
            log_f.write(resultado.stdout)
        logger.info("Tests ejecutados correctamente.")

        return resultado.returncode == 0
    except Exception as e:
        logger.error(f"Error al ejecutar pytest: {e}")
        with open(tests_log_path, "w", encoding="utf-8") as log_f:
            log_f.write(f"Error al ejecutar pytest: {e}")
        return False


def main():
    raiz_proyecto = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
    base_dir = os.path.join(raiz_proyecto, "pr_simulation")

    if not os.path.isdir(base_dir):
        print(f"No existe el directorio {base_dir}")
        return

    print("=== Ejecutando lint y tests para todos los PRs ===")
    for nombre_carpeta in sorted(os.listdir(base_dir)):
        ruta_pr = os.path.join(base_dir, nombre_carpeta)
        if os.path.isdir(ruta_pr):
            print(f"\nProcesando PR {nombre_carpeta}...")
            lint_ok = ejecutar_lint_y_guardar_log(ruta_pr)
            tests_ok = ejecutar_tests_y_guardar_log(ruta_pr)

            print(f" → Lint:  {'OK' if lint_ok else 'Error'}")
            print(f" → Tests: {'OK' if tests_ok else 'Error'}")


if __name__ == "__main__":  # pragma: no cover
    main()
