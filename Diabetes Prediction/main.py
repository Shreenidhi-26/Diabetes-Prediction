import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score

def load_data(file_path):
    df = pd.read_csv(file_path)
    return df

def clean_data(df):
    df_cleaned = df.dropna()
    return df_cleaned

def encode_categorical_variables(df):
    return df

def train_knn_model(X_train, y_train, n_neighbors=5):
    knn_model = KNeighborsClassifier(n_neighbors=n_neighbors)
    knn_model.fit(X_train, y_train)
    return knn_model

def split_data(df, target_column, test_size=0.2, random_state=42):
    X = df.drop(columns=[target_column])
    y = df[target_column]
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=test_size, random_state=random_state)
    return X_train, X_test, y_train, y_test

def preprocess_input(X):
    # You may need to apply the same preprocessing steps as in your main() function
    # For example, scaling the input data if you used StandardScaler in your main() function
    # scaler = StandardScaler()
    # scaled_data = scaler.fit_transform(X)
    return X

def calculate_predictions(X, knn_model):
    # Preprocess input data
    input_data = preprocess_input(X)

    # Make predictions using the model
    predictions = knn_model.predict(input_data)

    return predictions

def main():
    df = load_data("diabetes.csv") 
    df_cleaned = clean_data(df)
    df_encoded = encode_categorical_variables(df_cleaned)
    X_train, X_test, y_train, y_test = split_data(df_encoded, 'Outcome')
    knn_model = train_knn_model(X_train, y_train)
    y_pred = knn_model.predict(X_test)
    accuracy = accuracy_score(y_test, y_pred)
    precision = precision_score(y_test, y_pred)
    recall = recall_score(y_test, y_pred)
    f1 = f1_score(y_test, y_pred)
    print("Model Performance Metrics:")
    print("Accuracy:", accuracy)
    print("Precision:", precision)
    print("Recall:", recall)
    print("F1-score:", f1)
    return knn_model

if __name__ == "__main__":
    knn_model = main()

    # Load your data from CSV file
    file_path = "diabetes.csv"  
    df = load_data(file_path)

    # Make predictions for your data
    predictions = calculate_predictions(df.values, knn_model)

    # Print the predictions
    print("Predictions:", predictions)
