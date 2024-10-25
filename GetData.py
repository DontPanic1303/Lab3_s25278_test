import json
import gspread
import pandas as pd
from oauth2client.service_account import ServiceAccountCredentials
import logging

logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler('log.txt', encoding='utf-8'),
        logging.StreamHandler()
    ]
)


logging.info("Rozpoczęcie procesu pobierania danych z Google Sheets.")

scope = ['https://spreadsheets.google.com/feeds', 'https://www.googleapis.com/auth/drive']
creds = ServiceAccountCredentials.from_json_keyfile_name('creds.json', scope)

try:
    client = gspread.authorize(creds)
    logging.info("Zostałeś pomyślnie uwierzytelniony w Google Sheets.")
except Exception as e:
    logging.error(f"Błąd uwierzytelniania: {e}")
    raise

sheet_id = '1cafA7Adj9U97x9-uzY2DyHWOJnqGKv0QZNPyl5AfMIg'
try:
    sheet = client.open_by_key(sheet_id).get_worksheet(1)
    logging.info("Arkusz został pomyślnie otwarty.")
except Exception as e:
    logging.error(f"Błąd podczas otwierania arkusza: {e}")
    raise

try:
    data = sheet.get_all_records()
    logging.info("Dane zostały pomyślnie pobrane z arkusza.")
except Exception as e:
    logging.error(f"Błąd podczas pobierania danych: {e}")
    raise

df = pd.DataFrame(data)
csv_filename = 'CollegeDistance.csv'
try:
    df.to_csv(csv_filename, index=False)
    logging.info(f'Dane zostały zapisane do pliku {csv_filename}.')
except Exception as e:
    logging.error(f"Błąd podczas zapisywania do pliku CSV: {e}")
    raise
