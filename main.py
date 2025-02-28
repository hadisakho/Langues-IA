# main.py
import config
from modules import speech_recognition_module, vision_module, text_module
from models import language_model

def main():
    # Initialisation des modules et modèles
    print("Démarrage du projet d'IA d'apprentissage des langues...")
    
    # Exemple d'utilisation du module de reconnaissance vocale
    audio_input = speech_recognition_module.capture_audio()
    if audio_input:
        recognized_text = speech_recognition_module.recognize_speech(audio_input)
        print("Texte reconnu depuis l'audio :", recognized_text)
    
    # Exemple d'utilisation du module de vision pour analyser une image (texte ou visuel)
    #image_path = "/Users/sohan-henriadou/Downloads/hq720.jpg"
    #image_result = vision_module.process_image(image_path)
    #print("Résultat du traitement visuel :", image_result)
    
    # Exemple d'utilisation du module texte pour l'apprentissage de la lecture/écriture
    sample_text = "Bonjour, bienvenue dans votre cours de langue!"
    language_model_output = language_model.process_text(sample_text)
    text_module.display_text_learning(language_model_output)
    
    print("Fin du programme.")

if __name__ == '__main__':
    main()
