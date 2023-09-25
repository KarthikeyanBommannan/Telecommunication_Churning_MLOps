import logging

import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from zenml import step

@step
def data_split(df: pd.DataFrame) -> None:
    pass
