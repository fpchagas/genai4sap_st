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

#Building Frontend

st.image('./images/Coraheader970x250pxWhite.png', use_column_width="auto")
with st.expander("**Click to see instructions and sample questions!**", expanded=False):
    st.markdown(f"""
            **Seja específico e direto:**
            \nEspecifique a ação desejada: Comece sua pergunta com o verbo que indica a ação que você quer realizar (ex: "mostrar", "listar", "calcular", "resumir").
            \n**Defina os filtros:** 
            \nEspecifique claramente os critérios que você deseja usar para filtrar os resultados (ex: "onde o país é Brasil", "entre as datas X e Y").
            \n**Use linguagem clara e concisa:**
            \nEvite ambiguidades: Use termos precisos e evite gírias ou linguagem coloquial.
            \nSeja breve: Formule sua pergunta da forma mais simples e direta possível.
            \n
            """)

if "session_data" not in st.session_state:
    st.session_state.session_data = {
        "messages": [],
    }
for message in st.session_state.session_data["messages"]:
    with st.chat_message(message["role"], avatar=('./images/Userv2_128px.png' if message["role"] == 'human' else './images/CorAv2Streamlit.png')):
        if message["role"] == 'human':
            st.markdown(message["content"])
        else:
            if message["ok_code"] == 200:
                st.markdown(message["content"])
                with st.expander("Dados Solicitados:", expanded=True):
                        tab3, tab4 = st.tabs(["Data", "SQL"])
                        #tab3.write(message["Dados"],)
                        tab4.write(message["SQL"])
            elif message["ok_code"] == 201:
                st.markdown(message["content"])
                with st.expander("Generated SQL:", expanded=True):
                    st.write(message["SQL"])
            else:
                st.markdown(message["content"])

if prompt := st.chat_input("Let me show you my magic, ask me a question!"):
    st.chat_message("human", avatar='./images/Userv2_128px.png').markdown(prompt)
    st.session_state.session_data["messages"].append({"role": "human", "content": prompt})
    
    with st.chat_message("assistant", avatar='./images/CorAv2Streamlit.png'):
        with st.spinner("Doing the magic!!!"):
            result_sql_code = init.vn.generate_sql(question=prompt)
            print(result_sql_code)
            ai_response = "I'd be glad to help! Here's your answer!"
            st.session_state.session_data["messages"].append({"role": "assistant", "content": ai_response, "ok_code": 200, "SQL": result_sql_code})
            st.rerun()
            # if result_sql_code is not None:
            #     result_df = init.vn.run_sql(sql=result_sql_code)
            #     if not result_df.empty:              
            #         result_json = pandas.DataFrame.to_json(result_df.head(12),orient="records")
            #         ai_response = "I'd be glad to help! Here's your answer!"
            #         st.session_state.session_data["messages"].append({"role": "assistant", "content": ai_response, "ok_code": 200, "Dados": result_df, "SQL": result_sql_code["GeneratedSQL"]})
            #         st.rerun() 
            #     else:
            #         ai_response = "The query was generated successfully, but it did not return any data, please request different data!"
            #         with st.expander("Preview the generated query!"):
            #             st.write(result_sql_code["GeneratedSQL"])
            #         st.session_state.session_data["messages"].append({"role": "assistant", "content": ai_response, "ok_code": 201, "Dados": [], "SQL": result_sql_code["GeneratedSQL"], "Graph1": [], "Graph2": []})    
            #         st.rerun() 
            # else:
            #     ai_response = "Hmm, I'm still learning about that. Could you rephrase your question, or provide more context?"
            #     st.session_state.session_data["messages"].append({"role": "assistant", "content": ai_response, "ok_code": 500, "Dados": [], "SQL": [], "Graph1": [], "Graph2": []})
            #     st.rerun()