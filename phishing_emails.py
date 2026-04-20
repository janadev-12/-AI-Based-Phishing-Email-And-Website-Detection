import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, classification_report
import joblib

from vectorizer_utils import TextVectorizer, preprocess_text

# Load dataset
data = pd.read_csv("phishing_emails.csv")

# Preprocess text
data["text"] = data["text"].apply(preprocess_text)

# Split
X = data["text"]
y = data["label"]

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# Vectorizer
vectorizer = TextVectorizer()
X_train_vec = vectorizer.fit_transform(X_train)
X_test_vec = vectorizer.transform(X_test)

# Model
model = RandomForestClassifier(n_estimators=100, random_state=42)
model.fit(X_train_vec, y_train)

# Evaluate
y_pred = model.predict(X_test_vec)

print("Accuracy:", accuracy_score(y_test, y_pred))
print(classification_report(y_test, y_pred))

# 🔥 IMPORTANT — ADD HERE (LAST LA)
joblib.dump(model, "phishing_model.pkl")
joblib.dump(vectorizer.vectorizer, "vectorizer.pkl")

print("✅ Model and Vectorizer saved successfully")
import os

BASE_DIR = os.path.dirname(__file__)
file_path = os.path.join(BASE_DIR, "phishing_emails.csv")

data = pd.read_csv(file_path)