import logging
import os


def obtener_logger(name: str = "proyecto10_log", log_file: str = "logs/proyecto10.log"):
    """
    Devuelve un logger configurado para el proyecto
    """
    # Aseguramos que la carpeta de logs exista
    os.makedirs(os.path.dirname(log_file), exist_ok=True)
    logger = logging.getLogger(name)
    logger.setLevel(logging.INFO)

    # Evitamos agregar multiples handlers si ya existe uno
    if not logger.handlers:
        fh = logging.FileHandler(log_file)
        fh.setLevel(logging.INFO)
        formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
        fh.setFormatter(formatter)
        logger.addHandler(fh)
    return logger
