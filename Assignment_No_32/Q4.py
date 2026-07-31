# Q4: Write a program that copies all .txt files from one directory
# to another every ten minutes.
#
# Requirements:
# 1. Accept source and destination directories.
# 2. Validate both directories.
# 3. Copy only .txt files.
# 4. Maintain a log of copied files.
# 5. Avoid terminating if one file cannot be copied.

import os
import shutil
import time
from datetime import datetime


def copy_txt_files(source, destination):
    log_file = "copy_log.txt"

    for file in os.listdir(source):
        if file.endswith(".txt"):
            source_path = os.path.join(source, file)
            destination_path = os.path.join(destination, file)

            try:
                shutil.copy2(source_path, destination_path)

                with open(log_file, "a") as log:
                    log.write(f"{datetime.now()} : Copied -> {file}\n")

                print(file, "copied successfully.")

            except Exception as e:
                print("Could not copy", file)
                print(e)


def main():
    source = input("Enter Source Directory: ")
    destination = input("Enter Destination Directory: ")

    if not os.path.isdir(source):
        print("Source directory is invalid.")
        return

    if not os.path.isdir(destination):
        print("Destination directory is invalid.")
        return

    while True:
        print("\nChecking for .txt files...")
        copy_txt_files(source, destination)
        print("Waiting for 10 minutes...\n")
        time.sleep(600)   # 10 minutes


if __name__ == "__main__":
    main()