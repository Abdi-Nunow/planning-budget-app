import streamlit as st
from firebase_admin import auth, firestore
from data.regions import somali_region

db = firestore.client()

st.title("Create District User")

username = st.text_input("Username")
password = st.text_input("Password", type="password")

region = st.selectbox("Gobol", list(somali_region.keys()))
district = st.selectbox("Degmo", somali_region[region])

if st.button("Create User"):
    user = auth.create_user(
        email=f"{username}@app.local",
        password=password
    )

    db.collection("users").document(user.uid).set({
        "username": username,
        "role": "district",
        "region": region,
        "district": district
    })

    st.success("Degmo user waa la sameeyay")
