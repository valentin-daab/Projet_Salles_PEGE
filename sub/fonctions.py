# Explorateur de fichiers
import re
from time import sleep
import getpass
import pandas as pd
from datetime import datetime
from collections import defaultdict
import webbrowser
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
from rich.progress import track
from rich.console import Console


console = Console()

# Sélection des chemin d'accès à chromedriver.exe et navigateur.exe
def get_paths():
    global driver_path
    global browser_path
    root = Tk()
    root.update()
    console.print('Sélectionnez le fichier chromedriver.exe', style="#3399FF")
    driver_path = askopenfilename(
    title='Sélectionnez le fichier chromedriver.exe')
    console.print('Sélectionnez le .exe du navigateur', style="#3399FF")
    root.withdraw()
    browser_path = askopenfilename(title='Sélectionnez le .exe du navigateur')
    root.destroy()


### SELENIUM ###
def web():
    global driver
    option = webdriver.ChromeOptions()
    option.add_experimental_option("detach", True)
    option.add_experimental_option('excludeSwitches', ['enable-logging'])
    option.add_argument('headless')
    option.binary_location = browser_path
    s = Service(driver_path)
    driver = webdriver.Chrome(service=s, options=option)
    driver.get('https://monemploidutemps.unistra.fr/consult/calendar')


# Demande l'identifiant et le mot de passe UNISTRA
def get_user_info():
    global username
    global password
    username = input('Identifiant UNISTRA?')
    password = getpass.getpass('Mot de passe UNISTRA?')


# Renvoi des informations au navigateur et clique sur login
def connect():
    driver.find_element(By.ID, 'username').send_keys(username)
    driver.find_element(By.ID, 'password').send_keys(password)
    driver.find_element(By.ID, 'login-btn').click()


# Contrôle si encore sur la page de login ou pas
def check_login():
    try:
        driver.find_element(By.CLASS_NAME, 'login')
    except NoSuchElementException:
        return False
    return True


# Si encore sur la page de login > Réessayer, sinon > Connexion réussie
def connect_user():
    get_user_info()
    connect()
    while check_login():
        driver.find_element(By.ID, 'username').clear()
        console.print(
            'Mot de passe ou Identifiant incorrect, veuillez réessayer.', style='red')
        connect_user()
    return console.print('Connexion Réussie.', style='green')


# Clique sur les croix pour désélectionner
def deselect_clicker():
    driver.find_element(By.CLASS_NAME, 'v-list-item__action.my-0.mr-3').click()
    sleep(1.0)


# Contrôle s'il reste encore des croix à cliquer
def deselect_checker():
    try:
        driver.find_element(By.CLASS_NAME, 'v-list-item__action.my-0.mr-3')
    except NoSuchElementException:
        return False
    return True


# Tant qu'il reste des croix continue à cliquer dessus
def deselect():
    while deselect_checker():
        deselect_clicker()


# Aller dans l'onglet personnaliser
def customize():
    driver.find_element(
        By.CSS_SELECTOR, '#app-toolbar > div > button.v-app-bar__nav-icon.hidden-md-and-up.v-btn.v-btn--flat.v-btn--icon.v-btn--round.theme--dark.v-size--default > span > i').click()
    sleep(5.0)
    driver.find_element(
        By.CSS_SELECTOR, '#unistra-schedule > div.v-application--wrap > div > nav > div.v-navigation-drawer__content > div > a:nth-child(1)').click()
    sleep(5.0)
    deselect()
    sleep(2.0)
    driver.find_element(
        By.XPATH, '//strong[normalize-space()="Modifier la sélection"]').click()
    sleep(5.0)
    # Cliquer sur 'Salles'
    driver.find_element(By.XPATH, ("(//i[@role='button'])[3]")).click()
    sleep(4.0)
    # Cliquer sur 'Foret Noire'
    driver.find_element(By.XPATH, ("(//i[@role='button'])[4]")).click()
    sleep(4.0)
    # Cliquer sur 'PEGE'
    driver.find_element(By.XPATH, ("(//i[@role='button'])[7]")).click()
    sleep(4.0)
    # Cliquer sur 'FSEG'
    driver.find_element(By.XPATH, ("(//i[@role='button'])[10]")).click()
    sleep(4.0)
    # Cliquer sur 'FSEG-Salles de cours'
    driver.find_element(By.XPATH, ("(//i[@role='button'])[12]")).click()
    sleep(4.0)


# Sélection des salles au Rez-de-Chaussée
def rdc():
    driver.find_element(
        By.XPATH, ("(//div[@class='v-input--selection-controls__input'])[3]")).click()
    sleep(1.5)
    driver.find_element(
        By.XPATH, ("(//div[@class='v-input--selection-controls__input'])[4]")).click()
    sleep(1.5)
    driver.find_element(
        By.XPATH, ("(//div[@class='v-input--selection-controls__input'])[5]")).click()
    sleep(1.5)
    driver.find_element(
        By.XPATH, ("(//div[@class='v-input--selection-controls__input'])[6]")).click()
    sleep(1.5)
    driver.find_element(
        By.XPATH, ("(//div[@class='v-input--selection-controls__input'])[7]")).click()
    sleep(1.5)
    driver.find_element(
        By.XPATH, ("(//div[@class='v-input--selection-controls__input'])[8]")).click()
    sleep(1.5)
    driver.find_element(
        By.XPATH, ("(//div[@class='v-input--selection-controls__input'])[9]")).click()
    sleep(1.5)
    driver.find_element(
        By.XPATH, ("(//div[@class='v-input--selection-controls__input'])[10]")).click()
    sleep(1.5)
    driver.find_element(
        By.XPATH, ("(//div[@class='v-input--selection-controls__input'])[11]")).click()
    sleep(1.5)
    driver.find_element(
        By.XPATH, ("(//div[@class='v-input--selection-controls__input'])[12]")).click()
    sleep(1.5)
    driver.find_element(
        By.XPATH, ("(//div[@class='v-input--selection-controls__input'])[13]")).click()
    sleep(1.5)
    driver.find_element(
        By.XPATH, ("(//div[@class='v-input--selection-controls__input'])[14]")).click()
    sleep(1.5)
    driver.find_element(
        By.XPATH, ("(//div[@class='v-input--selection-controls__input'])[15]")).click()


# Sélection des salles du deuxième étage
def deuxieme():
    driver.find_element(
        By.XPATH, ("(//div[@class='v-input--selection-controls__input'])[16]")).click()
    sleep(1.5)
    driver.find_element(
        By.XPATH, ("(//div[@class='v-input--selection-controls__input'])[17]")).click()
    sleep(1.5)
    driver.find_element(
        By.XPATH, ("(//div[@class='v-input--selection-controls__input'])[18]")).click()


# Sélection des salles du troisième étage
def troisieme():
    driver.find_element(
        By.XPATH, ("(//div[@class='v-input--selection-controls__input'])[19]")).click()
    sleep(1.5)
    driver.find_element(
        By.XPATH, ("(//div[@class='v-input--selection-controls__input'])[20]")).click()
    sleep(1.5)
    driver.find_element(
        By.XPATH, ("(//div[@class='v-input--selection-controls__input'])[21]")).click()
    sleep(1.5)
    driver.find_element(
        By.XPATH, ("(//div[@class='v-input--selection-controls__input'])[22]")).click()
    sleep(1.5)
    driver.find_element(
        By.XPATH, ("(//div[@class='v-input--selection-controls__input'])[23]")).click()
    sleep(1.5)
    driver.find_element(
        By.XPATH, ("(//div[@class='v-input--selection-controls__input'])[24]")).click()
    sleep(1.5)
    driver.find_element(
        By.XPATH, ("(//div[@class='v-input--selection-controls__input'])[25]")).click()
    sleep(1.5)
    driver.find_element(
        By.XPATH, ("(//div[@class='v-input--selection-controls__input'])[26]")).click()
    sleep(1.5)
    driver.find_element(
        By.XPATH, ("(//div[@class='v-input--selection-controls__input'])[27]")).click()
    sleep(1.5)
    driver.find_element(
        By.XPATH, ("(//div[@class='v-input--selection-controls__input'])[28]")).click()
    sleep(1.5)
    driver.find_element(
        By.XPATH, ("(//div[@class='v-input--selection-controls__input'])[29]")).click()
    sleep(1.5)
    driver.find_element(
        By.XPATH, ("(//div[@class='v-input--selection-controls__input'])[30]")).click()
    sleep(1.5)
    driver.find_element(
        By.XPATH, ("(//div[@class='v-input--selection-controls__input'])[31]")).click()
    sleep(1.5)


# Demande le choix de l'étage à l'utilisateur
def choix_etage():
    global etage
    etage = input(
        "A quel étage cherchez vous une salle ? \n RDC : 0 \n 2 ème : 2 \n 3 ème : 3 \n")


# Sélectionne les salles de l'étage sélecitonnées par l'utilisateur
def select_etage():
    if etage == '0':
        rdc()
    if etage == '2':
        deuxieme()
    if etage == '3':
        troisieme()
    driver.back()


### SCRAPING ###
# Récupère les évènements d'aujourd'hui
def get_today_events():
    global today_events
    today_events = driver.find_element(
        By.CLASS_NAME, 'v-calendar-daily__day.v-present').get_attribute('outerHTML')


# Sépare les évènements dans une liste puis str(liste)
def get_sep_events():
    global sep_events
    sep_events = []
    sep_events = re.findall(
        'div class="v-event-timed onsecondary--text"(.*?)</div></div>', today_events)
    sep_events = str(sep_events)


# Récupère les salles occupées aujourd'hui
def get_rooms():
    global rooms
    rooms = re.findall('<br>(?=A )(.*?)\'', sep_events)


# Récupère les pixels qui déterminent l'heure de début
def get_top_pixels():
    global top_pixels
    top_pixels = re.findall('top: (.*?)px;', sep_events)
    top_pixels = [int(p) for p in top_pixels]


# Récupère les pixels qui déterminent la durée
def get_height_pixels():
    global height_pixels
    height_pixels = re.findall('height: (.*?)px;', sep_events)
    height_pixels = [int(p) for p in height_pixels]


# Conversion pixels qui déterminent le début en HH:MM
def get_occupation_start():
    global occupation_start_numbers
    global occupation_start_in_hours
    occupation_start_numbers = [
        (7 + ((p / 20) * 0.5)) * 60 for p in top_pixels]
    df1 = pd.DataFrame({'start': occupation_start_numbers})
    df1 = pd.to_datetime(df1.start, unit='m').dt.strftime('%H:%M')
    occupation_start_in_hours = df1.values.tolist()

# Conversion pixels qui déterminent la durée en HH:MM
def get_occupation_duration():
    global occupation_duration
    global occupation_duration_in_hours
    occupation_duration = [(((p / 20) * 0.5) * 60) for p in height_pixels]
    df = pd.DataFrame({'duration': occupation_duration})
    df = pd.to_datetime(df.duration, unit='m').dt.strftime('%H:%M')
    occupation_duration_in_hours = df.values.tolist()


# Déterminent l'heure de fin en HH:MM
def get_occupation_end():
    global occupation_end_in_hours
    occupation_end_in_minutes = [
        x + y for x, y in zip(occupation_start_numbers, occupation_duration)]
    df2 = pd.DataFrame({'end': occupation_end_in_minutes})
    df2 = pd.to_datetime(df2.end, unit='m').dt.strftime('%H:%M')
    occupation_end_in_hours = df2.values.tolist()


### HEURES SALLES ###
# Détermine l'heure actuelle
def get_now_time():
    global now_time
    now = datetime.now()
    now_time = now.strftime("%H:%M")
 
# Demande à quelle heure l'utilisateur souhaite entrer dans la salle
def choose_time():
    global now_time
    now_time = input('Quelle heure ? Répondre sous la forme HH:MM \n')


# L'utilisateur peut choisir entre utiliser l'heure actuelle ou une heure qu'il a choisi
def get_time():
    choice = int(
        input('Quand veux-tu utiliser la salle? \n Maintenant (0) \n Plus tard (1) \n'))
    if choice == 0:
        get_now_time()
        console.print('Heure actuelle :', now_time)
    if choice == 1:
        choose_time()
        console.print('Heure choisie :', now_time)


# Intégration de toutes les informations dans un dictionnaire
def get_dict():
    global dict_content
    dict_content = defaultdict(list)
    start_end = [list(t) for t in zip(
        occupation_start_in_hours, occupation_end_in_hours)]
    for x, y in zip(rooms, start_end):
        dict_content[x].append(y)
    dict_content = {key: sorted(dict_content[key])
                    for key in sorted(dict_content)}


# Référence des salles existantes pour chaque étage
def liste_salles():
    global liste_totale
    global liste_salles_0
    global liste_salles_2
    global liste_salles_3
    liste_salles_0 = ['A 015', 'A 016', 'A 017', 'A 018', 'A 019', 'A 020',
                      'A 021', 'A 022', 'A 023', 'A 024', 'A 025', 'A 026', 'A 027']
    liste_salles_2 = ['A 210', 'A 231', 'A 233']
    liste_salles_3 = ['A 310', 'A 311', 'A 312', 'A 313', 'A 314', 'A 326',
                      'A 327', 'A 328', 'A 329', 'A 330', 'A 331', 'A 333', 'A 336']
    liste_totale = [liste_salles_0, liste_salles_2, liste_salles_3]


# Convertit l'étage sélectionné par l'utilisateur en position dans la liste_totale
def etage_liste():
    global etage
    if etage == '3':
        etage = int(etage)-1
    if etage == '2':
        etage = int(etage)-1
    if etage == '0':
        etage = 0


### TRAITEMENT DES DONNEES ###
# Détermine les salles qui ne sont pas du tout utilisées aujourd'hui
def free_room():
    global gen
    global salle_libre
    h = 0
    salle_libre = []
    gen = (x for x in liste_totale[etage] if x not in dict_content.keys())
    for x in gen:
        salle_libre += [x]
    for x in salle_libre:
        console.print(
            'La salle', salle_libre[h], 'est libre toute la journée', style="green")
        h += 1


# Séparation des salles utilisées 1, 2, 3 ou 4 fois dans une même journée
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


# Salles utilisées une fois : comparaison de l'heure choisie et des heures de début et de fin des crénaux
def check_single_event():
    z = 0
    for i in single_event:
        elem = dict_content[str(i)]
        if (elem[0][0] < now_time < elem[0][1]):
            console.print(
                "La salle", single_event[z], "est occupée jusqu'à :", elem[0][1], style='red')
            z += 1
        if (now_time < elem[0][0]):
            console.print(
                "La salle", single_event[z], "est libre jusqu'à :", elem[0][0], style='green')
            z += 1
        if (now_time > elem[0][1]):
            console.print(
                "La salle", single_event[z], "est libre pour le reste de la journée", style='green')
            z += 1


# Salles utilisées deux fois : comparaison de l'heure choisie et des heures de début et de fin des crénaux
def check_double_event():
    j = 0
    for element in double_event:
        elem_double = dict_content[str(element)]
        if now_time < elem_double[0][0]:
            console.print(
                "La salle", double_event[j], "est libre jusqu'à", elem_double[0][0], style='green')
        if (elem_double[0][0] < now_time < elem_double[0][1]):
            console.print(
                "La salle", double_event[j], "est occupée jusqu'à :", elem_double[0][1], style='red')
            j += 1
        if (elem_double[0][1] < now_time < elem_double[1][0]):
            console.print(
                "La salle", double_event[j], "est libre jusqu'à", elem_double[1][0], style='green')
            j += 1
        if (elem_double[1][0] < now_time < elem_double[1][1]):
            console.print(
                "La salle", double_event[j], "est occupée jusqu'à :", elem_double[1][1], style='red')
            j += 1
        if elem_double[1][1] < now_time:
            console.print(
                "La salle", double_event[j], "est libre pour le reste de la journée", style='green')
            j += 1


# Salles utilisées trois fois : comparaison de l'heure choisie et des heures de début et de fin des crénaux
def check_triple_event():
    a = 0
    for element in triple_event:
        elem_triple = dict_content[str(element)]
        if now_time < elem_triple[0][0]:
            console.print(
                "La salle", double_event[a], "est libre jusqu'à :", elem_triple[0][0], style='green')
        if elem_triple[0][0] < now_time < elem_triple[0][1]:
            console.print(
                "La salle", triple_event[a], "est occupée jusqu'à :", elem_triple[0][1], style='red')
            a += 1
        if elem_triple[0][1] < now_time < elem_triple[1][0]:
            console.print(
                "La salle", triple_event[a], "est libre jusqu'à :", elem_triple[1][0], style='green')
            a += 1
        if elem_triple[1][0] < now_time < elem_triple[1][1]:
            console.print(
                "La salle", triple_event[a], "est occupée jusqu'à :", elem_triple[1][1], style='red')
            a += 1
        if elem_triple[1][1] < now_time < elem_triple[2][0]:
            console.print(
                "La salle", triple_event[a], "est libre jusqu'à :", elem_triple[2][0], style='green')
            a += 1
        if elem_triple[2][0] < now_time < elem_triple[2][1]:
            console.print(
                "La salle", triple_event[a], "est occupée jusqu'à :", elem_triple[2][1], style='red')
            a += 1
        if elem_triple[2][1] < now_time:
            console.print(
                "La salle", triple_event[a], "est libre pour le reste de la journée", style='green')
            a += 1


# Salles utilisées quatre fois : comparaison de l'heure choisie et des heures de début et de fin des crénaux
def check_quad_event():
    q = 0
    for element in quad_event:
        elem_quad = dict_content[str(element)]
        if now_time < elem_quad[0][0]:
            console.print(
                "La salle", quad_event[q], "est libre jusqu'à :", elem_quad[0][0], style='green')
            q += 1
        if elem_quad[0][0] < now_time < elem_quad[0][1]:
            console.print(
                "La salle", quad_event[q], "est occupée jusqu'à :", elem_quad[0][1], style='red')
            q += 1
        if elem_quad[0][1] < now_time < elem_quad[1][0]:
            console.print(
                "La salle", quad_event[q], "est libre jusqu'à :", elem_quad[1][0], style='green')
            q += 1
        if elem_quad[1][0] < now_time < elem_quad[1][1]:
            console.print(
                "La salle", quad_event[q], "est occupée jusqu'à :", elem_quad[1][1], style='red')
            q += 1
        if elem_quad[1][1] < now_time < elem_quad[2][0]:
            console.print(
                "La salle", quad_event[q], "est libre jusqu'à :", elem_quad[2][0], style='green')
            q += 1
        if elem_quad[2][0] < now_time < elem_quad[2][1]:
            console.print(
                "La salle", quad_event[q], "est occupée jusqu'à :", elem_quad[2][1], style='red')
            q += 1
        if elem_quad[2][1] < now_time < elem_quad[3][0]:
            console.print(
                "La salle", quad_event[q], "est libre jusqu'à :", elem_quad[3][0], style='green')
            q += 1
        if elem_quad[3][0] < now_time < elem_quad[3][1]:
            console.print(
                "La salle", quad_event[q], "est occupée jusqu'à :", elem_quad[3][1], style='red')
            q += 1
        if elem_quad[3][1] < now_time:
            console.print(
                "La salle", quad_event[q], "est libre pour le reste de la journée", style='green')
            q += 1


# Retourne dans l'onglet personnaliser et déselectionne toutes les sélections
def customize2():
    driver.find_element(
        By.CSS_SELECTOR, '#app-toolbar > div > button.v-app-bar__nav-icon.hidden-md-and-up.v-btn.v-btn--flat.v-btn--icon.v-btn--round.theme--dark.v-size--default > span > i').click()
    sleep(5.0)
    # ici en fonction  de la position de l'élément
    driver.find_element(
        By.CSS_SELECTOR, '#unistra-schedule > div.v-application--wrap > div > nav > div.v-navigation-drawer__content > div > a:nth-child(1)').click()
    sleep(5.0)
    deselect()


# Ouvre la page de personnalisation et l'utilisateur peut alors choisir son emploi du temps habituel
def fin():
    driver.close()
    console.print("Merci d'avoir utilisé notre programme, afin de retrouver votre emploi du temps initial, veuillez le personnalier depuis la page qui va s'ouvrir dans quelques instants...", style='purple')
    for step in track(range(10), description="Chargement ..."):
        sleep(1)
        step
    webbrowser.open("https://monemploidutemps.unistra.fr/config")
