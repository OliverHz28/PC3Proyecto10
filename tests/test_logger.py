from src.logger import obtener_logger


def test_crear_archivo(tmp_path):

    log_file = tmp_path / "crear_archivo.log"

    logger = obtener_logger(name="crear_archivo_logger", log_file=str(log_file))
    logger.info("Probando la creacion del archivo")

    assert log_file.exists()


def test_escribir_archivo(tmp_path):

    log_file = tmp_path / "escribir_archivo.log"
    mensaje = "Probando un mensaje de prueba para escribir archivo"

    logger = obtener_logger(name="escribir_archivo_logger", log_file=str(log_file))
    logger.info(mensaje)

    contenido = log_file.read_text()
    assert mensaje in contenido
