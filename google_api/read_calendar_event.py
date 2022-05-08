import datetime as dt
from google_api import Autenticator
#Instancia de la Clase Autenticator
AUTENTICATOR_INSTANCE = Autenticator()

class ReadCalendarEvent():
    def __init__(self):
        global AUTENTICATOR_INSTANCE
        CalendarService = AUTENTICATOR_INSTANCE.get_service()
        now = dt.datetime.utcnow().isoformat() + 'Z'  # 'Z' indicates UTC time
        EndDate = dt.datetime.fromisoformat("2022-05-10 20:30:00").isoformat() + "Z"
        print(now+" "+EndDate)
        print('Getting the upcoming 10 events')
        events_result = CalendarService.events().list(calendarId='primary', timeMin=now,
                                              maxResults=10, singleEvents=True,
                                              orderBy='startTime',timeMax=EndDate).execute()
        events = events_result.get('items', [])

        if not events:
            print('No upcoming events found.')
            return

        # Prints the start and name of the next 10 events
        for event in events:
            start = event['start'].get('dateTime', event['start'].get('date'))
            print(start, event['summary'], event["description"],event["start"])

if __name__ == "__main__":
    ReadCalendarEvent()