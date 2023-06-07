import streamlit as st

def process_type_selection(status):

    status.info("Please select an information extraction method...")
    process_select = st.radio(
    "**Please select the method for information extraction**:",
    ('Structured Data (Single)', 'Unstructured Data (Single)', 'Unstructured Data (Bulk)'))

    return process_select, status