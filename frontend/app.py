import httpx
import streamlit as st

st.title("Hello World App")

if st.button("Get Greeting"):
    response = httpx.get("http://172.30.109.56:8080")
    data = response.json()
    st.write(data["message"])
