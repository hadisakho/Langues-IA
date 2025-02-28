import speech_recognition as sr

def capture_audio():
    """Capture l'audio via le microphone."""
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Parlez maintenant...")
        # Ajustement du bruit ambiant pour une meilleure précision
        recognizer.adjust_for_ambient_noise(source, duration=1)
        audio = recognizer.listen(source)
    return audio

def recognize_speech(audio):
    """Convertit l'audio en texte en utilisant l'API Google Speech Recognition."""
    try:
        # Vous pouvez changer la langue si nécessaire, ici 'fr-FR' pour le français.
        text = sr.Recognizer().recognize_google(audio, language='fr-FR')
        return text
    except sr.UnknownValueError:
        return "La reconnaissance vocale n'a pas compris ce que vous avez dit."
    except sr.RequestError as e:
        return f"Erreur lors de la requête à l'API de reconnaissance vocale: {e}"

if __name__ == "__main__":
    audio_data = capture_audio()
    result = recognize_speech(audio_data)
    print("Vous avez dit :", result)
