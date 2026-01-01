import streamlit as st
import firebase_admin
from firebase_admin import credentials, firestore

# Firebase init (SAH)
if not firebase_admin._apps:
    cred = credentials.Certificate(st.secrets["firebase"])
    firebase_admin.initialize_app(cred)

db = firestore.client()

st.title("Planning & Budget Submission System")
st.success("Firebase si guul leh ayuu u xirmay ✅")
