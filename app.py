import streamlit as st
import firebase_admin
from firebase_admin import credentials, firestore

# 1. Firebase initialization
if not firebase_admin._apps:
    cred = credentials.Certificate(dict(st.secrets["firebase"]))
    firebase_admin.initialize_app(cred)

# 2. Firestore client
db = firestore.client()

# 3. Streamlit page settings
st.set_page_config(page_title="Planning & Budget System", layout="wide")

# 4. Header
st.title("Planning & Budget Submission System")
st.write("Fadlan isticmaal menu-ga bidix")

