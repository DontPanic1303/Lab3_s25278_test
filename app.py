from flask import Flask, request, jsonify
import joblib
import pandas as pd

model = joblib.load("model.pkl")
scaler = joblib.load("scaler.pkl")
transformer = joblib.load("transformer.pkl")

app = Flask(__name__)


@app.route('/predict', methods=['POST'])
def predict():
    try:
        data = request.get_json()

        df = pd.DataFrame([data])

        df_transformed = transformer.transform(df)
        df_scaled = scaler.transform(df_transformed)

        prediction = model.predict(df_scaled)

        return jsonify({'prediction': prediction[0]})

    except Exception as e:
        return jsonify({'error': str(e)}), 400


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
