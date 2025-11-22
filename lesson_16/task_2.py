import os
import json
import logging


log_filename = "json__bakhmatska.log"

logging.basicConfig(
    filename=log_filename,
    level=logging.ERROR,
    format="%(asctime)s - %(levelname)s - %(message)s"
)
logger = logging.getLogger()

folder_path = "work_with_json"

for filename in os.listdir(folder_path):
    file_path = os.path.join(folder_path, filename)

    if os.path.isfile(file_path):
        try:
            with open(file_path, 'r') as f:
                json.load(f)
            print(f" File '{filename}' is valid JSON ")
        except (json.JSONDecodeError, UnicodeDecodeError) as e:
            logger.error(f"File '{filename}' is not valid JSON: {e}")
            print(f" File '{filename}' is NOT valid JSON, details in log-file: {log_filename} ")
