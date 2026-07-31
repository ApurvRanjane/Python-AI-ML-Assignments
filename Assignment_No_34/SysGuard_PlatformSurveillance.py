##################################################################
#
#Importing Required Libraries
#
##################################################################

import psutil
import sys
import os
import time
import schedule
import smtplib
from email.message import EmailMessage

##################################################################
#
# Function Name : send_mail
# Input         : sender, app_password, receiver, subject, body
# Output        : None
# Description   : Sends the generated log report to the specified
#                 receiver email using Gmail SMTP over SSL.
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
# Function Name : ProcessScan
# Input         : None
# Output        : listprocess
# Description   : Scans all running processes and collects their
#                 PID, name, username, status, CPU usage, and
#                 memory usage into a list.
# Author        : Apurv Ranjane
# Date          : 27/07/2026
#
##################################################################

def ProcessScan():
    listprocess = []
    for proc in psutil.process_iter():
        info = proc.as_dict(attrs=["pid","name","username","status"])
        info["cpu_percent"] = proc.cpu_percent(None)
        info["memory_percent"] = proc.memory_percent()
        
        listprocess.append(info)
    return listprocess

##################################################################
#
# Function Name : PlatformSurvillence
# Input         : FolderName
# Output        : None
# Description   : Creates a log file containing system information
#                 such as CPU usage, RAM usage, network statistics,
#                 and running process details. Saves the log in the
#                 specified folder and sends the generated report
#                 to the receiver through email.
# Author        : Apurv Ranjane
# Date          : 27/07/2026
#
##################################################################

def PlatformSurvillence(FolderName):
    Border = "-"*50
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

    timestamp = time.strftime("%Y-%m-%d_%H-%M-%S")
    filename = os.path.join(FolderName,"SysGuard_%s.log" %timestamp)
    fobj = open(filename,"w")
    print(f"log file gets successfully created with name: {filename}")

    Border1 = "=" * 80

    fobj.write(Border1 + "\n")
    fobj.write("               SysGuard – Automated Platform Surveillance System\n")
    fobj.write(Border1 + "\n")
    fobj.write("Log File Generated At : " + timestamp + "\n")
    fobj.write(Border1 + "\n\n")

    fobj.write("SYSTEM REPORT\n")
    fobj.write("-" * 80 + "\n")

    #CPU INFORMATION
    fobj.write("Number of CPU Cores: %s\n" %psutil.cpu_count())
    fobj.write("CPU Usage : %s %%\n" %psutil.cpu_percent())
    fobj.write(Border+"\n")

    #RAM INFORMATION
    memory = psutil.virtual_memory()
    fobj.write("RAM Usage : %s %%\n" %memory.percent)
    fobj.write("Total RAM available : %s\n" %memory.total)
    fobj.write(Border+"\n")

    #NETWORK USAGE
    netobj = psutil.net_io_counters()
    fobj.write("Network Usage Report\n")
    fobj.write("Sent : %.2f MB\n" %(netobj.bytes_sent/(1024*1024)))
    fobj.write("Recieve : %.2f MB\n" %(netobj.bytes_recv/(1024*1024)))

    #PROCESS LOG
    Data = ProcessScan()
    for info in Data:
        # fobj.write(f"{info}\n")
        fobj.write("PID: %s\n" %info.get("pid"))
        fobj.write("Name: %s\n" %info.get("name"))
        fobj.write("Username: %s\n" %info.get("username"))
        fobj.write("Status: %s\n" %info.get("status"))
        fobj.write("CPU Usage: %.4f\n" %info.get("cpu_percent"))
        fobj.write("RAM Usage: %.2f\n" %info.get("memory_percent"))
        fobj.write(Border+"\n")

    fobj.write(Border+"\n")
    fobj.write("-----------------End of Log file----------------")
    fobj.write(Border+"\n")
    fobj.close()

    #Mail Send
    sender = "your_email@gmail.com"
    app_password = "your_app_password"
    receiver = sys.argv[3]

    # Read log file
    fobj = open(filename, "r")
    body = fobj.read()
    fobj.close()

    subject = "Platform Surveillance Report"

    send_mail(sender, app_password, receiver, subject, body)

    print("Mail sent successfully...")

##################################################################
#
# Function Name : main
# Input         : Command Line Arguments
# Output        : None
# Description   : Acts as the entry point of the application.
#                 Validates command line arguments, displays help
#                 and usage information, schedules periodic system
#                 surveillance, and starts the automation process.
# Author        : Apurv Ranjane
# Date          : 27/07/2026
#
##################################################################

def main():

    Border = "-"*50
    print(Border)
    print("----------------SysGuard – Automated Platform Surveillance System----------------")
    print(Border)

    #--h and --u will be handling
    if(len(sys.argv)==2):
        if(sys.argv[1] == "--h" or sys.argv[1] == "--H"):
            print("SysGuard performs the following tasks:")
            print("1: It fetch the information of running process.")
            print("2: It fetch information about primary storage as RAM.")
            print("3: It fetch information about secondary storage as HDD.")
            print("4: It fetch information about microprocessor.")
            print("5: It gets scheduled periodically.")
            print("6: It maintains the all records in log file.")
            print("7: It sends the log files through mail periodically.")

        elif(sys.argv[1] == "--u" or sys.argv[1] == "--U"):
            print("Use the automation script as : ")
            print(f"python {sys.argv[0]} <Time_Interval> <Folder_Name> <Receiver_Email>")
            print("Time_Interval : Time in minutes for periodic execution")
            print("Folder_Name   : Name of folder for log file creation")
            print("Receiver_Email: Email address to receive the log report")

        else:
            print("Unable to proceed as ther is no matching arguments..")
            print("Please use --h or --u flag for getting more details..")

    #Actual project code
    elif(len(sys.argv)==4):
        # print("CPU Usage : ",psutil.cpu_percent())
        print("Scheduler started successfully.")
        print("Press Ctrl + C to stop SysGuard.")
        schedule.every(int(sys.argv[1])).minutes.do(PlatformSurvillence,sys.argv[2])

        while(True):
            schedule.run_pending()
            time.sleep(1)

    else:
        print("Invalid number of arguments")
        print("Unable to proceed as arguments are not matching..")
        print("Please use --h or --u flag for getting more details..")

    print(Border)
    print("Thank you for using SysGuard.")
    print(Border)

##################################################################
#
#Starter of automation script
#
##################################################################

if __name__ == "__main__":
    main()