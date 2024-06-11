# FakeAPI Generator

Este proyecto es una aplicación desarrollada en Python utilizando el framework Flask, diseñada para crear APIs falsas de manera rápida y sencilla. Es útil para pruebas, desarrollo y demostraciones cuando no se dispone de un backend real.

## Tabla de Contenidos

- [Instalación](#instalación)
- [Uso](#uso)

## Instalación

1. Clona este repositorio:
    ```bash
    git clone https://github.com/tu-usuario/fake-api-generator.git
    cd fake-api-generator
    ```

2. Crea un entorno virtual e instala las dependencias:
    ```bash
    python -m venv venv
    source venv/bin/activate  # En Windows usa `venv\Scripts\activate`
    pip install -r requirements.txt
    ```

3. Configura las variables de entorno necesarias (si aplica). Puedes crear un archivo `.env` en la raíz del proyecto y definir las variables allí.

## Uso

1. Ejecuta la aplicación:
    ```bash
    flask run
    ```

2. La aplicación estará disponible en `http://127.0.0.1:5000/`.