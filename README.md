# BioHacker System 1.0 - Interfaz de Captura

Este proyecto contiene el Frontend y Backend básicos para ingresar datos de desarrollo personal a una base de datos SQL.

## Archivos incluidos
1. `frontend.html`: Pantalla de usuario con el formulario de captura.
2. `backend.py`: Servidor local programado en Python (usa el framework Flask).
3. `database.sql`: Esquema relacional para crear las tablas.

## Instrucciones de Instalación y Uso

**Requisitos previos:**
- Tener instalado Python en la computadora.
- Instalar la librería Flask abriendo la terminal y escribiendo: `pip install Flask`

**Pasos para usar el sistema:**
1. Ejecuta el archivo del backend en tu terminal con el comando: `python backend.py`
2. El servidor local se encenderá en el puerto 5000.
3. Haz doble clic en el archivo `frontend.html` para abrirlo en tu navegador de internet (Chrome, Edge, etc.).
4. Llena el formulario con tus horas de sueño y nivel de estrés y presiona "Guardar".
5. El backend recibirá los datos y simulará la orden SQL de inserción (`INSERT INTO`).