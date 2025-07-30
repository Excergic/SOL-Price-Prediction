import logging
from logging.handlers import RotatingFileHandler
import os
from datetime import datetime

## Log file Name
LOG_FILE_NAME = f"{datetime.now().strftime('%m_%d_%Y_%H_%M_%S')}.log"

LOG_PATH = os.path.join(os.getcwd(), "logs")
os.makedirs(LOG_PATH, exist_ok=True) ## create log folder if not exist, /logs/log_file_name.log
 
LOG_FILE_PATH = os.path.join(LOG_PATH, LOG_FILE_NAME) ## log file path, cwd/logs/log_file_name.log
MAX_LOG_SIZE = 5 * 1024 * 1024  # 5 MB
BACKUP_COUNT = 3  # Number of backup log files to keep

## Logging Levels
def configure_logger():
    """
     Configures logging with a rotating file handler and a console handler.
    """

    # create a custom logger
    logger = logging.getLogger()
    logger.setLevel(logging.DEBUG)

    # Formatter
    formatter = logging.Formatter("[ %(asctime)s ] %(name)s - %(levelname)s - %(message)s")

    # File handler with rotation
    file_handler = RotatingFileHandler(LOG_FILE_PATH, maxBytes=MAX_LOG_SIZE, backupCount=BACKUP_COUNT)
    file_handler.setFormatter(formatter)
    file_handler.setLevel(logging.DEBUG)

    # Console handler
    console_handler = logging.StreamHandler()
    console_handler.setFormatter(formatter)
    console_handler.setLevel(logging.INFO)

    # Add handlers to the logger
    logger.addHandler(file_handler)
    logger.addHandler(console_handler)

# Configure the logger
configure_logger()