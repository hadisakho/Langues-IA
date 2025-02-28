# modules/vision_module.py
import cv2
import pytesseract

def process_image(image_path):
    """Analyse une image pour en extraire du texte ou des informations visuelles."""
    # Chargement de l'image
    image = cv2.imread(image_path)
    if image is None:
        return "Image non trouvée ou impossible à charger."
    
    # Traitement d'image simple : conversion en niveaux de gris
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    
    # Extraction de texte avec Tesseract
    extracted_text = pytesseract.image_to_string(gray, lang='fra')
    return extracted_text if extracted_text.strip() != "" else "Aucun texte détecté."
