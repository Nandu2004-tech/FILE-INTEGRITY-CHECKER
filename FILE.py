import os
import hashlib


# Function to calculate SHA-256 hash of a file
def calculate_sha256(file_path):
    sha256_hash = hashlib.sha256()
    try:
        with open(file_path, "rb") as f:
            while True:
                data = f.read(65536)  # Read file in chunks
                if not data:
                    break
                sha256_hash.update(data)
        return sha256_hash.hexdigest()
    except FileNotFoundError:
        print(f"Error: File '{file_path}' not found.")
        return None
    except PermissionError:
        print(f"Error: Permission denied for file '{file_path}'.")
        return None
    except Exception as e:
        print(f"Unexpected error with file '{file_path}': {e}")
        return None


# Function to check integrity of all files in a directory
def check_integrity(directory_path):
    if not os.path.exists(directory_path) or not os.path.isdir(directory_path):
        print(f"Error: Directory '{directory_path}' does not exist.")
        return

    for root, dirs, files in os.walk(directory_path):
        for file_name in files:
            file_path = os.path.join(root, file_name)
            calculated_hash = calculate_sha256(file_path)
            if calculated_hash:
                print(f"File: {file_path}\nSHA-256 Hash: {calculated_hash}\n")


# Main Execution
if __name__ == "__main__":
    directory_to_check = input("Enter the directory path to check integrity: ")
    check_integrity(directory_to_check)
