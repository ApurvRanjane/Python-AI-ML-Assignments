import sys

def main():
    print("-----------------------------------------------------------------")
    print("Marvellous Automation Script")
    print("-----------------------------------------------------------------")

    if(len(sys.argv)==2):
        if(sys.argv[1]=="--h" or sys.argv[1]=="--H"):
            print("This automation script used to traverse the directory..")
            print("for better usage please check --u flag")

        elif(sys.argv[1]=="--u" or sys.argv[1]=="--U"):
            print("Please execute script as: ")
            print("python filename.py directoryname")
            print("Directory name should be absolute path")
            
        else:
            DirectoryName = sys.argv[1]
            print("Directory name is: ",DirectoryName)
        
    else:
        print("Invalid number of arguments.")
        print("Please use --h or --u for more information..")
    
    print("-----------------------------------------------------------------")
    print("Thank you for using Marvellous Automation Script")
    print("-----------------------------------------------------------------")

    
if __name__=="__main__":
    main()
