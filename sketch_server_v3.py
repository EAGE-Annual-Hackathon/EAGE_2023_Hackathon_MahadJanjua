from fastapi import FastAPI
import sketch
import pandas as pd
import json
from typing import List
from frontend.UnstructuredProcessSingle import process_file_into_df



app = FastAPI()

@app.get("/process_text_v3/")
def process_text_v3(path_to_df: str, prompt: str):
    # Call your function with the input text prompt here
    # Replace the following line with your own function logic

    df, _ = process_file_into_df(path_to_df)

    result = df.sketch.ask(prompt, call_display=False)
    processed_text = f"Output: {result}"
    
    return {"processed_text": processed_text}




