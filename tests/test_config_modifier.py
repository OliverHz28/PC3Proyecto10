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