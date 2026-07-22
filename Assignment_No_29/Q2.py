#Q2: Write a program which accept file name from user and open that file and display all contents in that file on console.


def main():
    file_name = input("Enter the name of file with extension: ")
    
    fobj = open(file_name,"r")
    data = fobj.read()

    print(data)
    fobj.close()

if __name__=="__main__":
    main()