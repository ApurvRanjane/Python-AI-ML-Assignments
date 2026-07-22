#Q1: Write a program which accept file name from user and check wheather that file present in current directory or not.
import os

def main():
    file_name = input("Enter the name of file with extension: ")
    
    ret = os.path.exists(file_name)

    if(ret):
        print(f"{file_name} is present in current directory..")
    else:
        print(f"{file_name} is not present in current directory..")

if __name__=="__main__":
    main()