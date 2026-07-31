# ---------------------------------------------------------------
# Q: Write a Python program that performs automatic file backup.
#
# Requirements:
# 1. Accept the source file path from the command line.
# 2. Accept the destination directory path from the command line.
# 3. Check whether the source file exists.
# 4. Create the destination directory if it does not exist.
# 5. Copy the source file to the destination directory.
# 6. Rename the backup file by appending the current date and time
#    to the original filename.
# 7. Log each successful backup operation into 'backup_log.txt'.
# 8. Schedule the backup to run automatically every hour.
#
# Example:
# Original File:
#   Data.txt
#
# Backup Files:
#   Data_24_07_2026_10_30_00.txt
#   Data_24_07_2026_11_30_00.txt
#
# Log File:
#   backup_log.txt
# ---------------------------------------------------------------

import sys
import time
import os
import schedule
import datetime
import shutil

def BackupFactory(SourceFilePath,DestinationDirePath):
    try:
        if (os.path.isfile(SourceFilePath)== False):
            print("Source file does not exist..")
            return

        os.makedirs(DestinationDirePath,exist_ok=True)

        fillename = os.path.basename(SourceFilePath)
        name,ext = os.path.splitext(fillename)

        current_time = datetime.datetime.now()

        backup_filename = f"{name}_{current_time.strftime('%d_%m_%Y_%H_%M_%S')}{ext}"

        backup_path = os.path.join(DestinationDirePath,backup_filename)

        shutil.copy2(SourceFilePath,backup_path)

        log_entry = f"Backup completed successfully at {current_time.strftime('%d-%m-%Y %I:%M:%S %p')}\n"

        fobj = open("backup_log.txt","a")
        fobj.write(log_entry)
        fobj.close()

    except Exception as e:
        print("Error :", e)


def main():
    if(len(sys.argv)==3):
        schedule.every(1).hour.do(BackupFactory,sys.argv[1],sys.argv[2])

        while(True):
            schedule.run_pending()
            time.sleep(1)

    else:
        print("Invalid command line arguments..")
        

if __name__ == "__main__":
    main()