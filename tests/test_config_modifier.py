# tests/test_config_modifier.py

import pytest
import json
import os
from src.config_modifier import leer_json, incrementar_version

# Preparamos un archivo temporal para pruebas
@pytest.fixture
def json_de_prueba(tmp_path):
    file_path = tmp_path / "config.json"
    data = {"version": 1.0, "name": "Test App"}
    with open(file_path, 'w') as f:
        json.dump(data, f)
    return file_path

def test_leer_json_valido(json_de_prueba):
    contenido = leer_json(json_de_prueba)
    assert contenido["version"] == 1.0
    assert contenido["name"] == "Test App"

def test_incrementar_version(json_de_prueba):
    nueva_version = incrementar_version(json_de_prueba)
    assert nueva_version == 2.0
    with open(json_de_prueba) as f:
        datos = json.load(f)
    assert datos["version"] == 2.0
