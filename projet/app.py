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
# import relatifs
from modif_edt.fonctions import get_paths, init_webdriver


def run():
    global driver
    get_paths()
    init_webdriver()

if __name__ == '__main__':
    run()



