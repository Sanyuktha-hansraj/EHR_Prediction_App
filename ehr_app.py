import streamlit as st
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score

# Page title
st.title("🏥 EHR-Based Patient Care Prediction")
st.write("Predict whether a patient is **In-Care** or **Out-Care** using lab test results.")

# Load data
@st.cache_data
def load_data():
    df = pd.read_csv("data-ori.csv")
    return df

df = load_data()

# Show first few rows of the dataset
st.subheader("📊 Preview of EHR Data")
st.dataframe(df.head())

# Encode categorical columns
le_sex = LabelEncoder()
df['SEX'] = le_sex.fit_transform(df['SEX'])

le_target = LabelEncoder()
df['SOURCE'] = le_target.fit_transform(df['SOURCE'])  # 0 = in, 1 = out

# Define features and target
X = df.drop('SOURCE', axis=1)
y = df['SOURCE']

# Split into train and test sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train a Random Forest Classifier
model = RandomForestClassifier(random_state=42)
model.fit(X_train, y_train)

# Evaluate model accuracy
y_pred = model.predict(X_test)
accuracy = accuracy_score(y_test, y_pred)
st.success(f"✅ Model trained with {accuracy:.2%} accuracy")

# Sidebar for user input
st.sidebar.header("🔍 Enter Patient Lab Test Results")

def user_input():
    data = {
        "HAEMATOCRIT": st.sidebar.number_input("Haematocrit", 20.0, 60.0, 35.0),
        "HAEMOGLOBINS": st.sidebar.number_input("Haemoglobins", 5.0, 18.0, 12.0),
        "ERYTHROCYTE": st.sidebar.number_input("Erythrocyte", 2.0, 7.0, 4.5),
        "LEUCOCYTE": st.sidebar.number_input("Leucocyte", 3.0, 15.0, 6.5),
        "THROMBOCYTE": st.sidebar.number_input("Thrombocyte", 100, 500, 300),
        "MCH": st.sidebar.number_input("MCH", 20.0, 35.0, 27.0),
        "MCHC": st.sidebar.number_input("MCHC", 28.0, 38.0, 32.0),
        "MCV": st.sidebar.number_input("MCV", 70.0, 110.0, 85.0),
        "AGE": st.sidebar.slider("Age", 0, 100, 30),
        "SEX": st.sidebar.selectbox("Sex", ["M", "F"])
    }
    data["SEX"] = le_sex.transform([data["SEX"]])[0]
    return pd.DataFrame([data])

input_df = user_input()

# Show input and prediction
if st.button("🔮 Predict Care Type"):
    result = model.predict(input_df)[0]
    care_type = le_target.inverse_transform([result])[0]
    st.subheader("🧾 Prediction")
    st.write(f"🩺 The model predicts this patient as: **{care_type.upper()} CARE**")


