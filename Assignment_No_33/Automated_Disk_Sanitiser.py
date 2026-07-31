##################################################################
#
#Importing Required Libraries
#
##################################################################

import sys
import os
import hashlib
import schedule
import time
import smtplib
from email.message import EmailMessage
from datetime import datetime

##################################################################
#
# Function Name : send_mail
# Input         : sender, app_password, receiver, subject, body
# Output        : None
# Description   : Sends an email containing the generated log report
# Author        : Apurv Ranjane
# Date          : 27/07/2026
#
##################################################################

def send_mail(sender,app_password,reciever,subject,body):

    msg = EmailMessage()
    msg["From"] = sender
    msg["To"] = reciever
    msg["Subject"] = subject

    msg.set_content(body)

    smtp = smtplib.SMTP_SSL("smtp.gmail.com",465)

    smtp.login(sender,app_password)

    smtp.send_message(msg)

    smtp.quit()

##################################################################
#
# Function Name : CalculateChecksum
# Input         : FileName
# Output        : MD5 Checksum
# Description   : Calculates and returns the MD5 checksum
#                 of the specified file.
# Author        : Apurv Ranjane
# Date          : 27/07/2026
#
##################################################################

def CalculateChecksum(FileName):
    fobj = open(FileName,"rb")

    hobj = hashlib.md5()

    Buffer = fobj.read(1024)

    while(len(Buffer) > 0):
        hobj.update(Buffer)
        Buffer = fobj.read(1024)
    
    fobj.close()

    ret = hobj.hexdigest()
    return ret

##################################################################
#
# Function Name : FindDuplicate
# Input         : DirectoryName
# Output        : Dictionary
# Description   : Scans the specified directory recursively and
#                 identifies duplicate files using their MD5
#                 checksum. Returns a dictionary containing
#                 checksum as key and list of duplicate file
#                 paths as value.
# Author        : Apurv Ranjane
# Date          : 27/07/2026
#
##################################################################

def FindDuplicate(DirectoryName):
    ret = False

    ret = os.path.exists(DirectoryName)
    if(ret == False):
        print("Path is invalid..")
        return

    ret = os.path.isdir(DirectoryName)
    if(ret == False):
        print("It is not directory..")
        return

    Duplicate = {}

    for FolderName,SubFolder,FileName in os.walk(DirectoryName):
        for fname in FileName:
            fname = os.path.join(FolderName,fname)
            checksum = CalculateChecksum(fname)

            if checksum in Duplicate:
                Duplicate[checksum].append(fname)
                
            else:
                Duplicate[checksum] = [fname]

    return Duplicate

##################################################################
#
# Function Name : DeleteDuplicate
# Input         : DirectoryName, FolderName
# Output        : None
# Description   : Detects and deletes duplicate files from the
#                 specified directory, generates a log report,
#                 records execution details, and sends the log
#                 report to the specified email address.
# Author        : Apurv Ranjane
# Date          : 27/07/2026
#
##################################################################

def DeleteDuplicate(DirectoryName,FolderName):
    start_time = time.time()
    start_datetime = datetime.now()

    timestamp = time.ctime()
    LogFileName = "AutomatedDiskSanitiser%s.log"%(timestamp)
    LogFileName = LogFileName.replace(" ","_")
    LogFileName = LogFileName.replace(":","_")

    Ret = False
    
    Ret = os.path.exists(FolderName)
    
    if(Ret == True):
        Ret = os.path.isdir(FolderName)
        if(Ret == False):
            print("Unable to proceed as directory name is existing but its not a directory..")
            return
            
    else:
        os.mkdir(FolderName)
        print("Directory for log file gets created successfully...")

    LogFileName = os.path.join(FolderName,LogFileName)

    fobj = open(LogFileName,"w")
    fobj.write("=" * 70 + "\n")
    fobj.write("          Automated Disk Sanitiser Log Report\n")
    fobj.write("=" * 70 + "\n\n")

    MyDict = FindDuplicate(DirectoryName)

    Result = list(filter(lambda x: len(x)>1,MyDict.values()))

    count = 0
    TotalFiles = 0
    TotalDeleted = 0

    for value in Result:
        for subvalue in value:
            count = count + 1
            TotalFiles = TotalFiles+1
            if(count>1):
                fobj.write(f"File name: {subvalue} has been deleted..\n")
                os.remove(subvalue)
                TotalDeleted = TotalDeleted + 1
        count = 0

    End_time = time.time()
    end_datetime = datetime.now()
    
    Time_Interval = End_time - start_time
    fobj.write(f"Start Time              : {start_datetime}\n")
    fobj.write(f"End Time                : {end_datetime}\n")
    fobj.write(f"Total Scanned files are : {TotalFiles}\n")
    fobj.write(f"Total deleted files are : {TotalDeleted}\n")
    fobj.write(f"The total time interval for this operation is: {Time_Interval:.6f} seconds\n")
    fobj.write(f"-"*100)
    fobj.close()

    # Send mail
    fobj = open(LogFileName,"r")
    Data = fobj.read()
    fobj.close()

    sender = "your_email@gmail.com"
    app_password = "your_16_character_app_password"
    receiver = sys.argv[4]
    subject = "Duplicate File Deletion Report"
    body = Data

    send_mail(sender, app_password, receiver, subject, body)
    print("Mail sent successfully..")

##################################################################
#
# Function Name : main
# Input         : Command-line arguments
# Output        : None
# Description   : Validates command-line arguments, displays
#                 help and usage information, schedules the
#                 duplicate file deletion task, and executes
#                 it periodically based on the specified time
#                 interval.
# Author        : Apurv Ranjane
# Date          : 27/07/2026
#
##################################################################

def main():

        if len(sys.argv) == 2:

            if sys.argv[1] == "--h":
                print("Help : This application deletes duplicate files from the specified directory.")
                print("Usage : python DirectoryChecksumDeleteFinal.py <DirectoryName> <TimeInMinutes> <LogFolder> <ReceiverEmail>")
                return

            elif sys.argv[1] == "--u":
                print("python DirectoryChecksumDeleteFinal.py Demo 5 Logs abc@gmail.com")
                print("Demo           -> Directory name")
                print("5              -> Time interval in minutes")
                print("Logs           -> Log folder")
                print("abc@gmail.com  -> Receiver email")
                return

        if len(sys.argv) != 5:
            print("Invalid number of arguments")
            print("Usage : python DirectoryChecksumDeleteFinal.py <DirectoryName> <TimeInMinutes> <LogFolder> <ReceiverEmail>")
            return

        try:
            interval = int(sys.argv[2])
        except ValueError:
            print("Time interval must be an integer.")
            return

        schedule.every(interval).minutes.do(DeleteDuplicate, sys.argv[1] , sys.argv[3])

        while True:
            schedule.run_pending()
            time.sleep(1)

##################################################################
#
#Starter of automation script
#
##################################################################
    
if __name__=="__main__":
    main()
