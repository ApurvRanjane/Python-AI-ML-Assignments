# Q5: Write a program that accepts a directory name from the user
# and counts the number of files inside it every five minutes.
#
# Store the result in DirectoryCountLog.txt.
#
# Each entry should contain:
# 1. Directory path
# 2. Number of files
# 3. Date and time

import os
import time
import datetime
import schedule
import sys

def DirectoryScanner(DirectoryPath):
    curr_time = datetime.datetime.now()
    filecount = 0

    for FoldrName,Subfolder,FileName in os.walk(DirectoryPath):

        for file in FileName:
            filecount = filecount+1

    fobj = open("DirectoryCountLog.txt","a")
    fobj.write(
    f"Directory Scanned : {DirectoryPath}\n"
    f"Total files : {filecount}\n"
    f"Scan Time : {curr_time.strftime('%d-%m-%Y %I:%M:%S %p')}\n"
)
    fobj.write("-" * 40 + "\n")
    fobj.close()

def main():
    schedule.every(5).seconds.do(DirectoryScanner,sys.argv[1])

    while(True):
        schedule.run_pending()
        time.sleep(1)

if __name__ == "__main__":
    main()
