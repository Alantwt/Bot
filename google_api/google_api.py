#AUTENTIFICAR
from __future__ import print_function
from calendar import calendar

import datetime
import os.path

from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError

#CREAR EVENTO
import datetime as dt
import time

#Direccion donde se va a acceder a la api 
SCOPES = ['https://www.googleapis.com/auth/calendar']
#ruta de donde esta el archivo con el id de la api para poder acceder a ella 
CREDENTIAL_FILE = "credentials.json"
TOKEN = "token.json"


#Clase para autentificarte en la api de google calendar
class Autenticator():
    def __init__(self):
        global CREDENTIAL_FILE
        self.creds = None
        # The file token.json stores the user's access and refresh tokens, and is
        # created automatically when the authorization flow completes for the first
        # time.
        if os.path.exists(TOKEN):
            self.creds = Credentials.from_authorized_user_file(TOKEN, SCOPES)
        if not self.creds or not self.creds.valid:
            if self.creds and self.creds.expired and self.creds.refresh_token:
                self.creds.refresh(Request())
            else:
                flow = InstalledAppFlow.from_client_secrets_file(
                    CREDENTIAL_FILE, SCOPES)
                self.creds = flow.run_local_server(port=0)
            # Save the credentials for the next run
            with open(TOKEN, 'w') as token:
                token.write(self.creds.to_json())
        try:
            self.service = build('calendar', 'v3', credentials=self.creds)

            # # Call the Calendar API
            # now = datetime.datetime.utcnow().isoformat() + 'Z'  # 'Z' indicates UTC time
            # print('Getting the upcoming 10 events')
            # events_result = self.service.events().list(calendarId='primary', timeMin=now,
            #                                     maxResults=10, singleEvents=True,
            #                                     orderBy='startTime').execute()
            # events = events_result.get('items', [])

            # if not events:
            #     print('No upcoming events found.')
            #     return

            # # Prints the start and name of the next 10 events
            # for event in events:
            #     start = event['start'].get('dateTime', event['start'].get('date'))
            #     print(start, event['summary'])

        except HttpError as error:
            print('An error occurred: %s' % error)

    def get_service(self):
        print("servicio")
        print(self.service)
        return self.service    

Autenticator()