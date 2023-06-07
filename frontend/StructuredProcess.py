import streamlit as st
import pandas as pd
import requests
from frontend.streamlit_state_handling import *


def add_title_step_1():
    """
    Adding title for step 1 - specifying file type
    """
    st.write("------------------------------------\n------------------------------------")
    st.markdown(f"### Step 1: Specifying the filetype")
    st.markdown("##### Please upload file to be processed.")


def excel_csv_loading(state):
    """
    Uploading and processing jpg/png/tif file
    """

    # file is uploaded
    uploaded_file = st.file_uploader(label='Upload file of type:', type=['xlsx', 'csv'])
    
    if uploaded_file is None:

        state.file = None
        state = state_upload_file_none(state)

    else:

        # file converted to numpy array for later processing

        state.file = uploaded_file 
        state.file_path = state.file.name

    return state


def convert_file_to_df(state, status):

    status.info("Process file into a dataframe...")

    if state.file is not None:
        if state.file.name.endswith(".csv"):
            state.method_one_df = pd.read_csv(state.file)

        elif state.file.name.endswith(".xlsx"):
            state.method_one_df = pd.read_excel(state.file)

    return state, status


def display_df_on_app(state, status):

    if state.method_one_df is not None:

        status.info("Displaying extracted dataframe...")
        st.write("")
        st.write(state.method_one_df)

    return status


def add_title_step_2(state):
    """
    Adding title for step 2 - begin chatting
    """

    if state.file is not None:
        st.write("------------------------------------\n------------------------------------")
        st.markdown(f"### Step 2: Information extraction via user query")


def input_query_text_area(state, status):

    if state.file is not None:

        status.info("Please enter your query...")
        col1, _ = st.columns([0.7, 0.3])

        with col1:

            state.query_method_one = st.text_area("Please enter your query regarding uploaded file:")
        
        if st.button("Save query"):
            state.save_query = True

    return state, status

def generate_proper_prompt(state):

    if state.save_query:
        state.query_boundary_condition = "Do not use your foundation knowledge. Only answer questions based on information provided in the context."
        state.prompt_method_one = state.query_boundary_condition + " " + state.query_method_one
        state.que_response_gen = True
        state.response_method_one = None

    return state


def call_api(state, path_to_df: str, prompt: str):

    #print(path_to_df)
    #print(prompt)
    url = "http://localhost:8000/process_text/"
    params = {"path_to_df": path_to_df, "prompt": prompt}
    
    response = requests.get(url, params=params)
    result = response.json()["processed_text"]
    state.response_method_one = result[len("Output: "):]
    
    return state


def generate_response(state, status):

    if state.que_response_gen:

        status.info("Ready for response generation!")

        st.write("----------------------------------------------------")

        if st.button("Ask query"):
            st.write("")
            with st.spinner("Generating response..."):
                # on_click=call_api, kwargs={"state": state, "path_to_df": state.file.name, "prompt": state.prompt_method_one}
                state = call_api(state, path_to_df=state.file.name, prompt=state.prompt_method_one)

    return state, status

def display_response(state, status):

    if state.response_method_one is not None:

        status.info("Dislaying response")
        _,  col2 = st.columns([0.3, 0.7])
        with col2:
            st.caption("Response:")
            st.success(state.response_method_one, icon="🤖")


def structured_pipeline(state, status):

    add_title_step_1()

    state = excel_csv_loading(state)

    state, status = convert_file_to_df(state, status)

    status = display_df_on_app(state, status)

    add_title_step_2(state)

    state, status = input_query_text_area(state, status)
    state = generate_proper_prompt(state)
    state, status = generate_response(state, status)

    display_response(state, status)
    
    return state, status