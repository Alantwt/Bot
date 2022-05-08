import datetime as dt
import time
from google_api import Autenticator
#Instancia de la Clase Autenticator
AUTENTICATOR_INSTANCE = Autenticator()

class CreateCalendarEvent():
    global AUTENTICATOR_INSTANCE
    print("inicio")
    def __init__(self,EventTitle : str, EventDescription : str,InitDate : str, EndDate : str):
        InitDate = dt.datetime.fromisoformat("2022-05-27 14:30:00").isoformat()
        EndDate = dt.datetime.fromisoformat("2022-05-27 20:30:00").isoformat()
        print(InitDate,EndDate)
        #Obtengo el self.service de la clase Autentificator que me va a servir para interactuar con la api una vez me autentifique
        CalendarService = AUTENTICATOR_INSTANCE.get_service()
        print("servicio2")
        print(CalendarService)
        #Inserto un evento en el CalendarService
        DicEvent = {
            "summary": EventTitle,
            "description": EventDescription,
            "start" : {"dateTime": InitDate, "timeZone":"America/Panama"},
            "end" : {"dateTime": EndDate,"timeZone":"America/Panama"}, 
        }
        event = CalendarService.events().insert(calendarId = "primary",body = DicEvent).execute()
        print("event created")
        
CreateCalendarEvent("Tarea","cualquier cosa", dt.datetime.fromisoformat("2022-05-10 14:30:00").isoformat(),dt.datetime.fromisoformat("2022-05-10 20:30:00").isoformat())