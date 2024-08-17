import numpy as np
import pandas as pd
import os,sys
from src.logger import logging
from src.exception import CustomException
from dataclasses import dataclass


## Data transformation config:
@dataclasses
class DataTransformationConfig:
    preprocessor_file_path=os.path.join('artifacts','preprocessor.pkl')
    
## Data Transformation class:
class DataTransformation:
    def __init__(self):
        self.data_transformation_config=DataTransformationConfig()
        
    def ModelTransformation(self):
        try:
            pass
        
        
        except Exception as e:
            logging.info('Some error Occured into ')
            raise CustomException(e,sys)