import logging     # any excecution of the code will be logged in the log file to track the error
import os
from datetime import datetime

LOG_FILE = f"{datetime.now().strftime('%m_%d_%Y_%H_%M_%S')}.log"  # log file name with timestamp
logs_path = os.path.join(os.getcwd(), "logs",LOG_FILE) # log file path
os.makedirs(logs_path,exist_ok=True) # create log file if not exist

LOG_FILE_PATH = os.path.join(logs_path,LOG_FILE)

logging.basicConfig(
    filename=LOG_FILE_PATH,
    format='[%(asctime)s]- %(name)s - %(levelname)s - %(message)s', # log file format
    level = logging.INFO, # log file level
)
