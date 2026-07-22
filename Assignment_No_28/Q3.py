#Q3: Write a program which accept file name from user and Display it line by line on screen.

def main():
    file_name = input("Enter the name of file with extension: ")
    fobj = open(file_name,"r")
    
    for line in fobj:
        print(line,end = "")

    fobj.close()

if __name__=="__main__":
    main()