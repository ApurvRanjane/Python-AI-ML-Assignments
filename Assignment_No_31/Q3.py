# Q3: Write a program that scans a specified directory every minute.
#
# The task should display:
# 1. Directory name
# 2. Number of files
# 3. Number of subdirectories
# 4. Date and time of scanning
#
# Use the os module.

import os
import time
import datetime
import schedule
import sys

def DirectoryScanner(DirectoryPath):
    curr_time = datetime.datetime.now()
    subfcount = 0
    filecount = 0
    print(f"Directory Scanned : {DirectoryPath}")

    for FoldrName,Subfolder,FileName in os.walk(DirectoryPath):

        for subf in Subfolder:
            subfcount = subfcount+1

        for file in FileName:
            filecount = filecount+1

    print(f"Total files: {filecount}")
    print(f"Total Subdirectories: {subfcount}")
    print(f"Scan time: ",curr_time.strftime("%d-%m-%Y %I:%M:%S %p"))


def main():
    schedule.every(1).minute.do(DirectoryScanner,sys.argv[1])

    while(True):
        schedule.run_pending()
        time.sleep(1)

if __name__ == "__main__":
    main()
