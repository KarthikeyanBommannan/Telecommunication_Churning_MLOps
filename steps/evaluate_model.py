import logging

import pandas as pd
from zenml import step
from sklearn.metrics import accuracy_score, f1_score, classification_report, recall_score

@step
def evaluate_model(df: pd.DataFrame) -> None:
    """Evaluate the model on ingested data

    Args:
        df (pd.DataFrame): ingested data
    """