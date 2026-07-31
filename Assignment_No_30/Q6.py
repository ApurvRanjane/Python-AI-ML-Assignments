# Q6: Write a script that schedules the following tasks:
#
# 1. Print "Lunch Time!" every day at 1:00 PM.
# 2. Print "Wrap up work" every day at 5:00 PM.
#
# Both tasks should be handled by separate functions.

import schedule
import time

def LunchRemainder():
    print("It's Lunch time..")

def OfficeLeaveRemainder():
    print("Wrap up work..")

def main():
    schedule.every(1).day.at("13:00").do(LunchRemainder)
    schedule.every(1).day.at("18:00").do(OfficeLeaveRemainder)

    while(True):
        schedule.run_pending()
        time.sleep(1)

if __name__ =="__main__":
    main()