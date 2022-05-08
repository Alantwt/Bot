from selenium import webdriver
import pickle


driver = webdriver.Edge(executable_path='./BrowserDriver\msedgedriver.exe')
executor_url = driver.command_executor._url
session_id = driver.session_id
driver.get("https://web.whatsapp.com/")

print("Session ID 1: " + session_id)
print("Executor URL: " + executor_url)
file = open("./sources/session",mode="wb")
file.seek(0)
WhatsappSession = {"id":session_id,"url":executor_url}
pickle.dump(WhatsappSession,file)
file.close()
