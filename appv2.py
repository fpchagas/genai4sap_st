import streamlit as st
from streamlit.components.v1 import html
from streamlit_google_auth import Authenticate
import pandas
import google.oauth2.id_token
from google.oauth2 import id_token
from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from utilities import (PROJECT_ID, MODEL, LANGUAGE, LOGO_URL, APP_TITLE, APP_SUBTITLE, API_KEY)
from vanna.chromadb import ChromaDB_VectorStore
from vanna.google import GoogleGeminiChat

#st.logo("my_logo.png")
st.set_page_config(layout="wide", page_title="GENAI4SAP", page_icon="./images/CorAv2Streamlit.png", initial_sidebar_state='collapsed')
with open( "css/style.css" ) as css:
    st.markdown(f'<style>{css.read()}</style>' , unsafe_allow_html= True)

with st.sidebar:
  st.subheader("Having fun yet?")
  st.slider("Amount of fun", 0, 1000, 450, key="slide")
  st.radio("Your thoughts", ["I agree", "I disagree"], key="radio")
  st.text_input("Thoughts", placeholder="Add your thoughts", label_visibility="collapsed")
  st.button("Submit")

pages = {
    "Your account": [
        st.Page("page/home.py", title="Home", default=True, icon=":material/home:"),
        st.Page("page/debug.py", title="Debug", icon=":material/engineering:"),
    ]
}

pg = st.navigation(pages)
pg.run()