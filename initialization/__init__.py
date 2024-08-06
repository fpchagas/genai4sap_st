import google.cloud.bigquery as bigquery
import google.oauth2
import json
import streamlit as st
import random
import os
import sys
import requests
import configparser
from streamlit.components.v1 import html
from streamlit_google_auth import Authenticate
import pandas
import google.auth.transport.requests
import google.oauth2.id_token
from google.oauth2 import id_token
from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from utilities import (PROJECT_ID, MODEL, LANGUAGE, LOGO_URL, APP_TITLE, APP_SUBTITLE, API_KEY)
from vanna.chromadb import ChromaDB_VectorStore
from vanna.google import GoogleGeminiChat


class MyVanna(ChromaDB_VectorStore, GoogleGeminiChat):
    def __init__(self, config={'path':'./chroma_data'}):
        ChromaDB_VectorStore.__init__(self, config=config)
        GoogleGeminiChat.__init__(self, config={'api_key': f'{API_KEY}', 'model': f'{MODEL}', 'language': f'{LANGUAGE}', 'temperature': 0.2})

vn = MyVanna()

vn.connect_to_bigquery(project_id=PROJECT_ID)