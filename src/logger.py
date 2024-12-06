import logging
import os
from datetime import datetime

# Create log directory and file name
LOG_FILE = f"{datetime.now().strftime('%m_%d_%Y_%H_%M_%S')}.log"
logs_path = os.path.join(os.getcwd(), "logs")
# alternative way, is to create additional folder inside the log folder, but unnessecary
# logs_path = os.path.join(os.getcwd(), "logs")
os.makedirs(logs_path, exist_ok=True)

# Full path for the log file
LOG_FILE_PATH = os.path.join(logs_path, LOG_FILE)

# Example
# logging.info("This is an info message.")
# [12/06/2024 15:45:12] 23 root - INFO - This is an info message.
# This essentially shows like print like statement in the log
logging.basicConfig(
    filename=LOG_FILE_PATH,
    format="[%(asctime)s ] %(lineno)d %(name)s - %(levelname)s - %(message)s",
    level = logging.INFO
)

# # control how this script behave when it is called directly
# # python logger.py
# # True if script is run directly
# # False if the script is imported as a module
# if __name__=="__main__":
#     logging.info("Logging has started")
