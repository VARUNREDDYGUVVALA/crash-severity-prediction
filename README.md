# 🚗 Crash Severity Prediction

Predict the severity of road accidents using Machine Learning — built with Python, Flask, and Scikit-Learn.

---

## 📘 Overview
This project aims to predict the **severity level of vehicle crashes** based on key factors such as weather, road conditions, and vehicle information. The goal is to help authorities and emergency responders prioritize their actions efficiently.

---

## 🧠 Key Features
- Data preprocessing and feature selection
- Machine Learning model (Random Forest)
- Flask web app with interactive UI
- Real-time crash severity prediction
- Scalable design ready for cloud deployment

---

## 🧩 Tech Stack
| Component | Technology |
|------------|-------------|
| **Frontend** | HTML, CSS, Bootstrap |
| **Backend** | Flask (Python) |
| **Machine Learning** | Scikit-Learn, Pandas, NumPy |
| **Model** | Random Forest |
| **Deployment (optional)** | Streamlit / Render / Hugging Face Spaces |

---

## 📊 Dataset
The dataset was obtained from **Kaggle** and cleaned to include only relevant features:
- Road surface condition  
- Light conditions  
- Weather  
- Vehicle type  
- Casualty class  
- Speed limit  

After preprocessing, top 10 features were selected using feature importance.

---

## 🧮 Model Training
- **Algorithm:** Random Forest Classifier  
- **Scaler:** StandardScaler  
- **Saved Models:** `random_forest_top10.pkl`, `scaler_top10.pkl`  
- **Performance Metrics:** Accuracy, F1-score, Confusion Matrix

---

## 💻 Run Locally

```bash
# Clone this repository
git clone https://github.com/VARUNREDDYGUVVALA/crash-severity-prediction.git
cd crash-severity-prediction/Crash\ severity\ DM

# Install dependencies
pip install -r requirements.txt

# Run Flask app
python app.py
