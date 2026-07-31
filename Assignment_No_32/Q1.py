# Q1: Write a program that creates a new text file every minute.
#
# Requirements:
# 1. The filename should contain the current timestamp.
# 2. Write the following information into the file:
#    - Filename
#    - Creation Date
#    - Creation Time


import schedule
import time
import datetime

def FileMaker():
    now = datetime.datetime.now()

    timestamp = now.strftime("%a_%b_%d_%H_%M_%S_%Y")
    LogFileName = f"File_{timestamp}.txt"

    with open(LogFileName, "w") as fobj:
        fobj.write(f"File Name      : {LogFileName}\n")
        fobj.write(f"Creation Date  : {now.strftime('%d-%m-%Y')}\n")
        fobj.write(f"Creation Time  : {now.strftime('%H:%M:%S')}\n")
        fobj.write(f"-"*40)

    print(f"{LogFileName} created successfully.")

def main():
    schedule.every(10).seconds.do(FileMaker)

    while True:
        schedule.run_pending()
        time.sleep(1)

if __name__ == "__main__":
    main()