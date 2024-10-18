import gspread
import pandas as pd
from oauth2client.service_account import ServiceAccountCredentials
import logging
import numpy as np

logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler('log.txt', encoding='utf-8'),
        logging.StreamHandler()
    ]
)

logging.info("Rozpoczęcie procesu aktualizacji danych w Google Sheets.")

scope = ['https://spreadsheets.google.com/feeds', 'https://www.googleapis.com/auth/drive']
try:
    creds = ServiceAccountCredentials.from_json_keyfile_name('creds.json', scope)
    client = gspread.authorize(creds)
    logging.info("Zostałeś pomyślnie uwierzytelniony w Google Sheets.")
except Exception as e:
    logging.error(f"Błąd uwierzytelniania: {e}")
    raise

csv_file_path = 'Lab2---Obr-bka-danych/data_student_25278.csv'
try:
    df = pd.read_csv(csv_file_path)
    logging.info(f"Dane zostały pomyślnie wczytane z pliku CSV: {csv_file_path}.")
except Exception as e:
    logging.error(f"Błąd podczas wczytywania pliku CSV: {e}")
    raise

logging.info("Zastąpienie NaN na -1")
df.replace([np.inf, -np.inf], np.nan, inplace=True)
df.fillna(-1, inplace=True)

spreadsheet_id = '1cafA7Adj9U97x9-uzY2DyHWOJnqGKv0QZNPyl5AfMIg'
try:
    sheet = client.open_by_key(spreadsheet_id).sheet1
    logging.info("Arkusz został pomyślnie otwarty.")
except Exception as e:
    logging.error(f"Błąd podczas otwierania arkusza: {e}")
    raise

try:
    sheet.clear()
    logging.info("Zawartość arkusza została pomyślnie usunięta.")
except Exception as e:
    logging.error(f"Błąd podczas czyszczenia arkusza: {e}")
    raise

try:
    sheet.update([df.columns.values.tolist()] + df.values.tolist())
    logging.info("Arkusz został pomyślnie zaktualizowany danymi z pliku CSV.")
except Exception as e:
    logging.error(f"Błąd podczas aktualizacji arkusza: {e}")
    raise
