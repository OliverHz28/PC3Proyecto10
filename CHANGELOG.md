## PR 29
- Se agregaron pruebas unitarias para `check_pr.py`
- Se anadieron validaciones para el titulo de la PR
- Se agregaron tests para verificar la seccion correspondiente en `CHANGELOG.md`
- Se anadieron pruebas para commits con formato incorrecto
- Se genero cobertura de validaciones de commits

## PR 13
- Se implemento la funcionalidad de auto-incremento de version en `config_modifier.py`
- Se agregaron pruebas basicas en `tests/test_config_modifier.py`

## PR 21
- Se anadio el script `lint_all.sh` para ejecutar linters
- Se integraron los tests en el flujo de trabajo (workflow)

## PR 24
- Se automatizo la validacion de Pull Requests mediante el script `check_pr.py`
- Se anadieron validaciones para titulos, commits y changelog
- Se genero reporte de validacion en `pr_report.md`

## PR 22
- Se creo el tag `v1.0.0` y se realizo el merge de la rama release a `main`
- Se agrego el archivo `pytest.ini` para configuracion de tests
- Se actualizo el `README.md` con guias de uso
- Se realizaron refactors en `config_modifier.py` y `lint_all.sh`

## PR 3
- Se integro la rama `feature/workflow` a `feature/develop`
- Se incluyeron tareas relacionadas al flujo automatizado de validaciones

## PR 2
- Se hizo merge de `feature/test` y `feature/tests` a `feature/develop`
- Se anadieron pruebas unitarias iniciales para archivos de configuracion

## PR 4
- Se hizo merge de `feature/config-modifier` a `feature/develop`
- Se incorporo logica para modificar y validar archivos de configuracion
