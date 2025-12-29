"""
models.py

Used to train the fraud detection model.
Run once to generate fraud_pipeline.pkl.
Not used at inference time.
"""
from sklearn.pipeline import Pipeline
from sklearn.compose import ColumnTransformer
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler, OneHotEncoder
from sklearn.impute import SimpleImputer
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report, confusion_matrix
import numpy as np
import pandas as pd 
import joblib
import os 

data = pd.read_csv("data/PS_20174392719_1491204439457_log.csv", nrows=50000)

#Target and feature variables 

X = data[["step","type","amount"]]
y = data["isFraud"]

#Seperating columns

numerical_cols = ["step","amount"]
categorical_cols = ["type"]

#Pipeline encoding

numerical_pipeline = Pipeline([
    ('imputer', SimpleImputer(strategy='mean')),
    ('scaler', StandardScaler())
])

categorical_pipeline = Pipeline([
    ('imputer', SimpleImputer(strategy='most_frequent')),
    ('encoder', OneHotEncoder(handle_unknown='ignore'))
])

#Join pipeline

preprocessor = ColumnTransformer([
    ('num', numerical_pipeline, numerical_cols),
    ('cat', categorical_pipeline, categorical_cols)
])

#Final pipeline

pipeline = Pipeline([
    ('preprocessor', preprocessor),
    ('model', RandomForestClassifier(
        n_estimators=100,
        random_state=42,
        class_weight='balanced',
        n_jobs=1
    ))
])

#Split data set

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=1, stratify=y)

#Training 

pipeline.fit(X_train, y_train)
y_pred = pipeline.predict(X_test)

print(classification_report(y_test, y_pred))

os.makedirs("backend/models", exist_ok=True)

joblib.dump(pipeline, "backend/models/fraud_pipeline.pkl")

















