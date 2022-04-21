
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common import keys

Bdriver = webdriver.Edge(executable_path="./BrowserDriver/msedgedriver")

def OpenUrl():
    Bdriver.get("https://web.whatsapp.com/")
    time.sleep(2)
    CanvasElement = True
    while CanvasElement:
        print(CanvasElement)
        CanvasElement = validateQR()
        if CanvasElement == False:
            print("sin canvas")
    ContactFind = searchCONTACTS()
    if ContactFind == True:    
        readChat()
        chat()


def validateQR():
    try:
        target = Bdriver.find_element(By.TAG_NAME,"canvas")
        time.sleep(10)
    except:
        return False
    return True

def searchCONTACTS():
    time.sleep(10)
    print("comienza")
    TargetsContacts = Bdriver.find_elements(By.TAG_NAME,"span")
    print(type(TargetsContacts))
    for contact in TargetsContacts:
        print(contact.text)
        if contact.text == "Anthonio":
            contact.click()
            return True
        else:
            print("no encontrado")

def chat():
    print("sentro")
    chatbox = Bdriver.find_element(By.XPATH,'//*[@id="main"]/footer/div[1]/div/span[2]/div/div[2]/div[1]/div/div[2]')
    chatbox.send_keys("ahora soy el bot")
    chatbox.send_keys(keys.Keys.ENTER)


def readChat():
    b=False
    while b == False:
        chats = Bdriver.find_elements(By.CLASS_NAME,'_1Gy50')
        if chats[len(chats)-1].text == "hola":
            break
                
OpenUrl()


