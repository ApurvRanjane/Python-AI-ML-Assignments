# Q1: Write a Python program that prints:
# "Jay Ganesh..."
# every two seconds.
#
# Use:
# schedule.every(2).seconds.do(...)

import schedule
import time

def PrintFactory():
    print("Jay Ganesh...")

def main():
    schedule.every(2).seconds.do(PrintFactory)

    while(True):
        schedule.run_pending()
        time.sleep(1)

if __name__ =="__main__":
    main()