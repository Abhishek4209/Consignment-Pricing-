import logging
from datatime import datetime
import os

LOG_FILE=f'datetime.now().strftime("%M_%D_%Y_%H_%M_%S").log'
logs_path=os.path.join(os.getcwd(), 'logs',LOG_FILE)
os.makedirs(logs_path,exists_ok=True)

LOG_FILE_PATH=os.path.join(logs_path,LOG_FILE)

logging.basicConfig(level=logging.INFO,
                    format="[ %(asctime)s ] %(lineno)d %(name)s - %(levelname)s - %(message)s",
                    filename=LOG_FILE_PATH)