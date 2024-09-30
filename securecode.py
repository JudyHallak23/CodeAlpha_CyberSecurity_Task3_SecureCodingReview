import os
import json
import logging
from werkzeug.security import generate_password_hash, check_password_hash

logging.basicConfig(level=logging.INFO, filename='app.log',
                    format='%(asctime)s - %(levelname)s - %(message)s')

SECRET_KEY = os.getenv("SECRET_KEY")

def secure_function(user_input):
    safe_commands = ['list', 'show']
    if user_input in safe_commands:
        os.system(f"echo {user_input}")
    else:
        logging.warning("Unauthorized command attempted.")

def secure_logging(data):
    logging.info("User performed an action.")

def safe_deserialization(serialized_data):
    try:
        data = json.loads(serialized_data)
        if not isinstance(data, dict):
            raise ValueError("Invalid data format.")
        return data
    except json.JSONDecodeError:
        logging.error("Failed to decode JSON.")
        return {}

def secure_file_download(filename):
    safe_directory = "/downloads/"
    if '..' in filename or filename.startswith('/'):
        logging.warning("Attempted directory traversal.")
        return "Invalid file name."

    file_path = os.path.join(safe_directory, filename)
    if os.path.isfile(file_path):
        with open(file_path, 'rb') as f:
            return f.read()
    else:
        logging.warning("File not found.")
        return "File not found."

def main():
    user_input = input("Enter a command to execute (list/show): ")
    secure_function(user_input)

    sensitive_data = input("Enter some data: ")
    secure_logging(sensitive_data)

    serialized_data = input("Enter serialized data (JSON): ")
    data = safe_deserialization(serialized_data)
    print(f"Deserialized data: {data}")

    filename = input("Enter the file name to download: ")
    file_content = secure_file_download(filename)
    print("File content downloaded." if isinstance(file_content, bytes) else file_content)

if __name__ == "__main__":
    main()



