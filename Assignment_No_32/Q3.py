# Q3: Write a program that reads and displays the contents of a
# specified text file every minute.
#
# Requirements:
# 1. Handle file does not exist.
# 2. Handle empty file.
# 3. Handle permission denied.
# 4. Handle file cannot be opened.

import schedule
import time
import datetime
import os
import sys

def FileSizeReader(FilePath):
    try:
        if (os.path.exists(FilePath) == False):
            print("File not exist..")
            return

        elif(os.path.getsize(FilePath) == 0):
            print("File is empty...")
            return
        
        else:
            filename =  os.path.basename(FilePath)
            fobj = open(FilePath,"r")
            data = fobj.read()
            print(f"Data in file is: {data}")
            fobj.close()

    except PermissionError:
        print("Error: Permission denied.")

    except FileNotFoundError:
        print("Error: File not found.")

    except OSError as e:
        print(f"OS Error: {e}")

    except Exception as e:
        print(f"Unexpected Error: {e}")
        

def main():
     if len(sys.argv) != 2:
        print("Usage : python FileReader.py <FilePath>")
        return

     schedule.every(10).seconds.do(FileSizeReader, sys.argv[1])

     while True:
        schedule.run_pending()
        time.sleep(1)

if __name__ == "__main__":
    main()