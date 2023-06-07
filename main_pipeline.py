import streamlit as st
import pandas as pd
from frontend.StreamlitFunctions import *
from frontend.ProcessFunctions import *
from frontend.StructuredProcess import *
from frontend.UnstructuredProcess import *
from frontend.UnstructuredProcessSingle import *

def main():

    state, status = st_layout_pipeline(
        background_image="app_images/background.png",
        logo_image="app_images/wdb.png",
        style_css=".streamlit/style.css"
    )

    state.process_select, status = process_type_selection(status)

    st.write("")
    state.process_select_confirmed = st.button("Start Process")

    if state.process_select_confirmed is True:
        status.info("Process selected!")
        state.begin_process = True

    if state.begin_process:
        if state.process_select == "Structured Data (Single)":
            state, status = structured_pipeline(state, status)
        elif state.process_select == "Unstructured Data (Single)":
            state, status = unstructured_pipeline_single(state, status)
        elif state.process_select == "Unstructured Data (Bulk)":
            state, status = unstructured_pipeline(state, status)
        

if __name__ == "__main__":
    main()
