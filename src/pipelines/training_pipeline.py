import numpy as np
import pandas as pd
import os 
import sys
from src.logger import logging
from src.exception import CustomException
from src.components.data_ingestion import DataIngestion



if __name__ == '__main__':
    logging.info('Data ingestion class Loaded')
    obj=DataIngestion()
    train_data_path,test_data_path=obj.initate_data_ingestion()
    print(train_data_path,test_data_path)
    logging.info('Training data is Completed')
    
    