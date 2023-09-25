import logging

import pandas as pd
import numpy as np
from sklearn.preprocessing import LabelEncoder
from sklearn.preprocessing import OneHotEncoder
from zenml import step

@step 
def data_encoding(df: pd.DataFrame) -> pd.DataFrame:
    pass



