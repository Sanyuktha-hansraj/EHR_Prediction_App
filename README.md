# 🏥 EHR_Prediction_App

A beginner-friendly **Streamlit web app** that predicts whether a patient is likely to be **In-Care** or **Out-Care** based on lab test results from Electronic Health Records (EHR). This project is designed to demonstrate basic data science and machine learning applied to healthcare.

---

## 📌 Project Objective

To build an easy-to-use machine learning application that:
- Accepts patient lab results as input
- Predicts care status using a trained Random Forest model
- Provides interactive predictions via a Streamlit interface

---

## 📊 Dataset Overview

- 📍 Source: Private hospital in Indonesia  
- 🎯 Goal: Classify patients as **In-Care (`in`)** or **Out-Care (`out`)**  
- 🔢 Features:
  - HAEMATOCRIT
  - HAEMOGLOBINS
  - ERYTHROCYTE
  - LEUCOCYTE
  - THROMBOCYTE
  - MCH
  - MCHC
  - MCV
  - AGE
  - SEX  
- ✅ Target Column: `SOURCE` (`in` / `out`)

---

## 🛠️ Tools & Technologies

- 🐍 Python 3  
- 📘 Pandas, scikit-learn  
- 🌐 Streamlit (for the web app UI)  
- 📊 Random Forest Classifier

---

## 🚀 How to Run This App

### 1. Clone the repository  
`git clone https://github.com/Sanyuktha-hansraj/EHR_Prediction_App.git`  
`cd EHR_Prediction_App`

### 2. Install the required packages  
`pip install -r requirements.txt`  

Or manually:  
`pip install streamlit pandas scikit-learn`

### 3. Run the Streamlit app  
`streamlit run ehr_app.py`  

The app will open in your browser at `http://localhost:8501`.

---

## 🧪 Sample Test Input (for Demo)

Try these values in the app:

Haematocrit: 27.5  
Haemoglobins: 9.6  
Erythrocyte: 3.9  
Leucocyte: 14.5  
Thrombocyte: 250  
MCH: 22.0  
MCHC: 30.5  
MCV: 70.2  
AGE: 62  
SEX: F

✅ **Expected Output:** IN CARE

---

## 📁 Project Structure

EHR_Prediction_App/  
├── ehr_app.py → Streamlit app source code  
├── data-ori.csv → Input EHR dataset  
├── requirements.txt → Package dependencies  
└── README.md → Project documentation

---

## 📈 Future Enhancements

- Add feature importance visualizations  
- Integrate SHAP or LIME for explainability  
- Enable CSV uploads for batch predictions  
- Deploy on Streamlit Cloud for public access

---

## 👩‍⚕️ Author

**Sanyuktha Hansraj**  
MSc Data Analytics with Bio AI – Digital University Kerala  
GitHub: [@Sanyuktha-hansraj](https://github.com/Sanyuktha-hansraj)

---

## ⚠️ Disclaimer

This project is for academic and educational purposes only.  
It is **not** intended for real clinical use or medical diagnosis.


