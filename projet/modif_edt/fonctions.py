from tkinter import *
from tkinter.filedialog import askopenfilename

# Choisir les chemins d'accès à chromedriver.exe et navigateur.exe

def get_paths():
    global driver_path
    global browser_path
    root = Tk()
    root.update()
    print('Sélectionnez le fichier chromedriver.exe')
    driver_path = askopenfilename(title = 'Sélectionnez le fichier chromedriver.exe')
    print('Sélectionnez le .exe du navigateur')
    root.withdraw()
    browser_path = askopenfilename(title = 'Sélectionnez le .exe du navigateur')
    root.destroy()


# Initialisation du webdriver