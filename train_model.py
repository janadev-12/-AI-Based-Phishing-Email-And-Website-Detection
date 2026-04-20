import pandas as pd
import os
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
import joblib

from vectorizer_utils import TextVectorizer, preprocess_text

BASE_DIR = os.path.dirname(__file__)
file_path = os.path.join(BASE_DIR, "phishing_emails.csv")

# Load dataset
data = pd.read_csv(file_path)

# Preprocess
data["text"] = data["text"].apply(preprocess_text)

X = data["text"]
y = data["label"]

# Split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

# Vectorize
vectorizer = TextVectorizer()
X_train_vec = vectorizer.fit_transform(X_train)

# Train model
model = RandomForestClassifier()
model.fit(X_train_vec, y_train)

# Save model & vectorizer
joblib.dump(model, os.path.join(BASE_DIR, "phishing_model.pkl"))
joblib.dump(vectorizer.vectorizer, os.path.join(BASE_DIR, "vectorizer.pkl"))

print("✅ Model trained and saved successfully")