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
import initialization as init 

result_sql_code = init.vn.generate_sql(question='list all open documents')
print(result_sql_code)
log = init.vn.ws.receive()
print(log)