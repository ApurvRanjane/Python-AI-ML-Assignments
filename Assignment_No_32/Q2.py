# Q2: Write a Python program that monitors the size of a specified
# file every 30 seconds.
#
# Requirements:
# 1. Store details in FileSizeLog.txt
# 2. File path
# 3. File size in bytes
# 4. Date and Time
# 5. Handle file not found.

import schedule
import time
import datetime
import os
import sys

def FileSizeChecker(FilePath):
    if (os.path.exists(FilePath) == False):
        print("File not exist..")
        return

    else:
        filename =  os.path.basename(FilePath)
        print(f"File name: {filename} : {os.path.getsize(FilePath)}bytes")
        

def main():
    schedule.every(10).seconds.do(FileSizeChecker,sys.argv[1])

    while True:
        schedule.run_pending()
        time.sleep(1)

if __name__ == "__main__":
    main()