import logging

import apiclient
import httplib2
from google.oauth2.gdch_credentials import ServiceAccountCredentials

logger = logging.getLogger(__name__)
class Binance:
    def __init__(self, api_key, username, password, api_secret, pass_phrase):
        self.user = username
        self.password = password
        self.api_key = api_key
        self.api_secret = api_secret
        self.pass_phrase = pass_phrase


def create(): return


def trade(): return


def order(): return


def run(): return


def update(): return


#CREDENTIALS_FILE = 'key_SpreadSheetPythonAPI.json'  # имя файла с закрытым ключом
#CREDENTIALS_FILE = 'key_ServerAUTH.json'  # имя файла с закрытым ключом
CREDENTIALS_FILE = 'key_ServAccKey.json'  # имя файла с закрытым ключом
#CREDENTIALS_FILE = 'key_webAPP_clientID.json'  # имя файла с закрытым ключом
#CREDENTIALS_FILE = 'key_desktop_clientID.json'  # имя файла с закрытым ключом

with open('service_email', 'r') as f:
    service_mail = f.read()[:-1]
# Читаем ключи из файла
credentials = ServiceAccountCredentials.from_json_keyfile_name(CREDENTIALS_FILE, ['https://www.googleapis.com/auth/spreadsheets',
                                                                                  'https://www.googleapis.com/auth/drive'])
httpAuth = credentials.authorize(httplib2.Http()) # Авторизуемся в системе
service = apiclient.discovery.build('sheets', 'v4', http = httpAuth) # Выбираем работу с таблицами и 4 версию API

spreadsheet_Id = "1W5Mm04gZyi7UbvZhq6ojZHBRwi93_hSKI5VAlfb1fRw"

driveService = apiclient.discovery.build('drive', 'v3', http = httpAuth)

shareRes = driveService.permissions().create(
    fileId = spreadsheet_Id,
    body = {'type': 'anyone', 'role': 'writer', 'emailAddress': service_mail},  # доступ на чтение кому угодно
    fields = 'id'
).execute()

result = service.spreadsheets().batchUpdate(spreadsheetId = spreadsheet_Id).execute()
print(result)