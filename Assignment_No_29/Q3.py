#Q3: Write a program which accept file name from command line and creates new file Demo.txt and copies all data of that file in Demo.txt
import sys

def main():
    file_name = sys.argv[1]
    fobj1 = open(file_name,"r")
    fobj2 = open("Demo.txt","w")

    data = fobj1.read()
    fobj2.write(data)

    print("Data is copy from",file_name," to Demo.txt....")

    fobj1.close()
    fobj2.close()

if __name__=="__main__":
    main()