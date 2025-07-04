import gspread
import pandas as pd
from oauth2client.service_account import ServiceAccountCredentials
from scripts.config import SERVICE_ACCOUNT_FILE

def load_records(sheet_name, worksheet_name):
    scope = ['https://spreadsheets.google.com/feeds', 'https://www.googleapis.com/auth/drive']
    creds = ServiceAccountCredentials.from_json_keyfile_name(SERVICE_ACCOUNT_FILE, scope)
    gc = gspread.authorize(creds)
    sheet = gc.open(sheet_name).worksheet(worksheet_name)
    print("Google Sheets Loaded.")
    return sheet, sheet.get_all_records()

def append_articles(sheet, df):
    if not df.empty:
        sheet.append_rows(df.values.tolist(), value_input_option = 'USER_ENTERED')
        print(f"{len(df)} new articles appended.")
