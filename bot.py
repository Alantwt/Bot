
from selenium import webdriver
import os
import time

class WhatsAppBot():
    def __init__(self):
        self.driver = webdriver.Edge(executable_path='./BrowserDriver/msedgedriver')
        self.wbot()
    
    def validar_QR(self):
        try:
            element = self.driver.find_element_by_tag_name("canvas")
            return True
        except:
            return False


    def bot_init(self):
        self.driver.get("https://web.whatsapp.com/")
        time.sleep(5)
        espera = True
        while espera:
            espera = self.Validar_QR()
            print(espera)
            time.sleep(2)
            if espera == False:
                print(espera)
                break

    

WhatsAppBot()