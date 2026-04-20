from flask import Flask, request, jsonify
from flask_cors import CORS
import joblib
import os
from vectorizer_utils import preprocess_text

app = Flask(__name__)
CORS(app)  # 🔥 Enable CORS (VERY IMPORTANT)

BASE_DIR = os.path.dirname(__file__)

# Load model and vectorizer
model = joblib.load(os.path.join(BASE_DIR, "phishing_model.pkl"))
vectorizer = joblib.load(os.path.join(BASE_DIR, "vectorizer.pkl"))

# ✅ Home route (avoid 404)
@app.route('/')
def home():
    return "✅ AI Phishing Detection API Running..."

# ✅ Detection API
@app.route('/detect', methods=['POST'])
def detect():
    data = request.get_json()

    email = data.get("email", "")
    url = data.get("url", "")

    # Combine input
    combined_text = email + " " + url

    # Preprocess
    processed_text = preprocess_text(combined_text)

    # Vectorize
    vector = vectorizer.transform([processed_text])

    # Predict
    prediction = model.predict(vector)[0]
    probability = model.predict_proba(vector)[0][1]

    return jsonify({
        "result": "Phishing" if prediction == 1 else "Legitimate",
        "confidence": round(probability * 100, 2)
    })

if __name__ == "__main__":
    # 🔥 Important for mobile testing also
    app.run(host="0.0.0.0", port=5000, debug=True)