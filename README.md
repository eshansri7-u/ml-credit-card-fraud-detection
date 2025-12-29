# ml-credit-card-fraud-detection
This project is a machine learning fraud detection system built using the PaySim mobile money transaction dataset. It includes data preprocessing, model training using a scikit-learn pipeline, model persistence with joblib, and deployment through a FastAPI backend. A Streamlit frontend is used to provide an interactive interface where users can input transaction details and receive real-time fraud probability predictions.

Project Overview

Financial fraud detection is a classic imbalanced classification problem where the goal is to identify fraudulent transactions while minimizing false positives.

This project:

-Trains a Random Forest classifier on transaction data

-Uses a sklearn Pipeline 

-Saves the trained model for reuse

-Exposes predictions through a FastAPI REST API

How to Run the Project

Follow these steps to run the fraud detection system locally.

1. Clone the repository
git clone https://github.com/your-username/fraud-detection-system.git
cd fraud-detection-system

2. Install dependencies

All required packages are listed in requirements.txt.

pip install -r requirements.txt

3. Start the FastAPI backend

Run the API server using uvicorn:
cd backend
uvicorn main:app --reload

The API will be available at:

http://127.0.0.1:8000

4. Start the Streamlit frontend

cd frontend 
streamlit run app.py


The Streamlit app will open in your browser and allow you to:

Enter transaction details

Submit them to the FastAPI backend

View real-time fraud probability predictions








