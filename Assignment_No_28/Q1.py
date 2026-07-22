#Q1: Write a program which accept file name from user and count lines in that file.

def main():
    file_name = input("Enter the name of file with extension: ")
    fobj = open(file_name,"r")
    file_lines = len(fobj.readlines())
    print("The number of lines present in file are: ",file_lines)
    fobj.close()

if __name__=="__main__":
    main()