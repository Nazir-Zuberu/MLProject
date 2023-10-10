import logging
import os
from datetime import datetime

# Creating a file name using date
LOG_FILE = f"{datetime.now().strftime('%m_%d_%Y_%H_%M_%S')}.log"
# Create a path for the logging file. In other words, the location of the logging file
# Get the main working directory and create the logs folder and create the LOG_FILE in it
logs_path = os.path.join(os.getcwd(), "logs",LOG_FILE)
# Create a directory for logs using the date of the logging.
os.makedirs(logs_path, exist_ok=True)
# Joining the file name and path together. This enable us to get to the log_file
LOG_FILE_PATH = os.path.join(logs_path, LOG_FILE)

# Creating the logger
logging.basicConfig(
    filename=LOG_FILE_PATH,
    format= "[ %(asctime)s ] %(lineno)d %(name)s - %(levelname)s - %(message)s",
    level=logging.INFO,
)

if __name__ == "__main__":
    logging.info("Logging has started")