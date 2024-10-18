import pandas as pd
from sklearn.preprocessing import StandardScaler
import logging

logging.basicConfig(level=logging.INFO,
                    format='%(asctime)s - %(levelname)s - %(message)s',
                    handlers=[
                        logging.FileHandler('log.txt', encoding='utf-8'),
                        logging.StreamHandler()
                    ])

file_path = 'data_student_25278.csv'
logging.info("Rozpoczęcie odczytu danych z pliku.")
df = pd.read_csv(file_path)
logging.info("Dane zostały pomyślnie wczytane.")

original_row_count = len(df)
logging.info(f"Liczba wierszy przed czyszczeniem: {original_row_count}")

df_cleaned = df.dropna(thresh=len(df.columns) - 2).reset_index(drop=True)

cleaned_row_count = len(df_cleaned)
removed_row_count = original_row_count - cleaned_row_count
logging.info(f"Liczba usuniętych wierszy: {removed_row_count}")

changed_value_count = 0
for column in df_cleaned.select_dtypes(include=['float64', 'int64']).columns:
    median_value = df_cleaned[column].median()
    original_values = df_cleaned[column].isnull().sum()
    df_cleaned.loc[:, column] = df_cleaned[column].fillna(median_value)
    changed = original_values - df_cleaned[column].isnull().sum()
    changed_value_count += changed
    logging.info(f"W kolumnie '{column}' uzupełniono {changed} brakujących wartości.")

for column in df_cleaned.select_dtypes(include=['object']).columns:
    mode_value = df_cleaned[column].mode()[0]
    original_values = df_cleaned[column].isnull().sum()
    df_cleaned.loc[:, column] = df_cleaned[column].fillna(mode_value)
    changed = original_values - df_cleaned[column].isnull().sum()
    changed_value_count += changed
    logging.info(f"W kolumnie '{column}' uzupełniono {changed} brakujących wartości.")

def time_to_minutes(time_str):
    if pd.isna(time_str) or time_str == '':
        return None
    hours, minutes = map(int, time_str.split(':'))
    return hours * 60 + minutes

time_columns = ['Czas Początkowy Podróży', 'Czas Końcowy Podróży']
for time_column in time_columns:
    if time_column in df_cleaned.columns:
        df_cleaned[time_column] = df_cleaned[time_column].apply(time_to_minutes)
        logging.info(f"Kolumna '{time_column}' została pomyślnie przetworzona na minuty.")

numeric_columns = df_cleaned.select_dtypes(include=['float64', 'int64']).columns
scaler = StandardScaler()
df_scaled = pd.DataFrame(scaler.fit_transform(df_cleaned[numeric_columns]), columns=numeric_columns)

df_final = pd.concat([df_scaled, df_cleaned[df_cleaned.select_dtypes(include=['object']).columns]], axis=1)

df_final.to_csv('cleaned_data_student_25278.csv', index=False)
logging.info("Dane zostały pomyślnie zapisane do pliku 'cleaned_data_student_25278.csv'.")

percentage_changed = (changed_value_count / (original_row_count * df.shape[1])) * 100
percentage_removed = (removed_row_count / original_row_count) * 100

report = f"Raport z przetwarzania danych:\n" \
         f"Procent danych, które zostały zmienione: {percentage_changed:.2f}%\n" \
         f"Procent danych, które zostały usunięte: {percentage_removed:.2f}%\n"

with open('report.txt', 'w', encoding='utf-8') as f:
    f.write(report)
logging.info("Raport został zapisany do pliku 'report.txt'.")

print(report)
