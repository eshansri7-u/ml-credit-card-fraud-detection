# Financial Fraud Detection System

## Project Overview

Financial fraud detection is a classic imbalanced classification problem where the goal is to identify fraudulent transactions while minimizing false positives.

This project offers an end-to-end solution that:
- **Trains a Random Forest classifier** on transaction data to detect anomalies.
- **Uses a scikit-learn Pipeline** for streamlined data processing and inference.
- **Saves the trained model** for efficient reuse and deployment.
- **Exposes predictions** through a **FastAPI REST API**.


## How to Run the Project
```bash
git clone [https://github.com/your-username/project.git](https://github.com/your-username/ml-credit-card-fraud-detection
.git)
cd project
```

## Install dependencies
```bash
pip install -r requirements.txt
```

## Start FastAPI backend
```bash
cd backend
uvicorn main:app --reload
```

## Start frontend
```bash
cd frontend 
streamlit run app.py
```

## Usage
Once the system is running, the Streamlit interface allows you to:

Enter transaction details (amounts, locations, time stamps, etc.).

Submit the data to the FastAPI backend.

View real-time fraud probability predictions returned by the model








