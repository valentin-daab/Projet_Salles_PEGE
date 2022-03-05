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
import getpass
import time
import re
# Import relatifs
import sub.fonctions as f


global liste_totale
global liste_salles_0
global liste_salles_2
global liste_salles_3
liste_salles_0 = ['A 015','A 016','A 017','A 018','A 019','A 020','A 021','A 022','A 023','A 024','A 025','A 026','A 027']
liste_salles_2 = ['A 210','A 231', 'A 233']
liste_salles_3 = ['A 310','A 311','A 312','A 313','A 314','A 326','A 327','A 328','A 329','A 330','A 331','A 333','A 336']
liste_totale = [liste_salles_0, liste_salles_2, liste_salles_3]


def run():
    f.get_paths()
    f.web()
    f.connect_user()
    time.sleep(5.0)
    f.customize()
    f.choix_etage()
    time.sleep(2.0)
    f.get_today_events()
    f.get_sep_events()
    f.get_rooms()
    f.get_top_pixels()
    f.get_height_pixels()
    f.get_occupation_start()
    f.get_occupation_duration()
    f.get_occupation_end()
    f.get_time()
    f.get_dict()
    f.etage_liste()
    f.liste_salles()
    f.free_room()
    f.sep_event_type()
    f.check_single_event()
    f.check_double_event()
    f.check_triple_event()
    f.check_quad_event()
    f.customize2()
    f.fin()


if __name__ == '__main__':
    run()
