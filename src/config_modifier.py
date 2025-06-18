import json
import os

try:
    from src.logger import obtener_logger
except ModuleNotFoundError:
    from logger import obtener_logger

logger = obtener_logger(log_file="logs/config_modifier.log")


def leer_json(file_path):
    """
    Lee el archivo JSON desde el sistema de archivos y
    devuelve su contenido como un diccionario
    """

    if not os.path.exists(file_path):
        logger.error(f"No existe el archivo '{file_path}'")
        raise FileNotFoundError(f"No existe el archivo '{file_path}'")

    with open(file_path, 'r', encoding='utf-8') as f:
        try:
            logger.info(f"Archivo '{file_path}' leído correctamente")
            return json.load(f)
        except json.JSONDecodeError:
            logger.error(f"El archivo '{file_path}' no contiene un JSON válido")
            raise ValueError(f"El archivo '{file_path}' no contiene un JSON válido")


def incrementar_version(file_path):
    """
    Incrementa el campo "version" del archivo JSON
    """

    config = leer_json(file_path)

    if "version" not in config:
        logger.error("No existe el campo 'version' en el archivo JSON")
        raise KeyError("No existe el campo 'version' en el archivo JSON")

    if not isinstance(config['version'], (int, float)):
        logger.error("El campo 'version' no es un número")
        raise TypeError("El campo 'version' no es un número")

    config["version"] += 1
    with open(file_path, 'w', encoding='utf-8') as f:
        json.dump(config, f, indent=4)
    logger.info(f"Versión incrementada a {config['version']} en {file_path}")
    return config["version"]


def incrementar_build_number(file_path):
    """
    Incrementa el campo "build_number" del archivo JSON.
    Si el campo no existe, lo crea con valor inicial 1.
    """
    config = leer_json(file_path)

    if "build_number" not in config:
        config["build_number"] = 0
        logger.info("Campo 'build_number' no existía, inicializado en 0")

    if not isinstance(config['build_number'], (int, float)):
        logger.error("El campo 'build_number' no es un número")
        raise TypeError("El campo 'build_number' no es un número")

    config["build_number"] += 1
    with open(file_path, 'w', encoding='utf-8') as f:
        json.dump(config, f, indent=4)
    logger.info(f"Build number incrementado a {config['build_number']} en {file_path}")
    return config["build_number"]


if __name__ == "__main__":  # pragma: no cover

    file_path = "config.json"
    try:
        data = leer_json(file_path)
        version = incrementar_version(file_path)
        build = incrementar_build_number(file_path)
        print(f"Contenido del archivo '{file_path}': {data}")
        print(f"Versión actualizada correctamente a: {version}")
        print(f"Build number actualizado correctamente a: {build}")
    except Exception as e:
        print(f"Error: {e}")
