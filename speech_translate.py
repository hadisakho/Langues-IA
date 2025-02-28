import speech_recognition as sr
sr.FLAC_EXECUTABLE = "/opt/homebrew/bin/flac"
from googletrans import Translator
import pyttsx3

def capture_audio():
    """Capture l'audio via le microphone."""
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Parlez maintenant...")
        # Ajuste le micro pour réduire le bruit ambiant
        recognizer.adjust_for_ambient_noise(source, duration=1)
        audio = recognizer.listen(source)
    return audio

def recognize_speech(audio):
    """Utilise l'API Google pour convertir l'audio en texte."""
    try:
        # La langue source est le français
        text = sr.Recognizer().recognize_google(audio, language='fr-FR')
        return text
    except sr.UnknownValueError:
        return None
    except sr.RequestError as e:
        print(f"Erreur lors de la requête à l'API : {e}")
        return None

def translate_text(text, dest_lang="en"):
    """Traduit le texte fourni dans la langue spécifiée (anglais par défaut)."""
    translator = Translator()
    translated = translator.translate(text, src='fr', dest='en')
    return translated.text

if __name__ == '__main__':
    audio_data = capture_audio()
    original_text = recognize_speech(audio_data)
    
    if original_text:
        print("Texte reconnu :", original_text)
        translated_text = translate_text(original_text, dest_lang="en")
        print("Traduction en anglais :", translated_text)
        engine = pyttsx3.init()
        engine.setProperty('voice', 'com.apple.eloquence.en-EN.Reed')
        engine.say(translated_text)
        engine.runAndWait()
        engine.stop()
    else:
        print("Aucun texte n'a été reconnu.")
