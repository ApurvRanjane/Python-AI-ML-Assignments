# Q5: Schedule a task that executes every five minutes.
#
# The task should write the current date and time into a file named
# "Marvellous.txt".
#
# New entries should be appended without removing previous entries.

import schedule
import time
import datetime

def TaskScheduler():
    print(f"The task executed at : {datetime.datetime.now().strftime("%d-%m-%Y %I:%M:%S %p")}")

def main():
    schedule.every(5).minutes.do(TaskScheduler)

    while(True):
        schedule.run_pending()
        time.sleep(1)

if __name__ =="__main__":
    main()