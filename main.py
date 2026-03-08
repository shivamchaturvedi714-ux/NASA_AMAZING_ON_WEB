import requests
import streamlit as st

url="https://api.nasa.gov/planetary/apod?api_key=XNy96e5ppGyBQX6emMtUGHtIfcf8Bjokwb4gXPkd"
r=requests.get(url)
content = r.json()
st.title(content["title"])
st.image(content["url"])
st.write(content["explanation"])
if st.button("refresh"):
    st.rerun()



