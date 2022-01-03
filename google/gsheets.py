# access google sheets via sheets api
# from: https://www.makeuseof.com/tag/read-write-google-sheets-python/
########################################

import gspread
from oauth2client.service_account import ServiceAccountCredentials
import json


print('hello')

scopes = [
    'https://www.googleapis.com/auth/spreadsheets',
    'https://www.googleapis.com/auth/drive'
]
credentials = ServiceAccountCredentials.from_json_keyfile_name(
    "[JSON_key_name].json", scopes)  # access the json key you downloaded earlier
file = gspread.authorize(credentials)  # authenticate the JSON key with gspread
sheet = file.open("Python_MUO_Google_Sheet")  # open sheet
# replace sheet_name with the name that corresponds to yours, e.g, it can be sheet1
sheet = sheet.sheet_name
