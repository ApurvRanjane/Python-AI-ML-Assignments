# Q4: Write a program that creates a new log file after every ten minutes.
#
# Requirements:
# 1. The filename should contain the current date and time.
# 2. Display a message indicating the log file was created successfully.
# 3. Display the creation time.

import schedule
import time


def LogFileMaker():
    timestamp = time.ctime()
    LogFileName = "MarvellousLog%s.txt"%(timestamp)
    LogFileName = LogFileName.replace(" ","_")
    LogFileName = LogFileName.replace(":","_")

    fobj = open(LogFileName,"w")
    fobj.write(f"Log file created Successfully..\n Creation time: {timestamp}")

def main():
    schedule.every(10).minutes.do(LogFileMaker)

    while(True):
        schedule.run_pending()
        time.sleep(1)

if __name__=="__main__":
    main()
