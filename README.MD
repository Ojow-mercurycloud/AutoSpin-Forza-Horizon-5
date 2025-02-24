### FRANÇAIS

# 🚗 Automatisation des Wheelspins dans Forza Horizon 5

Ce script automatise les "Wheelspins" dans Forza Horizon 5. Il appuie sur "Entrée" toutes les secondes et détecte l'interface de vente de voiture pour sélectionner la troisième option.

## 📋 Prérequis

- Python 3.x
- Tesseract OCR

## 🛠️ Installation

### Étape 1 : Installer Python

Assurez-vous que Python est installé sur votre système. Vous pouvez le télécharger depuis [python.org](https://www.python.org/downloads/).

### Étape 2 : Installer Tesseract OCR

1. Téléchargez et installez Tesseract depuis [ce lien](https://github.com/tesseract-ocr/tesseract).
2. Ajoutez le chemin vers le dossier contenant `tesseract.exe` à la variable d'environnement `PATH`. Par défaut, il est souvent installé dans `C:\Program Files\Tesseract-OCR`.

### Étape 3 : Installer les dépendances Python

Ouvrez une invite de commande et exécutez la commande suivante pour installer les bibliothèques nécessaires :

```bash
pip install pyautogui opencv-python pytesseract
```

## ⚙️ Configuration

1. Assurez-vous que le chemin vers l'exécutable Tesseract est correct dans le script Python. Modifiez la ligne suivante si nécessaire :

```python
pytesseract.pytesseract.tesseract_cmd = r'D:\Tesseract\tesseract.exe'
```

## 🚀 Utilisation

1. Lancez le jeu Forza Horizon 5 et assurez-vous que l'interface est visible.
2. Exécutez le script Python :

```bash
python script.py
```

Le script appuiera automatiquement sur "Entrée" toutes les secondes et détectera l'interface de vente de voiture pour sélectionner la troisième option.

## 📝 Remarques

- Assurez-vous que la résolution de l'écran est constante pour que la reconnaissance de texte fonctionne correctement.
- Ajustez le délai dans le script si nécessaire pour correspondre à votre configuration.

---


### ENGLISH


# 🚗 Automating Wheelspins in Forza Horizon 5

This script automates "Wheelspins" in Forza Horizon 5. It presses "Enter" every second and detects the car sale interface to select the third option.

## 📋 Prerequisites

- Python 3.x
- Tesseract OCR

## 🛠️ Installation

### Step 1: Install Python

Ensure Python is installed on your system. You can download it from [python.org](https://www.python.org/downloads/).

### Step 2: Install Tesseract OCR

1. Download and install Tesseract from [this link](https://github.com/tesseract-ocr/tesseract).
2. Add the path to the folder containing `tesseract.exe` to the `PATH` environment variable. By default, it is often installed in `C:\Program Files\Tesseract-OCR`.

### Step 3: Install Python Dependencies

Open a command prompt and run the following command to install the necessary libraries:

```bash
pip install pyautogui opencv-python pytesseract
```

## ⚙️ Configuration

1. Ensure the path to the Tesseract executable is correct in the Python script. Modify the following line if necessary:

```python
pytesseract.pytesseract.tesseract_cmd = r'D:\Tesseract\tesseract.exe'
```

## 🚀 Usage

1. Launch the Forza Horizon 5 game and ensure the interface is visible.
2. Run the Python script:

```bash
python script.py
```

The script will automatically press "Enter" every second and detect the car sale interface to select the third option.

## 📝 Notes

- Ensure the screen resolution is constant for text recognition to work correctly.
- Adjust the delay in the script if necessary to match your setup.
