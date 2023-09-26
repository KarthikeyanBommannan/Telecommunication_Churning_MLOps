import os 
from box.exceptions import BoxValueError
import yaml
from Telco_Churn_MLOps import logger
import json
import joblib
from ensure import ensure_annotations
from box import ConfigBox
from typing import Any 


@ensure_annotations
def read_yaml(path_to_yaml: str) -> ConfigBox:
    """
    Read a YAML file and return its contents as a ConfigBox object.

    Parameters:
        path_to_yaml (path): The path to the YAML file to be read.

    Returns:
        ConfigBox: A ConfigBox object containing the contents of the YAML file.

    Raises:
        ValueError: If the YAML file is empty.
        Exception: If an error occurs while reading the YAML file.
    """
    try:
        with open(path_to_yaml) as yaml_file:
            content = yaml.safe_load(yaml_file)
            logger.info(f"yaml file:{path_to_yaml} loaded successfully")
            return ConfigBox(content)
    except BoxValueError:
        raise ValueError("yaml file is empty")
    except Exception as e:
        raise e
        