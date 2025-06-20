import os
import shutil
import tempfile
import pytest
from unittest import mock
from scripts import log_pr


@pytest.fixture
def temp_pr_dir():
    temp_dir = tempfile.mkdtemp()
    yield temp_dir
    shutil.rmtree(temp_dir)


@mock.patch("scripts.log_pr.obtener_logger")
@mock.patch("scripts.log_pr.subprocess.run")
def test_ejecutar_lint_y_guardar_log_ok(mock_run, mock_logger, temp_pr_dir):
    mock_run.return_value = mock.Mock(stdout="lint ok", returncode=0)
    result = log_pr.ejecutar_lint_y_guardar_log(temp_pr_dir)
    assert result
    lint_log = os.path.join(temp_pr_dir, "logs", "lint.log")
    assert os.path.isfile(lint_log)
    with open(lint_log) as f:
        assert "lint ok" in f.read()


@mock.patch("scripts.log_pr.obtener_logger")
@mock.patch("scripts.log_pr.subprocess.run", side_effect=Exception("fail"))
def test_ejecutar_lint_y_guardar_log_error(mock_run, mock_logger, temp_pr_dir):
    result = log_pr.ejecutar_lint_y_guardar_log(temp_pr_dir)
    assert not result
    lint_log = os.path.join(temp_pr_dir, "logs", "lint.log")
    assert os.path.isfile(lint_log)
    with open(lint_log) as f:
        assert "Error al ejecutar lint_all.sh" in f.read()


@mock.patch("scripts.log_pr.obtener_logger")
@mock.patch("scripts.log_pr.subprocess.run")
def test_ejecutar_tests_y_guardar_log_ok(mock_run, mock_logger, temp_pr_dir):
    mock_run.return_value = mock.Mock(stdout="test ok", returncode=0)
    result = log_pr.ejecutar_tests_y_guardar_log(temp_pr_dir)
    assert result
    tests_log = os.path.join(temp_pr_dir, "logs", "tests.log")
    assert os.path.isfile(tests_log)
    with open(tests_log) as f:
        assert "test ok" in f.read()


@mock.patch("scripts.log_pr.obtener_logger")
@mock.patch("scripts.log_pr.subprocess.run", side_effect=Exception("fail"))
def test_ejecutar_tests_y_guardar_log_error(mock_run, mock_logger, temp_pr_dir):
    result = log_pr.ejecutar_tests_y_guardar_log(temp_pr_dir)
    assert not result
    tests_log = os.path.join(temp_pr_dir, "logs", "tests.log")
    assert os.path.isfile(tests_log)
    with open(tests_log) as f:
        assert "Error al ejecutar pytest" in f.read()


@mock.patch("scripts.log_pr.obtener_logger")
@mock.patch("scripts.log_pr.subprocess.run")
def test_ejecutar_lint_y_guardar_log_bandit(mock_run, mock_logger, temp_pr_dir):
    # Simula que bandit_report.json existe
    raiz = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
    bandit_path = os.path.join(raiz, "bandit_report.json")
    with open(bandit_path, "w") as f:
        f.write("{}")
    mock_run.return_value = mock.Mock(stdout="lint ok", returncode=0)
    result = log_pr.ejecutar_lint_y_guardar_log(temp_pr_dir)
    assert result
    logs_dir = os.path.join(temp_pr_dir, "logs")
    assert os.path.isfile(os.path.join(logs_dir, "bandit_report.json"))
    # Limpieza
    if os.path.exists(bandit_path):
        os.remove(bandit_path)
