# Diabetes Risk Prediction

This project aims to predict the risk of diabetes in individuals based on various health parameters. The model is built using machine learning techniques, and the web interface allows users to input their health data and get a prediction about their likelihood of developing diabetes.

## Project Files

The project includes several files for both backend and frontend implementation:

1. **app.py**  
   This is the main backend script. It uses the Flask framework to run the web application and handle HTTP requests. It also processes data passed from the frontend and invokes the machine learning model to generate predictions.

2. **diabetes.csv**  
   This file contains the dataset used to train the machine learning model. It includes various health parameters (such as age, blood pressure, BMI, etc.) and whether the individual has diabetes.

3. **diabetes.jpg**  
   An image used in the web interface, likely for visual branding or displaying the project logo.

4. **index.html**  
   The landing page of the web application. It includes a form where users can input their health parameters for the diabetes risk prediction.

5. **index.js**  
   This file contains the JavaScript functions that handle frontend logic, such as form validation, sending data to the server, and receiving the prediction result.

6. **main.py**  
   A Python script that defines the machine learning model. It preprocesses the data, trains the model, and evaluates its performance. The model is then used to make predictions based on user input.

7. **result.html**  
   A template file that displays the prediction result to the user. After submitting their data through the form, the user will be redirected to this page, which shows whether they are at risk of diabetes or not.

8. **styles.css**  
   This file contains the styles used to make the web interface visually appealing and user-friendly. It defines the layout, colors, and fonts used across the web application.

## How to Run

### 1. Clone the repository

First, clone the repository to your local machine:

```bash
git clone https://github.com/your-username/diabetes-risk-prediction.git
cd diabetes-risk-prediction
