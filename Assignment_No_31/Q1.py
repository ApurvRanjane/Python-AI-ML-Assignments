# Q1: Write a program that accepts:
# 1. A message from the user.
# 2. A time interval in seconds.
# Schedule the program to display the message repeatedly after the specified interval.
# Validate that the interval is greater than zero.

import schedule
import time
import sys

msg = sys.argv[1]
interval = int(sys.argv[2])

def msgPrinter():
    print(msg)

def main():
    schedule.every(interval).seconds.do(msgPrinter)

    while(True):
        schedule.run_pending()
        time.sleep(1)

if __name__=="__main__":
    main()
