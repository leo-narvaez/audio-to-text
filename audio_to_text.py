import speech_recognition as sr
from pydub import AudioSegment
import argparse

# Convertir archivo de audio a WAV si es necesario
def convert_to_wav(audio_file):
    audio = AudioSegment.from_file(audio_file)
    wav_file = "converted_audio.wav"
    audio.export(wav_file, format="wav")
    return wav_file

# Función para transcribir audio a texto
def transcribe_audio(audio_file):
    # Convertir el audio a WAV si no está en ese formato
    if not audio_file.endswith('.wav'):
        audio_file = convert_to_wav(audio_file)
    
    # Inicializar el reconocedor
    recognizer = sr.Recognizer()
    
    # Leer el archivo de audio
    with sr.AudioFile(audio_file) as source:
        # Obtener la duración total del audio
        audio = AudioSegment.from_wav(audio_file)
        audio_length = len(audio) / 1000  # Convertir de milisegundos a segundos
        step = 10  # Duración de cada fragmento en segundos
        transcription = ""

        for start in range(0, int(audio_length), step):
            end = min(start + step, int(audio_length))
            source.seek(start)  # Moverse al inicio del fragmento
            audio_data = recognizer.record(source, duration=end - start)  # Leer el fragmento
            # Transcribir el audio a texto
            try:
                text = recognizer.recognize_google(audio_data, language='es-ES')
                transcription += text + " "  # Agregar la transcripción del fragmento
            except sr.UnknownValueError:
                transcription += "[No se pudo entender el audio] "
            except sr.RequestError as e:
                print(f"Error en la solicitud; {e}")  # Mensaje de error
                return f"No se pudo solicitar resultados; {e}"

    return transcription

# Configuración de argparse para capturar el archivo de audio como parámetro
def parse_arguments():
    parser = argparse.ArgumentParser(description='Transcripción de audio a texto')
    parser.add_argument('audio_file', type=str, help='Ruta al archivo de audio')
    return parser.parse_args()

if __name__ == "__main__":
    # Capturar la ruta del archivo de audio desde los parámetros
    args = parse_arguments()
    audio_file_path = args.audio_file

    # Llamar a la función de transcripción
    transcription = transcribe_audio(audio_file_path)
    print("Transcripción:", transcription)
