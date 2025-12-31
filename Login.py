import streamlit as st
import requests

API_KEY = st.secrets["firebase_api_key"]

st.title("Login")

username = st.text_input("Username")
password = st.text_input("Password", type="password")

if st.button("Login"):
    email = f"{username}@app.local"
    url = f"https://identitytoolkit.googleapis.com/v1/accounts:signInWithPassword?key={API_KEY}"

    res = requests.post(url, json={
        "email": email,
        "password": password,
        "returnSecureToken": True
    })

    if res.status_code == 200:
        st.session_state["user"] = username
        st.success("Login successful")
        st.experimental_rerun()
    else:
        st.error("Username ama Password khaldan")
