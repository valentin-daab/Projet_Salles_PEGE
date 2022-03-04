# Explorateur de fichiers
from tkinter import *
from tkinter.filedialog import askopenfilename
# Selenium / Webdriver
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import ElementNotInteractableException
# Autres
import time
import getpass

### Variables

URL = "https://monemploidutemps.unistra.fr/consult/calendar"
ETAGE = input("A quel étage cherchez vous une salle ? \n RDC : 0 \n 2 ème : 2 \n 3 ème : 3 \n")


### Choisir les chemins d'accès à chromedriver.exe et navigateur.exe

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


### Initialisation du webdriver

def init_webdriver():
    global driver
    option = webdriver.ChromeOptions()
    option.binary_location = browser_path
    s = Service(driver_path)
    driver = webdriver.Chrome(service = s, options = option)
    driver.get(URL)


### Connexion unistra

def get_user_info():
    global username 
    global password
    username = input('Identifiant UNISTRA?')
    password = getpass.getpass('Mot de passe UNISTRA?')

def connect():
    driver.find_element(By.ID, 'username').send_keys(username)
    driver.find_element(By.ID, 'password').send_keys(password)
    driver.find_element(By.ID, 'login-btn').click()

def check_login():
    try:
        driver.find_element(By.CLASS_NAME, 'login')
    except NoSuchElementException:
        return False
    return True

def connect_user():
    get_user_info()
    connect()
    while check_login():
        driver.find_element(By.ID, 'username').clear() #permet d'effacer l'input qui reste dans le login
        print('Mot de passe ou Identifiant incorrect, veuillez réessayer.')
        connect_user()
    return print('Connexion Réussie.')


### Personnaliser > Salles > PEGE 

def clicker_pour_modifier():
    driver.find_element(By.CSS_SELECTOR, '#app-toolbar > div > button.v-app-bar__nav-icon.hidden-md-and-up.v-btn.v-btn--flat.v-btn--icon.v-btn--round.theme--dark.v-size--default > span > i').click()
    time.sleep(5.0)
    driver.find_element(By.CSS_SELECTOR, '#unistra-schedule > div.v-application--wrap > div > nav > div.v-navigation-drawer__content > div > a:nth-child(1)').click() 
    time.sleep(5.0)
    driver.find_element(By.XPATH, '//strong[normalize-space()="Modifier la sélection"]').click() 
    time.sleep(5.0)
    driver.find_element(By.XPATH, ("(//i[@role='button'])[3]")).click() 
    time.sleep(4.0)
    driver.find_element(By.XPATH, ("(//i[@role='button'])[4]")).click()
    time.sleep(4.0)
    driver.find_element(By.XPATH, ("(//i[@role='button'])[7]")).click()
    time.sleep(4.0)
    driver.find_element(By.XPATH, ("(//i[@role='button'])[10]")).click()
    time.sleep(4.0)
    driver.find_element(By.XPATH, ("(//i[@role='button'])[12]")).click()
    time.sleep(4.0)


### Sélection salles RDC

def rdc() :
    driver.find_element(By.XPATH, ("(//div[@class='v-input--selection-controls__input'])[3]")).click()
    time.sleep(1.5)
    driver.find_element(By.XPATH, ("(//div[@class='v-input--selection-controls__input'])[4]")).click()
    time.sleep(1.5)
    driver.find_element(By.XPATH, ("(//div[@class='v-input--selection-controls__input'])[5]")).click()
    time.sleep(1.5)
    driver.find_element(By.XPATH, ("(//div[@class='v-input--selection-controls__input'])[6]")).click()
    time.sleep(1.5)
    driver.find_element(By.XPATH, ("(//div[@class='v-input--selection-controls__input'])[7]")).click()
    time.sleep(1.5)
    driver.find_element(By.XPATH, ("(//div[@class='v-input--selection-controls__input'])[8]")).click()
    time.sleep(1.5)
    driver.find_element(By.XPATH, ("(//div[@class='v-input--selection-controls__input'])[9]")).click()
    time.sleep(1.5)
    driver.find_element(By.XPATH, ("(//div[@class='v-input--selection-controls__input'])[10]")).click()
    time.sleep(1.5)
    driver.find_element(By.XPATH, ("(//div[@class='v-input--selection-controls__input'])[11]")).click()
    time.sleep(1.5)
    driver.find_element(By.XPATH, ("(//div[@class='v-input--selection-controls__input'])[12]")).click()
    time.sleep(1.5)
    driver.find_element(By.XPATH, ("(//div[@class='v-input--selection-controls__input'])[13]")).click()
    time.sleep(1.5)
    driver.find_element(By.XPATH, ("(//div[@class='v-input--selection-controls__input'])[14]")).click()
    time.sleep(1.5)
    driver.find_element(By.XPATH, ("(//div[@class='v-input--selection-controls__input'])[15]")).click()


### Sélection salles 2e

def deuxieme() :
    driver.find_element(By.XPATH, ("(//div[@class='v-input--selection-controls__input'])[16]")).click()
    time.sleep(1.5)
    driver.find_element(By.XPATH, ("(//div[@class='v-input--selection-controls__input'])[17]")).click()
    time.sleep(1.5)
    driver.find_element(By.XPATH, ("(//div[@class='v-input--selection-controls__input'])[18]")).click()


### Sélection salles 3e

def troisieme() :
    driver.find_element(By.XPATH, ("(//div[@class='v-input--selection-controls__input'])[19]")).click()
    time.sleep(1.5)
    driver.find_element(By.XPATH, ("(//div[@class='v-input--selection-controls__input'])[20]")).click()
    time.sleep(1.5)
    driver.find_element(By.XPATH, ("(//div[@class='v-input--selection-controls__input'])[21]")).click()
    time.sleep(1.5)
    driver.find_element(By.XPATH, ("(//div[@class='v-input--selection-controls__input'])[22]")).click()
    time.sleep(1.5)
    driver.find_element(By.XPATH, ("(//div[@class='v-input--selection-controls__input'])[23]")).click()
    time.sleep(1.5)
    driver.find_element(By.XPATH, ("(//div[@class='v-input--selection-controls__input'])[24]")).click()
    time.sleep(1.5)
    driver.find_element(By.XPATH, ("(//div[@class='v-input--selection-controls__input'])[25]")).click()
    time.sleep(1.5)
    driver.find_element(By.XPATH, ("(//div[@class='v-input--selection-controls__input'])[26]")).click()
    time.sleep(1.5)
    driver.find_element(By.XPATH, ("(//div[@class='v-input--selection-controls__input'])[27]")).click()
    time.sleep(1.5)
    driver.find_element(By.XPATH, ("(//div[@class='v-input--selection-controls__input'])[28]")).click()
    time.sleep(1.5)
    driver.find_element(By.XPATH, ("(//div[@class='v-input--selection-controls__input'])[29]")).click()
    time.sleep(1.5)
    driver.find_element(By.XPATH, ("(//div[@class='v-input--selection-controls__input'])[30]")).click()
    time.sleep(1.5)
    driver.find_element(By.XPATH, ("(//div[@class='v-input--selection-controls__input'])[31]")).click()


### Quel étage sélectionner en fonction du choix

def choix_etage() :
    if ETAGE =='0' :
        rdc()
    if ETAGE =='2' :
        deuxieme()
    if ETAGE =='3' :
        troisieme()
choix_etage()


### 