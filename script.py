import pyautogui
import cv2
import numpy as np
import pytesseract
import time

# Chemin vers l'exécutable Tesseract
pytesseract.pytesseract.tesseract_cmd = r'D:\Tesseract\tesseract.exe'

def capture_screen():
    # Capture l'écran
    screenshot = pyautogui.screenshot()
    screenshot = cv2.cvtColor(np.array(screenshot), cv2.COLOR_RGB2BGR)
    return screenshot

def is_car_owned():
    screenshot = capture_screen()
    
    # Convertir l'image en niveaux de gris
    gray = cv2.cvtColor(screenshot, cv2.COLOR_BGR2GRAY)
    
    # Utiliser pytesseract pour extraire le texte
    text = pytesseract.image_to_string(gray, lang='fra')
    
    # Vérifier si le texte contient "VOITURE DÉJÀ POSSÉDÉE"
    if "VOITURE DÉJÀ POSSÉDÉE" in text:
        return True
    return False

def press_enter():
    # Simule l'appui sur la touche "Entrée"
    pyautogui.press('enter')

def sell_car():
    # Simule l'appui sur la touche pour vendre la voiture
    pyautogui.press('down', presses=2)  # Se déplacer vers la 3ème option
    pyautogui.press('down', presses=2)
    pyautogui.press('enter')

def main():
    while True:
        # Vérifie si l'interface de vente de voiture est présente
        if is_car_owned():
            sell_car()
        else:
            press_enter()
        
        # Attendre un peu entre chaque vérification
        time.sleep(1)

if __name__ == "__main__":
    main()