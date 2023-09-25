import logging

import pandas as pd
from zenml import step, pipeline 

class IngestData:
    """ Ingesting data from the data path
    """
    def __init__(self, data_path: str): # self = ingest_data ,data_path = link to the destination where the file is stored
        """
        Args: data_path (str): path to the data
        """
        self.data_path = data_path
    
    def get_data(self):
        """
        Ingesting the data from the data path.
        """
        logging.info(f"Ingesting data from {self.data_path}")
        return pd.read_csv(self.data_path)

@step
def ingest_df(data_path: str) -> pd.DataFrame:
    """Ingesting the data from data_path

    Args:
        data_path (str): path to the data

    Returns:
        pd.DataFrame: the ingested data
    """
    try:
        ingest_data = IngestData(data_path) # ingest_data is object and data_path is the parameter having the path for the file.
        df = ingest_data.get_data()
        return pd.DataFrame(df)
    except Exception as e:
        logging.error(f"Error while ingesting data {e}")
        raise e