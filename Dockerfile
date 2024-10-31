FROM python:3.8-slim

WORKDIR /app

COPY app.py model.pkl scaler.pkl transformer.pkl requirements.txt ./

RUN pip install --no-cache-dir -r requirements.txt
RUN pip install --upgrade scikit-learn numpy

EXPOSE 5000

CMD ["python", "app.py"]