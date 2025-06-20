# Grupo 6 - PC3-proyecto10

## Team

| Miembro del Equipo | Codigo |
| :----------------- | :-------------------- | 
| **Choquecambi Germain** | `20211360A` |
| **Serrano Edy** | `20211229B` | 
| **Hinojosa Frank** | `20210345I`  | 

## Descripcion

**[Proyecto 10 - Grupo 6](https://github.com/OliverHz28/PC3Proyecto10)**, enfocado en simular un flujo Pull Request completo y la revisión de código automatizada usando:

- Git hooks
- Linters y análisis estático
- Scripts Python
- Simulación de merge
- Integración con GitHub Actions (act)

El avance se ha divido en 3 Sprints.

## Sprint 1

Realizado del 7 al 9 de junio de 2025, se compone de los siguiente:

### 1. Ramas

- `feature/tests`, desarrollado por **Edy Serrano** 
- `feature/hooks-testing`, desarrollado por **Germain Choquechambi** 
- `feature/lint-hooks`, desarrollado por **Germain Choquechambi** 
- `feature/workflows`, desarrollado por **Edy Serrano** 
- `feature/config-modifier`, desarrollado por **Frank Hinojosa** 

### 2. Issues

- [#2](#2-pruebas-automatizadas) Pruebas automatizadas
- [#3](#3-crear-workflow) Crear workflow 
- [#4](#4-crear-script-config_modifierpy) Crear script config_modifier.py
- [#5](#5-verificacion-calidad-de-codigo-python) Verificacion calidad de Codigo Python
- [#8](#8-validacion-y-control-de-calidad-con-hooks-commit-msg-y-pre-push) Validacion y control de calidad con hooks commit-msg y pre-push

### 3. Pull Request

- [#6](https://github.com/OliverHz28/PC3Proyecto10/pull/6) : merge[#4](#4-crear-script-config_modifierpy): feature/config-modifier a feature/develop 
- [#7](https://github.com/OliverHz28/PC3Proyecto10/pull/7) : merge[#2](#2-pruebas-automatizadas): feature/test a feature/develop
- [#9](https://github.com/OliverHz28/PC3Proyecto10/pull/9) : merge[#3](#3-crear-workflow) : feature/workflow a feature/develop
- [#10](https://github.com/OliverHz28/PC3Proyecto10/pull/10) : [#8](#8-validacion-y-control-de-calidad-con-hooks-commit-msg-y-pre-push) y [#5](#5-verificacion-calidad-de-codigo-python) : Feature/lint hooks


## Objetivos

- Crear la estructura inicial:

  * Carpeta `scripts/` con:
    * `lint_all.sh` que ejecute:

      * `flake8 src/ --max-line-length=88 --select=E,W,F`
      * `shellcheck scripts/*.sh`
      * `tflint --enable-all iac/` (si existe carpeta `iac/`, sino mostrar mensaje de "No IaC").
    * Hook `commit-msg` en `.git/hooks/` que valide patrón `^[A-Z]{3,5}-\d+: .+`.
    * Hook `pre-push` en `.git/hooks/` que llame a `lint_all.sh` y bloquee si hay errores.
  * Carpeta `src/` con un script Python `config_modifier.py` que:

    * Lea un JSON `config.json` y modifique un campo específico (por ejemplo, incremente "version").
  * Carpeta `tests/` con al menos 2 pruebas pytest para `config_modifier.py`.
  * Carpeta `.github/workflows/` con archivo `pr_validation.yaml` esqueleto que contenga jobs vacíos.
  * Carpeta `pr_simulation/` vacía.

* Ejecutar `lint_all.sh` localmente y corregir errores encontrados.

## Demostracion en video

[Sprint 1 (Dia 3: 9/06/2025) Grupo 6 Proyecto 10 ](https://www.youtube.com/watch?v=ZwcuikAZ56w&ab_channel=SerranoArosteguiEdySaul)

## Distribución

- **Edy Serrano**: Issues [#2](#2-pruebas-automatizadas), [#3](#3-crear-workflow)
- **Frank Hinojosa**: Issues [#4](#4-crear-script-config_modifierpy)
- **Germain Choquecambi**: [#5](#5-verificacion-calidad-de-codigo-python), [#8](#8-validacion-y-control-de-calidad-con-hooks-commit-msg-y-pre-push)

## Issues del Sprint 1

### [#2](https://github.com/OliverHz28/PC3Proyecto10/issues/2) Pruebas automatizadas
- **User story**  
    **As a** _desarrollador_  
    **I need** _pruebas automatizadas para asegurar el funcionamiento correcto del sistema_  
    **So that** _puedo garantizar que las funcionalidades principales operan correctamente y detectar errores de manera temprana_
- **Responsable**: Edy Serrano
- **Rama**: `feature/tests`
- **Objetivo**: Garantizar que las funcionalidades principales operan correctamente y detectar errores de manera temprana

### [#3](https://github.com/OliverHz28/PC3Proyecto10/issues/3) Crear workflow 
- **User story**  
    **As a** _desarrollador_  
    **I need** _un workflow skeleton pr_validation.yaml para preparar la automatización de validaciones_  
    **So that** _el proyecto este listo para implementar validaciones automaticas en los flujos de desarrollo (push y pull request)_
- **Responsable**: Edy Serrano
- **Rama**: `feature/workflows`
- **Objetivo**: Preparar el skeleton pr_validation.yaml que contenga jobs vacíos.

### [#4](https://github.com/OliverHz28/PC3Proyecto10/issues/4) Crear script config_modifier.py
- **User story**  
    **As a** _desarrollador_  
    **I need** _un script `config_modifier.py` que modifique archivos JSON_  
    **So that** _pueda automatizar cambios de configuración en los proyectos de forma rapida y segura_ 
- **Responsable**: Frank Hinojosa
- **Rama**: `feature/config-modifier`
- **Objetivo**: Crear `config_modifier.py` con funciones que lea un JSON config.json y modifique un campo específico como incrementar la `version`

### [#5](https://github.com/OliverHz28/PC3Proyecto10/issues/5) Verificacion calidad de Codigo Python
- **User story**  
    **As a** _desarrolador_  
    **I need** _analizar automaticamente mi codigo Python en busca de errores y prblemas de estilo_  
    **So that** _pueda asegurarme de que la base de codigo se mantenga limpia, legible y libre de erroes comunes_ 
- **Responsable**: Germain Choquechambi
- **Rama**: `feature/lint-hooks`
- **Objetivo**: Para verificar la calidad del codigo usando `linters`

### [#8](https://github.com/OliverHz28/PC3Proyecto10/issues/8) Validacion y control de calidad con hooks commit-msg y pre-push
- **User story**  
    **As a** _desarrollador_  
    **I need** _que el hook commit-msg valide el formato del mensaje de commit y que el hook pre-push ejecute un script de linting antes de permitir un push_  
    **So that** _se mantenga un mensaje de commits claro, y se garantice la calidad del codigo antes de subir cambios al repositorio remoto_
- **Responsable**: Germain Choquechambi
- **Rama**: `feature/hooks-testing`
- **Objetivo**: Verificar el formato del commit y garantizar la calidad del codigo antes de subir cambios al repositorio remoto



## Flujo de Trabajo
Se utilizo la estrategia **Git Flow** para organizar el desarrollo:

- **Ramas principales**:
  - `main`: Contiene la version estable y lista para produccion.
  - `develop`: Integra las funcionalidades completadas antes de pasar a `main`.

- **Ramas de soporte**:
  - `feature/*`: Cada nueva funcionalidad o issue se desarrolla en una rama `feature/nombre-issue` creada desde `develop`.
  - `hotfix/*`: Para corregir errores críticos detectados en `main`.
  - `release/*`: Preparacion de nuevas versiones antes de fusionar a `main`.

## Ejecucion del Proyecto

Para trabajar con el proyecto, realiza los pasos a continuacion.

1. **Clonar el repositorio**
    ```bash
    git clone https://github.com/OliverHz28/PC3Proyecto10.git
    cd PC3Proyecto10
    ```

2. **Crear y activar el entorno virtual**
    ```bash
    python3 -m venv pc3
    source pc3/bin/activate
    ```

3. **Instalar dependencias**
    ```bash
    pip install -r requirements.txt
    ```
4. **Instalar herramientas de analisis**
    
    Instalar `shellcheck` para analizar scrips bash
    ```bash
    sudo apt update && sudo apt install shellcheck
    ```

    Instalar `tflint` para analizar el codigo terraform de la plataforma oficial
    ```bash
    curl -s https://raw.githubusercontent.com/terraform-linters/tflint/master/install_linux.sh | bash
    ```
5. Copiar los `hooks` personalizados a la carpeta `.git/hooks`

    ```bash
    cp hooks/commit-msg .git/hooks/commit-msg
    ```

    ```bash
    cp hooks/pre-push .git/hooks/
    ```

6. Dar permisos de ejecucion a los hooks y al script de linting
    ```bash
    chmod +x .git/hooks/commit-msg
    ```

    ```bash
    chmod +x .git/hooks/pre-push
    ```

    ```bash
    chmod +x scripts/lint_all.sh 
    ```

4. **Ejecucion de `config_modifier.py`**
      ```bash
      python3 src/config_modifier.py
      ```

5. **Ejecucion de pruebas automatizadas**
      ```bash
      pytest
      ```

6. **Verificación de calidad de código**

    Antes de realizar el push, puedes ejecutar manualmente el linter:
      ```bash
    ./scripts/lint_all.sh 
      ```

## Sprint 2

Realizado del 13 al 17 de junio de 2025, se compone de los siguiente:

### 1. Ramas

- `feature/workflow-pull_request`, desarrollado por **Edy Serrano** 
- `feature/mejora-lint`, desarrollado por **Edy Serrano** 
- `feature/extender-workflow`, desarrollado por **Edy Serrano** 
- `feature/validar-pr`, desarrollado por **Germain Choquechambi** 
- `feature/tests-check-pr`, desarrollado por **Germain Choquechambi** 
- `feature/nuevos-test-check-pr`, desarrollado por **Germain Choquechambi** 
- `feature/AUTO_INCR_VERSION`, desarrollado por **Frank Hinojosa** 
- `feature/ADD_LOGGING`, desarrollado por **Frank Hinojosa** 


### 2. Issues

- [#13](#13-añadir-incremento-automatico-de-build_number-en-config_modifierpy) Añadir incremento automatico de build_number en config_modifier.py
- [#14](#14-añadir-modulo-de-logging) Añadir modulo de logging 
- [#15](#15-validar-el-titulo-de-pr) Validar el titulo de PR 
- [#16](#16-verificar-que-el-changelog-este-actualizado) Verificar que el changelog este actualizado
- [#17](#17-validar-formato-de-los-mensajes-de-commit) Validar formato de los mensajes de commit
- [#18](#18-generar-informe-de-validacion) Generar informe de validacion 
- [#19](#19-extender-workflow-de-actions-para-prs) Extender workflow de Actions para PRs
- [#20](#20-mejorar-lint_allsh-con-manejo-de-errores) Mejorar lint_all.sh con manejo de errores
- [#21](#21-configurar-simulación-con-act-pull_request) Mejorar lint_all.sh con manejo de errores
- [#24](#24-configurar-simulación-con-act-pull_request) [Epic] Automatizacion de validacion de Pull Requests
- [#29](#29-agregar-pruebas-unitarias-para-check_prpy) Agregar pruebas unitarias para check_pr.py

### 3. Pull Request

#### 3.1 Aceptados
- [#25](https://github.com/OliverHz28/PC3Proyecto10/pull/25) : feat[[#24]](#24-configurar-simulación-con-act-pull_request): Automatizar validacion de PRs con check_pr.py
- [#28](https://github.com/OliverHz28/PC3Proyecto10/pull/28) : feat[[#13]](#13-añadir-incremento-automatico-de-build_number-en-config_modifierpy): merge feature/AUTO_INCR_VERSION a develop
- [#31](https://github.com/OliverHz28/PC3Proyecto10/pull/31) : feat[[#21]](#21-configurar-simulación-con-act-pull_request) :
Feature/workflow pull request
- [#32](https://github.com/OliverHz28/PC3Proyecto10/pull/32) : Feature/mejora lint
- [#33](https://github.com/OliverHz28/PC3Proyecto10/pull/33) : docs[[#24]](#24-configurar-simulación-con-act-pull_request) :
crear CHANGELOG y agregar reportes de simulacion de PRs
- [#34](https://github.com/OliverHz28/PC3Proyecto10/pull/34) : merge[[#14]](#14-añadir-modulo-de-logging) :
feature/ADD_LOGGING branch a develop
- [#36](https://github.com/OliverHz28/PC3Proyecto10/pull/36) : test[[#29]](#29-agregar-pruebas-unitarias-para-check_prpy) :
agregar tests para check_pr.py
- [#37](https://github.com/OliverHz28/PC3Proyecto10/pull/36) : feat[[#19]](#19-extender-workflow-de-actions-para-prs) :
merge Feature/extender-workflow a develop

#### 3.1 Rechazados
- [#26](https://github.com/OliverHz28/PC3Proyecto10/pull/21) : feat[[#21]](#21-configurar-simulación-con-act-pull_request): añadir lint_all.sh y los test al workflow
- [#27](https://github.com/OliverHz28/PC3Proyecto10/pull/27) : Feature/config pullrequest
test[[#29]](#29-agregar-pruebas-unitarias-para-check_prpy): agregar pruebas unitarias para check_pr.py
- [#35](https://github.com/OliverHz28/PC3Proyecto10/pull/27) : Feature/config pullrequest
test[[#29]](#29-agregar-pruebas-unitarias-para-check_prpy): merge feature/test_check-pr a develop

## Objetivos

* Completar **`check_pr.py`**:

  - Leer carpeta `pr_simulation/<id>/` y:

     * `pr_<id>_title.txt` -> validar patrón `^[A-Z]{3,5}-\d+: .+`.
     * `CHANGELOG.md` -> verificar que contenga `<id>` en una sección "## PR <id>".
     * `commits.txt` -> validar que cada línea comience con `feat[#n]: descripción` o `fix[#n]: descripción`.
  - Generar `pr_simulation/<id>/pr_report.md` con:

     * Sección **Título**: OK/Fail (explicar si no coincide).
     * Sección **Changelog**: OK/Fail (explicar si no se actualizó).
     * Sección **Commits**: OK/Fail (enlistar commits inválidos).
     * Sección **Lint**: llamar a `lint_all.sh` y capturar salida; indicar si OK/Fail.
     * Sección **Tests**: ejecutar `pytest --maxfail=1 --disable-warnings -q` y reportar éxito o fallos.
  - Si cualquier sección es "Fail", salir con código de error -
* Ampliar **`pr_validation.yaml`**:

  * Job `validate-pr`:

    - Usa `actions/checkout@v2`.
    - Ejecuta `scripts/lint_all.sh`.
    - Corre pytest con cobertura y falla si < 80%.
    - Ejecuta `python3 scripts/check_pr.py pr_simulation/<id>` (usando matrix strategy para probar varios IDs de ejemplo).
  * Configurar `on: pull_request` y `on: workflow_dispatch`.
* Crear **dos ramas de feature**:

  - `feature/AUTO_INCR_VERSION`: modifica `config_modifier.py` para incrementar también otro parámetro (p. ej., `build_number`).
  - `feature/ADD_LOGGING`: añade un módulo Python `logger.py` que gestione logs en archivos.
* Simular **2 Pull Requests locales**:

  * Para cada rama, crear `pr_simulation/201_title.txt`, `pr_simulation/201_body.md`,
    `pr_simulation/201_commits.txt` con 3 commits apropiados.
  * Ejecutar `act pull_request` localmente para disparar `pr_validation.yaml`.
  * Revisar resultados y corregir errores en scripts y código.

## Demostracion en video

[Sprint 2 (Dia 18/06/2025) Grupo 6 Proyecto 10 ](https://www.youtube.com/watch?v=CXj9d7sZ-J0)

## Distribución

- **Edy Serrano**: Issues [#19](#19-extender-workflow-de-actions-para-prs), [#20](#20-mejorar-lint_allsh-con-manejo-de-errores), [#21](#21-configurar-simulación-con-act-pull_request)
- **Frank Hinojosa**: Issues [#13](#13-añadir-incremento-automatico-de-build_number-en-config_modifierpy), [#14](#14-añadir-modulo-de-logging)
- **Germain Choquecambi**: [#15](#15-validar-el-titulo-de-pr), [#16](#16-verificar-que-el-changelog-este-actualizado), [#17](#17-validar-formato-de-los-mensajes-de-commit), [#18](#18-generar-informe-de-validacion), [#24](#24-configurar-simulación-con-act-pull_request), [#29](#29-agregar-pruebas-unitarias-para-check_prpy)

## Issues del Sprint 2

### [#13](https://github.com/OliverHz28/PC3Proyecto10/issues/13) Añadir incremento automatico de build_number en config_modifier.py
- **User story**  
    **As a** _desarrollador_  
    **I need** _extender `config_modifier.py` para incrementar el campo build_number_  
    **So that** _las builds automatizadas tengan un seguimiento adecuado de versiones_
- **Responsable**: Frank Hinojosa
- **Rama**: `feature/AUTO_INCR_VERSION`
- **Objetivo**: Asegurar que las builds automatizadas cuenten con un seguimiento de versiones adecuado mediante la gestion del campo build_number

### [#14](https://github.com/OliverHz28/PC3Proyecto10/issues/14) Añadir modulo de logging
- **User story**  
    **As a** _desarrollador_  
    **I need** _crear un modulo `logger.py` para la gestion de logs_  
    **So that** _todos los scripts tengan la capacidad de diagnostico y rastros de auditoría_
- **Responsable**: Frank Hinojosa
- **Rama**: `feature/ADD_LOGGING`
- **Objetivo**: Equipar los scripts con la capacidaded de diagnostico y rastreo de auditoria

### [#15](https://github.com/OliverHz28/PC3Proyecto10/issues/15) Validar el titulo de PR
- **User story**  
    **As a** _desarrollador_  
    **I need** _que el script `check_pr.py` compruebe el archivo pr_<id>_title.txt cumpla con el patron  `^[A-Z]{3,5}-\d+: .+`_  
    **So that** _los títulos de los Pull Requests sean claros y faciles de entender para todo el equipod_
- **Responsable**: Germain Choquechambi
- **Rama**: `feature/validar-pr`
- **Objetivo**: Extender el script check_pr.py para que sea capaz de leer el contenido de archivos de titulo de PR y validar su formato

### [#16](https://github.com/OliverHz28/PC3Proyecto10/issues/16) Verificar que el changelog este actualizado
- **User story**  
    **As a** _desarrollador_  
    **I need** _que el script `check_pr.py` revise si el archivo `CHANGELOG.md` incluye una seccion para el PR actual (por ejemplo, ## PR 201_ )
    **So that** _podamos mantener un registro claro de los cambios realizados por cada PR_
- **Responsable**: Germain Choquechambi
- **Rama**: `feature/validar-pr`
- **Objetivo**: Añadir una funcionalidad al script check_pr.py que permita inspeccionar el contenido del archivo CHANGELOG.md

### [#17](https://github.com/OliverHz28/PC3Proyecto10/issues/17) Validar formato de los mensajes de commit
- **User story**  
    **As a** _desarrollador_  
    **I need** _que el script `check_pr.py` revise que los mensajes de commit tengan un formato claro y uniforme_  
    **So that** _el historial de cambios sea mas facil de leer y mantener para todo el equipo_
- **Responsable**: Germain Choquechambi
- **Rama**: `feature/validar-pr`
- **Objetivo**: Añadir una funcionalidad al script check_pr.py que permita leer y evaluar el formato de los mensajes de commit.

### [#18](https://github.com/OliverHz28/PC3Proyecto10/issues/18) Generar informe de validacion
- **User story**  
    **As a** _desarrollador_  
    **I need** _que `check_pr.py` cree un archivo pr_report.md con las secciones Título, Changelog, Commits, Lint y Tests, marcando cada una con OK o Fail_  
    **So that** _pueda tener un resumen automático y rapido del estado de cada PR._
- **Responsable**: Germain Choquechambi
- **Rama**: `feature/validar-pr`
- **Objetivo**: Proporcionar a un resumen automatico y rapido del estado de los pull request, centralizando los resultados de varias verificaciones en un unico archivo `pr_report.md`

### [#19](https://github.com/OliverHz28/PC3Proyecto10/issues/19) Extender workflow de Actions para PRs
- **User story**  
    **As a** _miembro del equipo de DevOps_  
    **I need** _actualizar pr_validation.yaml con un pipeline de validacion_  
    **So that** _multiples PRs puedan validarse automAticamente en paralelo usando estrategia matrix de GitHub Actions_
- **Responsable**: Edy Serrano
- **Rama**: `feature/extender-workflow`
- **Objetivo**: Automatizar y paralelizar el proceso de validación de los pull requests, utilizando github actions y su estrategia matrix

### [#20](https://github.com/OliverHz28/PC3Proyecto10/issues/20) Mejorar lint_all.sh con manejo de errores
- **User story**  
    **As a** _ingeniero de integracion de CI_  
    **I need** _un script lint_all.sh mejorado con manejo adecuado de errores_  
    **So that** _los problemas de linting se identifiquen y reporten claramente tanto en entornos locales como de CI_
- **Responsable**: Edy Serrano
- **Rama**: `feature/mejora-lint`
- **Objetivo**: Refactorizar el script `lint_all.sh` para gestionar de forma proactiva y clara los errores que puedan surgir durante el proceso de linting

### [#21](https://github.com/OliverHz28/PC3Proyecto10/issues/21) Configurar simulación con act pull_request
- **User story**  
    **As a** _ingeniero de desarrollo local_  
    **I need** _configurar y probar workflows de GitHub Actions localmente usando act_  
    **So that** _la validacion de PR pueda probarse sin hacer push al repositorio remoto_
- **Responsable**: Edy Serrano
- **Rama**: `feature/workflow-pull_request`
- **Objetivo**: Permitir probar y depurar los workflows de github actions de forma local antes de hacer un push al repositorio remoto

### [#24](https://github.com/OliverHz28/PC3Proyecto10/issues/24) Configurar simulación con act pull_request
- **Historias de usuario relacionados**
  
  [#15](#15-validar-el-titulo-de-pr) Validar formato del título de PR
  
  [#16](#16-verificar-que-el-changelog-este-actualizado) Verificar que el changelog esté actualizado
  
  [#17](#17-validar-formato-de-los-mensajes-de-commit) Validar formato de los mensajes de commit
  
  [#18](#18-generar-informe-de-validacion) Generar informe de 
  validacion  
- **Responsable**: Germain Choquechambi
- **Rama**: `feature/validar-pr`
- **Objetivo**: Automatizar la validación de Pull Requests mediante el `check_pr.py` para  que analice los archivos de la PR (título, changelog, commits), ejecute linters y tests, y genere un reporte `pr_report.md` con los resultados de la validacion

### [#29](https://github.com/OliverHz28/PC3Proyecto10/issues/29) Agregar pruebas unitarias para check_pr.py
- **User story**  
    **As a** _desarrollador_  
    **I need** _agregar pruebas unitarias para validar el formato del título, los commits y la sección en el CHANGELOG.md en pull requests_  
    **So that** _pueda asegurarme de que las PRs cumplan con las reglas definidas antes de ser revisadas o integradas_
- **Responsable**: Germain Choquechambi
- **Rama**: `feature/tests-check-pr`
- **Objetivo**: Implementar pruebas unitarias para garantizar la calidad de las funciones de validacion existentes.

## Flujo de Trabajo
Se utilizo la estrategia **Git Flow** para organizar el desarrollo:

- **Ramas principales**:
  - `main`: Contiene la version estable y lista para produccion.
  - `develop`: Integra las funcionalidades completadas antes de pasar a `main`.

- **Ramas de soporte**:
  - `feature/*`: Cada nueva funcionalidad o issue se desarrolla en una rama `feature/nombre-issue` creada desde `develop`.
  - `hotfix/*`: Para corregir errores críticos detectados en `main`.
  - `release/*`: Preparacion de nuevas versiones antes de fusionar a `main`.

## Ejecucion del Proyecto

Continuando con los pasos del  sprint 1, a continuacion seguir los siguientes pasos:

1.**Instalar las nuevas dependencias**
  
  ```bash
  pip install -r requirements.txt
  ```
2.**Ejecucion de `check_pr.py`**
    
  Esto generara un reporte `pr_report.md` de los pull request
  
  ```bash
  python3 scripts/check_pr.py
  ```

  Ejecucion de sus tests
  
  ```bash
  pytest tests/test_check_pr.py
  ```

2.**Ejecucion de `config_modifier.py`**
      
  Esto generara tambien la carpeta logs
  
  ```bash
  python3 src/config_modifier.py
  ```
  Ejecucion de sus tests
  
  ```bash
  pytest tests/test_config_modifier.py
  ```

3.**Instalacion de act**

  Previa instalacion del docker, instalamos el act
    
  ```bash
  curl -s https://raw.githubusercontent.com/nektos/act/master/install.sh | sudo bash
  ```

  Movemos el act a una carpeta global

  ```bash
  sudo mv ./bin/act /usr/local/bin/act
  ```
4.Ejecucion del act 
  ```bash
  act pull_request
  ```

## Sprint 3

Realizado del 18 al 19 de junio de 2025, se compone de los siguiente:

### Objetivos

* Refinar validaciones y documentación:

  - Mejorar **lint_all.sh** para:

     * Incluir `bandit -r src/` y reportar vulnerabilidades (Fall back si > 0).
     * Actualizar `.flake8` con reglas específicas de estilo de equipo (ej., max-line-length = 100, no ignorar errores).
  - Extender **`check_pr.py`** para:

     * Verificar que no existan tickets duplicados en `CHANGELOG.md` (evitar doble mención de `<id>`).
     * Validar que el PR description (`pr_<id>_body.md`) incluya al menos 200 caracteres y contenga un "Resumen" y "Cambios" secciones.
     * Incluir en `pr_report.md` una sección "Mejoras sugeridas" si se detectan líneas de código duplicadas (usar Python para buscar duplicados en `src/`).
  - Ajustar **`pr_validation.yaml`** para:

     * Agregar un job `security-scan` que ejecute `bandit` y `shellcheck`, y falle si hay vulnerabilidades críticas.
     * Enviar notificación simulada al equipo (imprimir en consola) si hay fallos de seguridad.
  - Completar **logs** en `pr_simulation/<id>/logs/`:

     * Guardar salida de `lint_all.sh` en `logs/lint.log`.
     * Guardar salida de `pytest` en `logs/tests.log`.
     * Guardar `bandit_report.json` si aplica.

### 1. Ramas

- `feature/workflow-scan`, desarrollado por **Edy Serrano** 
- `feature/validar-pr-completo`, desarrollado por **Germain Choquechambi** 
- `feature/logs-pr`, desarrollado por **Frank Hinojosa** 

### 2. Issues

- [#39](#41-Registro-de-lint_all.sh) Registro de lint_all.sh
- [#41](#41-Job-de-Security-Scan-en-CI) Job de Security Scan en CI
- [#43](#43-Automatizacion-de-revisiones-de-PR:-estructura,-cambios-y-mejoras-sugeridas) Automatizacion de revisiones de PR: estructura, cambios y mejoras sugeridas
- [#44](#41-Registro-de-salida-de-Pytest-para-simulaciones-de-PR) Registro de salida de Pytest para simulaciones de PR
- [#45](#41-Registro-de-reporte-de-Bandit) Registro de reporte de Bandit
 

### 3. Pull Request

#### 3.1 Aceptados
- [#46](https://github.com/OliverHz28/PC3Proyecto10/pull/46) : feat[[#43]](#46-Feature/validar-pr-completo): Feature/validar pr completo
- [#47](https://github.com/OliverHz28/PC3Proyecto10/pull/47) : feat[[#41]](#47-feature/workflow-scan-a-rama-develop): Feature/workflow scan a rama develop 
- [#48](https://github.com/OliverHz28/PC3Proyecto10/pull/48) : feat[[#45]](#45-merge-Feature/logs-pr-a-rama-develop) :
merge Feature/logs-pr a rama develop

## Ejecucion del Proyecto

Continuando con los pasos del  sprint 2, a continuacion seguir los siguiente paso:

- Ejecucion del act 
  ```bash
  act pull_request
  ```

## Demostracion en video

[Sprint 3 (19/06/2025) Grupo 6 Proyecto 10 ](https://www.youtube.com/watch?v=EdfvsKFbDEw)
