import logging  # Import the logging module to enable logging
import os       # Import os to handle file and directory paths
from datetime import datetime  # Import datetime to create a timestamped log file name

# Create a log file name using the current date and time
LOG_FILE = f"{datetime.now().strftime('%m_%d_%Y_%H_%M_%S')}.log"

# Define the path to the 'logs' directory where logs will be saved
logs_dir = os.path.join(os.getcwd(), "logs")  # Join current working directory with "logs"

# Create the 'logs' directory if it doesn't already exist
os.makedirs(logs_dir, exist_ok=True)

# Full path to the log file inside the 'logs' directory
LOG_FILE_PATH = os.path.join(logs_dir, LOG_FILE)

# Configure the logging settings
logging.basicConfig(
    filename=LOG_FILE_PATH,                         # Set the log file location
    format="[%(asctime)s] %(lineno)d - %(levelname)s - %(message)s",  # Log format
    level=logging.INFO                              # Set the minimum log level to INFO
)


