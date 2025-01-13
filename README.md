# Proyecto: Audio to Text en Python

Este proyecto convierte audio en texto utilizando Python y la librería `speech_recognition`. Puedes cargar archivos de audio y obtener su transcripción en texto. Ideal para quienes necesitan transformar grabaciones o audios a formato escrito.

### Descripción de la librería `speech_recognition`

La librería `speech_recognition` es una herramienta poderosa para convertir audio a texto en Python. Ofrece soporte para varios motores de reconocimiento de voz, tanto en línea como sin conexión. Puedes usar la API de Google para el reconocimiento en línea o utilizar CMU Sphinx si necesitas una opción sin conexión. `speech_recognition` es fácil de usar y es ampliamente utilizada en proyectos de procesamiento de lenguaje natural.

## Requisitos

- Python 3.x
- pip (gestor de paquetes de Python)

## Instalación

Sigue estos pasos para configurar tu entorno de desarrollo e instalar las dependencias necesarias:

### 1. Clonar el repositorio

Si aún no tienes el repositorio en tu máquina local, clónalo con el siguiente comando:
```bash
git clone https://github.com/tuusuario/nombre-del-repositorio.git
```
### 2. Crear un entorno virtual

Es recomendable usar un entorno virtual para gestionar las dependencias del proyecto. Sigue estos pasos:

#### En Windows:
```bash
python -m venv env
```
#### En MacOS/Linux:
```bash
python3 -m venv env
```
### 3. Activar el entorno virtual

#### En Windows:
```bash
.\env\Scripts\activate
```
#### En MacOS/Linux:
```bash
source env/bin/activate
```
Verás que el prompt de la terminal cambia para mostrar que estás en el entorno virtual.

### 4. Instalar las dependencias

Una vez activado el entorno virtual, instala las librerías necesarias para el proyecto:
```bash
pip install -r requirements.txt
```
Si no tienes un archivo `requirements.txt`, puedes instalar manualmente las librerías requeridas:
```bash
pip install SpeechRecognition pyaudio
```
- **SpeechRecognition**: Esta librería facilita la conversión de audio en texto. Utiliza motores de reconocimiento de voz como Google Web Speech API o el motor local CMU Sphinx.
- **PyAudio**: Es necesaria para trabajar con archivos de audio en tiempo real o grabar desde el micrófono.

### 5. Configuración opcional

Si vas a utilizar la API de Google para el reconocimiento de voz, puedes necesitar instalar `pyaudio` o configuraciones adicionales dependiendo del sistema operativo.

### 6. Uso

Para usar el script de transcripción de audio, solo debes ejecutar el siguiente comando en la terminal (dentro del entorno virtual):

```bash
python audio_to_text.py <ruta_del_audio>
```
Asegúrate de reemplazar `<ruta_del_audio>` con la ubicación del archivo de audio que deseas convertir.

### 7. Ejemplo

Si tienes un archivo `audio.wav` en la misma carpeta que el script, puedes correr el siguiente comando:
```bash
python audio_to_text.py audio.wav
```
El script procesará el audio y devolverá el texto transcrito en la consola.
## Contribuciones

Si deseas contribuir a este proyecto, por favor sigue estos pasos:

1. Forkea el repositorio.
2. Crea una nueva rama (git checkout -b feature/nueva-funcionalidad).
3. Realiza tus cambios.
4. Realiza un commit (git commit -am 'Añadir nueva funcionalidad').
5. Sube tus cambios (git push origin feature/nueva-funcionalidad).
6. Abre un Pull Request.

## Licencia

Este proyecto está bajo la Licencia MIT. Consulta el archivo [LICENSE](LICENSE) para más detalles.

