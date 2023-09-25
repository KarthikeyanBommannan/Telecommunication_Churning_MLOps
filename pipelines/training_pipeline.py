from zenml import pipeline

from steps.ingest_data import ingest_df
from steps.clean_data import clean_data
from steps.encode import data_encoding
from steps.split import data_split
from steps.data_balancing import balance_data
from steps.model_train import train_model
from steps.evaluate_model import evaluate_model


@pipeline
def train_pipeline(data_path: str):
    df = ingest_df(data_path)
    cleaned = clean_data(df)
    encoded = data_encoding(cleaned)
    splitted = data_split(encoded)
    
    
    
    
    