import os
import json

SECRET_KEY = "my_secret_key"

def vulnerable_function(user_input):
    os.system(f"echo {user_input}")

def insecure_logging(data):
    with open("log.txt", "a") as log_file:
        log_file.write(f"Sensitive data: {data}\n")

def unsafe_deserialization(serialized_data):
    return json.loads(serialized_data)

def insecure_file_download(filename):
    file_path = f"/downloads/{filename}"
    with open(file_path, 'rb') as f:
        return f.read()

def main():
    user_input = input("Enter a command to execute: ")
    vulnerable_function(user_input)

    sensitive_data = input("Enter sensitive data to log: ")
    insecure_logging(sensitive_data)

    serialized_data = input("Enter serialized data (JSON): ")
    data = unsafe_deserialization(serialized_data)
    print(f"Deserialized data: {data}")

    filename = input("Enter the file name to download: ")
    file_content = insecure_file_download(filename)
    print("File content downloaded.")

if __name__ == "__main__":
    main()


