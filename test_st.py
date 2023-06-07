import streamlit as st
import pandas as pd
import asyncio
#import sketch
import requests


def call_api(path_to_df: str, prompt: str):
    url = "http://localhost:8000/process_text/"
    params = {"path_to_df": path_to_df, "prompt": prompt}
    
    response = requests.get(url, params=params)
    data = response.json()

    print(data)
    
    return data["processed_text"]


def get_response(df, prompt):

    #response = df.sketch.ask(prompt, call_display=False)
    #print(response)
    response = "hello world"
    return response
    
#df = pd.read_csv("data/test.csv")
prompt = "tell me the maximum gamma ray value"
path_to_df = "data/test.csv"
st.button("Ask query", on_click=call_api, kwargs={"path_to_df":path_to_df, "prompt":prompt})


