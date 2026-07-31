# Q4: Create a task that executes every day at 9:00 AM and prints:
# "Namaskar..."
#
# Use:
# schedule.every().day.at("09:00").do(...)

import schedule
import time
import datetime

def Greetings():
    print("Namaskar")

def main():
    schedule.every(1).day.at("9:00").do(Greetings)

    while(True):
        schedule.run_pending()
        time.sleep(1)

if __name__ =="__main__":
    main()