 AI-Based Phishing Detection System

 Overview

This project is an AI-powered phishing detection system that analyzes URLs and email content to determine whether they are **phishing or legitimate**. It uses Machine Learning techniques to classify inputs in real-time.

---

 Features

* 🔍 Detect phishing emails and URLs
* 🤖 Machine Learning model (Random Forest)
* 📊 TF-IDF text vectorization
* ⚡ Real-time prediction
* 💻 Hacker-style UI with Matrix animation

---

 Tech Stack

* **Frontend:** HTML, CSS, JavaScript
* **Backend:** Python, Flask
* **Machine Learning:** Scikit-learn
* **Libraries:** Pandas, Joblib

---

 Project Structure

```
AI-based-phishing/
│
├── backend/
│   ├── app.py
│   ├── train_model.py
│   ├── vectorizer_utils.py
│   ├── generate_dataset.py
│   ├── phishing_emails.csv
│   ├── phishing_model.pkl
│   ├── vectorizer.pkl
│
├── frontend/
│   ├── index.html
│   ├── style.css
│   ├── script.js
│
└── README.md
```

---

    Setup Instructions

 Install Dependencies

```
pip install flask flask-cors scikit-learn pandas joblib
```

---

 Generate Dataset

```
python generate_dataset.py
```

---

 Train the Model

```
python train_model.py
```

---

 Run Backend Server

```
python app.py
```

---

 Run Frontend

Open:

```
frontend/index.html
```

---

 Model Details

* **Algorithm:** Random Forest Classifier
* **Vectorization:** TF-IDF
* **Dataset Size:** 6000+ samples
* **Accuracy:** ~85% – 95%

---

 How It Works

1. User enters a URL or Email
2. Input is preprocessed
3. TF-IDF converts text into features
4. Model predicts result
5. Output shown as **Phishing 🚨 or Legit ✅**

---

 Author

  R.JANAVANTH

---

 Future Improvements

* 🔗 Chrome Extension
* 📧 Real-time email scanner
* ☁️ Cloud deployment
* 🧠 Deep Learning model (LSTM)

 Note

This project is built for educational and cybersecurity awareness purposes.