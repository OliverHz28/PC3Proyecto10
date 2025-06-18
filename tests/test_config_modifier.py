# tests/test_config_modifier.py

import pytest
import json
from src.config_modifier import leer_json, incrementar_version, incrementar_build_number


@pytest.fixture
# Preparamos un archivo
# temporal para pruebas
def json_de_prueba(tmp_path):
    file_path = tmp_path / "config.json"
    data = {"version": 1.0, "name": "Test App"}
    with open(file_path, 'w') as f:
        json.dump(data, f)
    return file_path


# Preparamos un archivo JSON valido para probar la lectura correcta
def test_leer_json_valido(json_de_prueba):
    contenido = leer_json(json_de_prueba)
    assert contenido["version"] == 1.0
    assert contenido["name"] == "Test App"


# Preparamos un archivo JSON con el campo 'version'
# valido para probar el incremento de version
def test_incrementar_version(json_de_prueba):
    nueva_version = incrementar_version(json_de_prueba)
    assert nueva_version == 2.0
    with open(json_de_prueba) as f:
        datos = json.load(f)
    assert datos["version"] == 2.0


# Preparamos un archivo  con contenido invalido (no JSON)
def test_leer_json_invalido(tmp_path):
    file_path = tmp_path / "invalido.json"
    file_path.write_text("esto no es json")
    with pytest.raises(ValueError):
        leer_json(file_path)


# Preparamos un archivo JSON con campo 'version' de tipo incorrecto
def test_incrementar_version_tipo_incorrecto(tmp_path):
    file_path = tmp_path / "version_invalida.json"
    with open(file_path, 'w') as f:
        json.dump({"version": "uno"}, f)
    with pytest.raises(TypeError):
        incrementar_version(file_path)


@pytest.fixture
def json_con_build_number(tmp_path):
    """Fixture para pruebas con build_number"""
    file_path = tmp_path / "config_build.json"
    data = {"version": 1.0, "build_number": 5, "name": "Proyecto 10"}
    with open(file_path, 'w') as f:
        json.dump(data, f)
    return file_path


def test_incrementar_build_number_existente(json_con_build_number):
    """Prueba para incrementar build_number cuando ya existe"""
    nuevo_build = incrementar_build_number(json_con_build_number)
    assert nuevo_build == 6
    with open(json_con_build_number) as f:
        datos = json.load(f)
    assert datos["build_number"] == 6
    assert datos["version"] == 1.0


@pytest.fixture
def json_sin_build_number(tmp_path):
    """Fixture para pruebas sin build_number"""
    file_path = tmp_path / "config_sin_build.json"
    data = {"version": 1.0, "name": "Test App"}
    with open(file_path, 'w') as f:
        json.dump(data, f)
    return file_path


def test_incrementar_build_number_nuevo(json_sin_build_number):
    """Prueba incrementar build_number cuando no existe"""
    nuevo_build = incrementar_build_number(json_sin_build_number)
    assert nuevo_build == 1
    with open(json_sin_build_number) as f:
        datos = json.load(f)
    assert datos["build_number"] == 1


def test_incrementar_build_number_tipo_incorrecto(tmp_path):
    """Prueba error cuando build_number no es un número"""
    file_path = tmp_path / "build_invalido.json"
    with open(file_path, 'w') as f:
        json.dump({"build_number": "cinco"}, f)
    with pytest.raises(TypeError):
        incrementar_build_number(file_path)


def test_leer_json_archivo_inexistente():
    """
    Cuando el archivo no existe debe lanzarse FileNotFoundError
    """
    with pytest.raises(FileNotFoundError):
        leer_json("archivo_que_no_existe.json")


def test_incrementar_version_sin_campo_version(tmp_path):
    """
    Si el JSON no contiene la clave 'version' debe lanzarse KeyError
    """
    path = tmp_path / "sin_version.json"
    with open(path, "w", encoding="utf-8") as f:
        json.dump({"name": "App sin versión"}, f)

    with pytest.raises(KeyError):
        incrementar_version(path)
