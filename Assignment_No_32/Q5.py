# Q5: Write a program that deletes all empty files from a specified
# directory every hour.
#
# Requirements:
# 1. Scan the directory recursively.
# 2. Detect files whose size is zero bytes.
# 3. Delete the empty files.
# 4. Store deleted file paths in a log file.
# 5. Handle permission errors.

import os
import time
from datetime import datetime


def delete_empty_files(directory):
    log_file = "delete_log.txt"

    for root, dirs, files in os.walk(directory):
        for file in files:
            file_path = os.path.join(root, file)

            try:
                if os.path.getsize(file_path) == 0:
                    os.remove(file_path)

                    with open(log_file, "a") as log:
                        log.write(f"{datetime.now()} : Deleted -> {file_path}\n")

                    print(file_path, "deleted.")

            except PermissionError:
                print("Permission Denied:", file_path)

            except Exception as e:
                print("Error:", e)


def main():
    directory = input("Enter Directory Path: ")

    if not os.path.isdir(directory):
        print("Invalid Directory.")
        return

    while True:
        print("\nScanning for empty files...")
        delete_empty_files(directory)
        print("Waiting for 1 hour...\n")
        time.sleep(3600)   # 1 hour


if __name__ == "__main__":
    main()