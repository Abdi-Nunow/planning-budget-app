import streamlit as st
import firebase_admin
from firebase_admin import credentials, firestore

# Firebase init ka akhrinaya Streamlit Secrets
if not firebase_admin._apps:
    cred = credentials.Certificate(dict(st.secrets["firebase"]))
    firebase_admin.initialize_app(cred)

db = firestore.client()

st.title("Planning & Budget Submission System")
st.write("Fadlan isticmaal menu-ga bidix")

# Web API Key
API_KEY = st.secrets["firebase_api_key"]



