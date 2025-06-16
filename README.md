# Grupo 6 - PC3-proyecto10

## Team

| Miembro del Equipo | Codigo |
| :----------------- | :-------------------- | 
| **Choquecambi Germain** | `20211360A` |
| **Serrano Edy** | `20211229B` | 
| **Hinojosa Frank** | `20210345I`  | 

## Descripcion

**Proyecto 10 - Grupo 6**, enfocado en simular un flujo Pull Request completo y la revisión de código automatizada usando:

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

### 2. Isues

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
    chmod +x lint_all.sh
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


