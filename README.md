Jest to repozytorium gdzie tertowałem działanie Workflows więc jakoś commitów jest bardzo niska. Bardziej jakościowe commity wysyłałem na repozytorium organizacji.

README - Projekt Przetwarzania Danych
Ten projekt automatyzuje generowanie danych, przesyłanie ich do Google Sheets, pobieranie, czyszczenie, standaryzację oraz generowanie raportu. Cały proces jest realizowany za pomocą GitHub Actions i Pythonowych skryptów.

Projekt generuje dane, przesyła je do Google Sheets, a następnie pobiera, czyści i standaryzuje dane, tworząc raport. Dane są przetwarzane i analizowane w pełni automatycznie, korzystając z GitHub Actions.

Workflows:

    1. GenerateData.yml
    Workflow generuje dane, przesyła je do Google Sheets i usuwa wrażliwe dane po zakończeniu procesu.

    Kluczowe kroki:
    1. Instalacja zależności.
    2. Klonowanie repozytorium. 
    3. Generowanie danych (generator_danych.py).
    4. Przesyłanie danych do Google Sheets (SendData.py).

    2. GetDataAndCleanIT.yml
    Workflow pobiera dane z Google Sheets, czyści je, zwraca w postaci pliku cleaned_data_student_s25278.csv 
    i tworzy raport z przetwarzania danych. 

       Kluczowe kroki:
      1. Instalacja zależności.
      2. Pobranie danych z Google Sheets (GetData.py).
      3. Czyszczenie i standaryzacja danych (CleanData.py).
      4. Wyświetlenie raportu (report.txt).
   

Skrypty Python:

    1. SendData.py
    Wysyła plik data_student_s25278.csv do google sheets
    Opis działania:
        1. Uwierzytelnianie do Google Sheets
        2. Odczyt pliku CSV
        3. Zastąpienie wartości NaN na -1
        4. Otwieranie arkusza Google Sheets
        5. Aktualizacja arkusza danymi z CSV

    2. GetData.py
    Pobiera dane z google sheets i zapisuje je w data_student_s25278.csv 
    Opis działania:
        1. Uwierzytelnianie do Google Sheets
        2. Otwieranie arkusza Google Sheets
        3. Pobieranie danych z Google Sheets
        4. Zapisywanie danych do pliku CSV

    3. CleanData.py
    Czyszczenie danych z pliku data_student_s25278.csv i zapisanie ich w cleaned_data_student_s25278.csv
    Opis działania:
        1. Wczytywanie danych z pliku CSV
        2. Zastąpienie wartości -1 na NaN
        3. Sprawdzanie i naprawianie formatów czasu
        4. Usunięcie wierszy z byd duża ilością brakujących danych
        5. Zastąpienie dla kolumn liczbowych wartości (NaN) na medianę, a dla kolumn tekstowych na najczęściej występującą wartością (modą) 
        6. Standaryzacja danych liczbowych
        7. Zapisywanie przetworzonych danych (cleaned_data_student_s25278.csv)
        8. Generowanie raportu (report.txt)

GitHub Secrets:

    GOOGLE_SHEETS_CREDENTIALS: Klucz API do Google Sheets.
    GH_TOKEN: Token dostępu do GitHub (dla repozytoriów prywatnych).


Uruchamianie Workflows:
    
    1. Generowanie danych i przesyłanie do Google Sheets
    Workflow GenerateData.yml można uruchomić ręcznie w zakładce "Actions" w GitHub.

    2. Pobieranie i czyszczenie danych
    Workflow GetDataAndCleanIT.yml uruchamia się ręcznie lub przy pushu do gałęzi main.

Pliki:

    data_student_25278.csv: Wygenerowane dane studentów (surowe).
    cleaned_data_student_25278.csv: Oczyszczone i ustandaryzowane dane.
    report.txt: Raport z przetwarzania danych.
    log.txt: logi dokumentujące przebieg procesu.
