import httpx
import streamlit as st

st.title("Hello World App")

if st.button("Get Greeting"):
    response = httpx.get("http://backend:80")
    data = response.json()
    st.write(data["message"])
