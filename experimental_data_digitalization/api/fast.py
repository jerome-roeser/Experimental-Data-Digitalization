import pandas as pd
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from experimental_data_digitalization.data.preprocess import get_file_metadata

# from taxifare.ml_logic.registry import load_model
# from taxifare.ml_logic.preprocessor import preprocess_features
# from taxifare.interface.main import pred

app = FastAPI()

# Allowing all middleware is optional, but good practice for dev purposes
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allows all origins
    allow_credentials=True,
    allow_methods=["*"],  # Allows all methods
    allow_headers=["*"],  # Allows all headers
)

@app.get("/")
def root():
    return {'greeting': 'Hello'}


@app.get("/metadata")
def figures() -> dict:
    """
    Input: a pdf file
    Output: the number of figures in the paper
    """
    metadata = get_file_metadata()
    return {'metadata' : metadata}
