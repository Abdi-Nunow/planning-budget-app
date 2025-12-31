import streamlit as st
import firebase_admin
from firebase_admin import credentials, firestore

# Firebase initialization
if not firebase_admin._apps:
    cred = credentials.Certificate(dict(st.secrets["firebase"]))
    firebase_admin.initialize_app(cred)

db = firestore.client()

st.set_page_config(page_title="Planning & Budget System", layout="wide")
st.title("Planning & Budget Submission System")
st.write("Fadlan isticmaal menu-ga bidix")

# Access API_KEY if needed
API_KEY = st.secrets["AIzaSyAQUJ6UIwmSulo2ewXBZojiRBzRH7LEdXw"]


