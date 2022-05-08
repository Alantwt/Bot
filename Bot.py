from selenium.webdriver.remote.webdriver import WebDriver
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common import keys
import pickle
from selenium.webdriver.remote.webdriver import WebDriver

BrowserDriver = webdriver
SessionFile = "./sources/session"
task = None

def bot_init_():
    global BrowserDriver
    BrowserDriver = conect_whatsapp_session()
    CanvasElement = True
    while CanvasElement:
        print(CanvasElement)
        CanvasElement = validateQR()
        if CanvasElement == False:
            print("sin canvas")
    ContactFind = searchCONTACTS()
    if ContactFind == True:
        while True:
            readChat()
            chat()
            print(f"task: {task}")


def validateQR():
    global BrowserDriver
    try:
        target = BrowserDriver.find_element(By.TAG_NAME,"canvas")
        time.sleep(10)
    except:
        return False
    return True


def searchCONTACTS():
    global BrowserDriver
    time.sleep(10)
    print("comienza")
    TargetsContacts = BrowserDriver.find_elements(By.TAG_NAME,"span")
    print(type(TargetsContacts))
    for contact in TargetsContacts:
        print(contact.text)
        if contact.text == ":vv":
            contact.click()
            return True
        else:
            print("no encontrado")


def chat():
    global BrowserDriver
    print("sentro")
    chatbox = BrowserDriver.find_element(By.XPATH,'//*[@id="main"]/footer/div[1]/div/span[2]/div/div[2]/div[1]/div/div[2]')
    chatbox.send_keys("h")
    chatbox.send_keys(keys.Keys.ENTER)


def readChat():
    global task
    b=False
    while b == False:
        chats = BrowserDriver.find_elements(By.CLASS_NAME,'_1Gy50')
        if chats[len(chats)-1].text[0:5] == "!task":
            task = chats[len(chats)-1].text
            break
               

def conect_whatsapp_session():
    file = open(SessionFile,mode="rb")
    WhatsappSession = pickle.load(file)
    session_id, executor_url = WhatsappSession["id"],WhatsappSession["url"]

    def new_command_execute(self, command, params=None):
        print(f"command: {command}")
        if command == "newSession":
            return {'success': 0, 'value': None, 'sessionId': session_id}
        else:
            return org_command_execute(self, command, params)
                
    org_command_execute = WebDriver.execute

    WebDriver.execute = new_command_execute

    new_driver = webdriver.Remote(command_executor=executor_url, desired_capabilities={})
    new_driver.session_id = session_id

    WebDriver.execute = org_command_execute

    return new_driver

if __name__ == "__main__":
    bot_init_()

