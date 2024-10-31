Marcin Milewski 
s25278
Lab4

Aplikacja służy do przewidywania wyników na podstawie danych o dystansie do uczelni, wykorzystując wytrenowany model RandomForestRegressor. API zostało opakowane w kontener Docker i opublikowane na Docker Hub.

Zawartość Repozytorium
- app.py - skrypt uruchamiający API do przewidywania.
- train_model.py - skrypt do trenowania modelu.
- Dockerfile - plik budujący obraz Dockera dla aplikacji.
- GetData.py - plik słurzący do pobierania danych z chmury.
- requirements.txt - lista wymaganych pakietów.
- GetDataAndCleanIT.yml - workflow który wykorzystuje pliki GetData.py i train_model.py

Pliki postałe podczas działania programu
- model.pkl, scaler.pkl, transformer.pkl - zapisane pliki modelu, skalera oraz transformera kolumn. Wytworzone z działania train_model.py
- CollegeDistance.csv - dane z chmury postałe podczas działania GetData.py

Instrukcja obsługi

1. Jak sklonować repozytorum:
    
        git clone https://github.com/PJATK-ASI-2024/Lab-4_s25278.git


2. Jak pobrać dane i stworzyć model
    
        Postępować zgodnie z instrukcjami w pliku GetDataAndCleanIT.yml


3. Jak wytrenować model kiedy ma się dane
    
        Wstawić dane do forderu projektu
        python train_model.py


4. Uruchomienie serwera
    
        python app.py


5. Korzystanie z API

        curl -X POST -H "Content-Type: application/json" -d '{"rownames": 1, "gender": "male", "ethnicity": "other", "fcollege": "yes", "mcollege": "no", "home": "yes", "urban": "yes", "unemp": 0.1, "wage": 0.5, "distance": 20, "tuition": 1.2, "education": 12, "income": "high", "region": "other"}' http://localhost:5000/predict


Jak korzysrać z dockera

1. Pobranie obrazu z Docker Huba

        docker pull dontpanic13/pjatk_lab4:l4


2. Uruchomienie kontenera z obrazu Docker Hub

        docker run -p 5000:5000 dontpanic13/pjatk_lab4:l4

3. Korzystanie z API

        curl -X POST -H "Content-Type: application/json" -d '{"rownames": 1, "gender": "male", "ethnicity": "other", "fcollege": "yes", "mcollege": "no", "home": "yes", "urban": "yes", "unemp": 0.1, "wage": 0.5, "distance": 20, "tuition": 1.2, "education": 12, "income": "high", "region": "other"}' http://localhost:5000/predict

