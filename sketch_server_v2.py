from fastapi import FastAPI
import sketch
import pandas as pd
import json
from typing import List

app = FastAPI()

@app.get("/process_text_v2/")
def process_text_v2(path_to_df: str, prompt: str):
    # Call your function with the input text prompt here
    # Replace the following line with your own function logic

    if path_to_df.endswith(".csv"):
        df = pd.read_csv(path_to_df)
    elif path_to_df.endswith(".xlsx"):
        df = pd.read_excel(path_to_df)

    result = df.sketch.ask(prompt, call_display=False)
    processed_text = f"Output: {result}"
    
    return {"processed_text": processed_text}




