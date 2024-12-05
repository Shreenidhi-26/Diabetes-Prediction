from flask import Flask, request
import pandas as pd
from main import train_knn_model

app = Flask(__name__)

@app.route('/', methods=['POST'])
def predict_diabetes():
    data = request.form.to_dict()
    glucose = float(data['glucose'])
    blood_pressure = float(data['bloodPressure'])
    bmi = float(data['bmi'])

    # Validate input: Ensure non-negativity
    if glucose < 0 or blood_pressure < 0 or bmi < 0:
        return "Error: Negative numbers are not allowed."

    input_data = [[glucose, blood_pressure, bmi]]

    prediction = knn_model.predict(input_data)
    return str(prediction[0])

if __name__ == '__main__':
    app.run(debug=True)
