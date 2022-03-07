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
from rich import pretty
from rich.console import Console
console = Console()
import webbrowser
from colorama import Fore
from collections import defaultdict
from datetime import datetime
import pandas as pd
import getpass
import time
import re

# Choisir chemin d'accès
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


# Selenium 
def web():
    global driver
    option = webdriver.ChromeOptions()
    option.add_experimental_option("detach", True)
    option.add_experimental_option('excludeSwitches', ['enable-logging'])
    option.binary_location = browser_path
    s = Service(driver_path)
    driver = webdriver.Chrome(service = s, options = option)
    driver.get('https://monemploidutemps.unistra.fr/consult/calendar')


# Connexion
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
        driver.find_element(By.ID, 'username').clear()
        print('Mot de passe ou Identifiant incorrect, veuillez réessayer.')
        connect_user()
    return print('Connexion Réussie.')


# Deselect
def deselect_clicker():
    driver.find_element(By.CLASS_NAME, 'v-list-item__action.my-0.mr-3').click()
    time.sleep(1.0)

def deselect_checker():
    try:
        driver.find_element(By.CLASS_NAME, 'v-list-item__action.my-0.mr-3')
    except NoSuchElementException:
        return False
    return True

def deselect():
    while deselect_checker():
        deselect_clicker()
    print('Déselection Réussie.')


# Personnaliser edt
def customize():
    driver.find_element(By.CSS_SELECTOR, '#app-toolbar > div > button.v-app-bar__nav-icon.hidden-md-and-up.v-btn.v-btn--flat.v-btn--icon.v-btn--round.theme--dark.v-size--default > span > i').click()
    time.sleep(5.0)
    driver.find_element(By.CSS_SELECTOR, '#unistra-schedule > div.v-application--wrap > div > nav > div.v-navigation-drawer__content > div > a:nth-child(1)').click()
    time.sleep(5.0)
    deselect()
    time.sleep(2.0)
    driver.find_element(By.XPATH, '//strong[normalize-space()="Modifier la sélection"]').click()
    time.sleep(5.0)
    # Cliquer sur 'Salles'
    driver.find_element(By.XPATH, ("(//i[@role='button'])[3]")).click()
    time.sleep(4.0)
    # Cliquer sur 'Foret Noire'
    driver.find_element(By.XPATH, ("(//i[@role='button'])[4]")).click()
    time.sleep(4.0)
    # Cliquer sur 'PEGE'
    driver.find_element(By.XPATH, ("(//i[@role='button'])[7]")).click()
    time.sleep(4.0)
    # Cliquer sur 'FSEG'
    driver.find_element(By.XPATH, ("(//i[@role='button'])[10]")).click()
    time.sleep(4.0)
    # Cliquer sur 'FSEG-Salles de cours'
    driver.find_element(By.XPATH, ("(//i[@role='button'])[12]")).click()
    time.sleep(4.0)


# Sélection rdc
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


# Sélection deuxième étage
def deuxieme() :
    driver.find_element(By.XPATH, ("(//div[@class='v-input--selection-controls__input'])[16]")).click()
    time.sleep(1.5)
    driver.find_element(By.XPATH, ("(//div[@class='v-input--selection-controls__input'])[17]")).click()
    time.sleep(1.5)
    driver.find_element(By.XPATH, ("(//div[@class='v-input--selection-controls__input'])[18]")).click()


# Séleciton troisième étage
def troisieme():
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
    time.sleep(1.5)


# Coche en fonction de l'étage
def choix_etage() :
    global etage
    etage = input("A quel étage cherchez vous une salle ? \n RDC : 0 \n 2 ème : 2 \n 3 ème : 3 \n")
    if etage =='0' :
        rdc()
    if etage =='2' :
        deuxieme()
    if etage =='3' :
        troisieme()
    driver.back()


### SCRAPING ###
def get_today_events():
    global today_events
    today_events = driver.find_element(By.CLASS_NAME, 'v-calendar-daily__day.v-present').get_attribute('outerHTML')

def get_sep_events():
    global sep_events
    sep_events = []
    sep_events = re.findall('div class="v-event-timed onsecondary--text"(.*?)</div></div>', today_events)
    sep_events= str(sep_events)

def get_rooms():
    global rooms
    rooms = re.findall('<br>(?=A )(.*?)\'', sep_events)

def get_top_pixels():
    global top_pixels
    top_pixels = re.findall('top: (.*?)px;', sep_events)
    top_pixels = [int(p) for p in top_pixels]

def get_height_pixels():
    global height_pixels
    height_pixels = re.findall('height: (.*?)px;', sep_events)
    height_pixels = [int(p) for p in height_pixels]

def get_occupation_start():
    global occupation_start_numbers
    global occupation_start_in_hours
    occupation_start_numbers = [(7 + ((p / 20) * 0.5)) * 60 for p in top_pixels]
    df1 = pd.DataFrame({'start': occupation_start_numbers})
    df1 = pd.to_datetime(df1.start, unit='m').dt.strftime('%H:%M')
    occupation_start_in_hours = df1.values.tolist()

def get_occupation_duration():
    global occupation_duration
    global occupation_duration_in_hours
    occupation_duration = [(((p / 20) * 0.5) * 60) for p in height_pixels]
    df = pd.DataFrame({'duration': occupation_duration})
    df = pd.to_datetime(df.duration, unit='m').dt.strftime('%H:%M')
    occupation_duration_in_hours = df.values.tolist()

def get_occupation_end():
    global occupation_end_in_hours
    occupation_end_in_minutes = [x + y for x, y in zip(occupation_start_numbers, occupation_duration)]
    df2 = pd.DataFrame({'end': occupation_end_in_minutes})
    df2 = pd.to_datetime(df2.end, unit='m').dt.strftime('%H:%M')
    occupation_end_in_hours = df2.values.tolist()


### HEURES SALLES ###
def get_now_time():
    global now_time
    now = datetime.now()
    now_time = now.strftime("%H:%M")

def choose_time():
    global now_time
    now_time = input('Quelle heure ? Répondre sous la forme HH:MM \n')

def get_time():
    choice = int(
        input('Quand veux-tu utiliser la salle? \n Maintenant (0) \n Plus tard (1) \n'))
    if choice == 0:
        get_now_time()
        print('Heure actuelle :', now_time)
    if choice == 1:
        choose_time()
        print('Heure choisie :', now_time)


# Dictionnaire
def get_dict():
    global dict_content
    dict_content = defaultdict(list)
    start_end = [list(t) for t in zip(occupation_start_in_hours, occupation_end_in_hours)]
    for x,y in zip(rooms, start_end):
        dict_content[x].append(y)
    dict_content = {key : sorted(dict_content[key]) for key in sorted(dict_content)}

### SALLES OCCUPEES ###

def liste_salles():
    global liste_totale
    global liste_salles_0
    global liste_salles_2
    global liste_salles_3
    liste_salles_0 = ['A 015','A 016','A 017','A 018','A 019','A 020','A 021','A 022','A 023','A 024','A 025','A 026','A 027']
    liste_salles_2 = ['A 210','A 231', 'A 233']
    liste_salles_3 = ['A 310','A 311','A 312','A 313','A 314','A 326','A 327','A 328','A 329','A 330','A 331','A 333','A 336']
    liste_totale = [liste_salles_0, liste_salles_2, liste_salles_3]

def etage_liste():
    global etage
    if etage == '3' :
        etage = int(etage)-1
    if etage == '2' :
        etage = int(etage)-1
    if etage == '0' :
        etage = 0

def free_room():
    global gen
    global salle_libre  
    h = 0
    salle_libre = []   
    gen = (x for x in liste_totale[etage] if x not in dict_content.keys())    
    for x in gen:
        salle_libre += [x]
    for x in salle_libre :
        console.print('La salle', salle_libre[h], 'est libre toute la journée', style="bold red")
        h += 1

def sep_event_type():
    global elem
    global elem_double
    global elem_triple
    global elem_quad
    global single_event
    global double_event
    global triple_event
    global quad_event
    single_event = []
    double_event = []
    triple_event = []
    quad_event = []
    for keys in dict_content:
        if len(dict_content[keys]) == 1:
            single_event.append(keys)
        if len(dict_content[keys]) == 2:
            double_event.append(keys)
        if len(dict_content[keys]) == 3:
            triple_event.append(keys)
        if len(dict_content[keys]) == 4:
            quad_event.append(keys)

def check_single_event():
    z = 0
    for i in single_event:
        elem = dict_content[str(i)]
        if (elem[0][0] < now_time < elem[0][1]):
            print(Fore.RED + "La salle", single_event[z],"est occupée jusqu'à :",elem[0][1])
            z += 1
        if (now_time < elem[0][0]):
            print(Fore.GREEN + "La salle", single_event[z],"est libre jusqu'à :", elem[0][0])
            z += 1
        if (now_time > elem[0][1]):
            print(Fore.GREEN + "La salle", single_event[z],"est libre pour le reste de la journée")
            z += 1

def check_double_event():
    j = 0
    for element in double_event :
        elem_double = dict_content[str(element)]
        if now_time < elem_double[0][0]:
            print(Fore.GREEN + "La salle", double_event[j], "est libre jusqu'à", elem_double[0][0])
        if (elem_double[0][0] < now_time < elem_double[0][1]): 
            print(Fore.RED + "La salle",double_event[j], "est occupée jusqu'à :", elem_double[0][1]) 
            j += 1
        if (elem_double[0][1] < now_time < elem_double[1][0]):
            print(Fore.GREEN + "La salle", double_event[j], "est libre jusqu'à", elem_double[1][0])
            j += 1
        if (elem_double[1][0] < now_time < elem_double[1][1]): 
            print(Fore.RED + "La salle", double_event[j], "est occupée jusqu'à :", elem_double[1][1])
            j += 1
        if elem_double[1][1] < now_time:
            print(Fore.GREEN + "La salle", double_event[j], "est libre pour le reste de la journée")
            j += 1

def check_triple_event():
    a = 0
    for element in triple_event:
        elem_triple = dict_content[str(element)]
        if now_time < elem_triple[0][0]:
            print(Fore.GREEN + "La salle", double_event[a], "est libre jusqu'à :", elem_triple[0][0])
        if elem_triple[0][0] < now_time < elem_triple[0][1]: 
            print(Fore.RED + "La salle", triple_event[a], "est occupée jusqu'à :", elem_triple[0][1]) 
            a += 1
        if elem_triple[0][1] < now_time < elem_triple[1][0]: 
            print(Fore.GREEN + "La salle", triple_event[a], "est libre jusqu'à :", elem_triple[1][0])
            a += 1   
        if elem_triple[1][0] < now_time < elem_triple[1][1]: 
            print(Fore.RED + "La salle", triple_event[a], "est occupée jusqu'à :", elem_triple[1][1])
            a += 1
        if elem_triple[1][1] < now_time < elem_triple[2][0]: 
            print(Fore.GREEN + "La salle", triple_event[a], "est occupée jusqu'à :", elem_triple[2][0])
            a += 1    
        if elem_triple[2][0] < now_time < elem_triple[2][1]:
            print(Fore.RED + "La salle", triple_event[a], "est occupée jusqu'à :", elem_triple[2][1])
            a += 1
        if elem_triple[2][1] < now_time:
            print(Fore.GREEN + "La salle", triple_event[a], "est libre pour le reste de la journée")
            a += 1

def check_quad_event():
    q = 0
    for element in quad_event:
        elem_quad = dict_content[str(element)]
        if now_time < elem_quad[0][0]:
            print(Fore.GREEN + "La salle", quad_event[q], "est libre jusqu'à :", elem_quad[0][0])
            q += 1
        if elem_quad[0][0] < now_time < elem_quad[0][1]:
            print(Fore.RED + "La salle", quad_event[q], "est occupée jusqu'à :", elem_quad[0][1])
            q += 1
        if elem_quad[0][1] < now_time < elem_quad[1][0]:
            print(Fore.GREEN + "La salle", quad_event[q], "est libre jusqu'à :", elem_quad[1][0])
            q += 1
        if elem_quad[1][0] < now_time < elem_quad[1][1]:
            print(Fore.RED + "La salle", quad_event[q], "est occupée jusqu'à :", elem_quad[1][1])
            q += 1
        if elem_quad[1][1] < now_time < elem_quad[2][0]:
            print(Fore.GREEN + "La salle", quad_event[q], "est libre jusqu'à :", elem_quad[2][0])
            q += 1    
        if elem_quad[2][0] < now_time < elem_quad[2][1]:
            print(Fore.RED + "La salle", quad_event[q], "est occupée jusqu'à :", elem_quad[2][1])
            q += 1
        if elem_quad[2][1] < now_time < elem_quad[3][0]:
            print(Fore.GREEN + "La salle", quad_event[q], "est libre jusqu'à :", elem_quad[3][0])
            q += 1    
        if elem_quad[3][0] < now_time < elem_quad[3][1]:
            print(Fore.RED + "La salle", quad_event[q], "est occupée jusqu'à :", elem_quad[3][1])
            q += 1
        if elem_quad[3][1] < now_time:
            print(Fore.GREEN + "La salle", quad_event[q], "est libre pour le reste de la journée")
            q += 1

def customize2():
    driver.find_element(By.CSS_SELECTOR, '#app-toolbar > div > button.v-app-bar__nav-icon.hidden-md-and-up.v-btn.v-btn--flat.v-btn--icon.v-btn--round.theme--dark.v-size--default > span > i').click()
    time.sleep(5.0)
    driver.find_element(By.CSS_SELECTOR, '#unistra-schedule > div.v-application--wrap > div > nav > div.v-navigation-drawer__content > div > a:nth-child(1)').click() # ici en fonction  de la position de l'élément
    time.sleep(5.0)
    deselect()

def fin():
    driver.close()
    print("Merci d'avoir utilisé notre programme, afin de retrouver votre emploi du temps initial, veuillez le personnalier depuis la page qui va s'ouvrir dans quelques instants...")
    for i in range(0,5):
        print(5-i)
        time.sleep(1)
    print('0')
    webbrowser.open("https://monemploidutemps.unistra.fr/config")

       