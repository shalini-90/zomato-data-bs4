import csv
from curses import keyname
import json
import pandas as pd
import gspread
from oauth2client.service_account import ServiceAccountCredentials
from pprint import pprint as pp
from google.oauth2 import service_account
from googleapiclient.discovery import build
# import googleapiclient 
from google.oauth2.credentials import Credentials

scope = ["https://spreadsheets.google.com/feeds",'https://www.googleapis.com/auth/spreadsheets',
	    "https://www.googleapis.com/auth/drive.file","https://www.googleapis.com/auth/drive"]

creds = ServiceAccountCredentials.from_json_keyfile_name("/home/zec/Desktop/zomato/env/zo66.json",scope)
client = gspread.authorize(creds)
sheet = client.open("zomatoo_project").sheet1   

DATA_SPREADSHEET_ID='1N1R0CUwqDxD8nBvQtS4XwhulJgNUp1zWaNeg6CLSMls'

def append_googlesheet(value1):
    values = [value1]
    service = build('sheets','v4',credentials=creds)
    response = service.spreadsheets().values().append(spreadsheetId='1N1R0CUwqDxD8nBvQtS4XwhulJgNUp1zWaNeg6CLSMls', valueInputOption='USER_ENTERED', range="Sheet1!A2:E2", body={"values": values}).execute() 




    # data = sheet.get_all_records()
# print(data)
# with open('/home/zec/Desktop/zomato/swiggy_project/swiggyproject-366710-31a187b4ffc7.json', newline='') as f:
#     reader = csv.reader(f)
#     values = list(reader)
#     service = build('sheets','v4',credentials=creds)
# response = service.spreadsheets().values().append(spreadsheetId='1PeFBGfRhDQ3_BfJQG8KjvyKTKZWlONdnZHuHY2cFacY', valueInputOption='USER_ENTERED', range="Sheet1", body={"values": values}).execute()