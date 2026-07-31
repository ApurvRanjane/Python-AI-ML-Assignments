# Q6: Write a program that schedules the following messages:
#
# Monday at 9:00 AM  : Start your weekly goals
# Wednesday at 5:00 PM : Review your weekly progress
# Friday at 6:00 PM : Weekly work completed
#
# Use:
# schedule.every().monday.at(...)
# schedule.every().wednesday.at(...)
# schedule.every().friday.at(...)

import schedule
import time

def MondayTask():
    print(f"Start your weekly goals..")

def WednesdayTask():
    print(f"Review your weekly progress..")

def FridayTask():
    print(f"Weekly work completd..")

def main():
    schedule.every().monday.at("9:00").do(MondayTask)
    schedule.every().wednesday.at("17:00").do(WednesdayTask)
    schedule.every().friday.at("18:00").do(FridayTask)

    while(True):
        schedule.run_pending()
        time.sleep(1)

if __name__=="__main__":
    main()
