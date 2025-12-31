import streamlit as st
import firebase_admin
from firebase_admin import credentials, firestore

# -------------------------------
# 1️⃣ Firebase Initialization
# -------------------------------
if not firebase_admin._apps:
    cred = credentials.Certificate(dict(st.secrets["firebase"]))
    firebase_admin.initialize_app(cred)

# Firestore client
db = firestore.client()

# -------------------------------
# 2️⃣ Streamlit page settings
# -------------------------------
st.set_page_config(page_title="Planning & Budget System", layout="wide")

# -------------------------------
# 3️⃣ Header
# -------------------------------
st.title("Planning & Budget Submission System")
st.write("Fadlan isticmaal menu-ga bidix")

# -------------------------------
# 4️⃣ Web API Key
# -------------------------------
API_KEY = st.secrets["firebase_api_key"]

# Example (kaliya test, kadib tirtir)
st.write("Web API Key loaded successfully")


