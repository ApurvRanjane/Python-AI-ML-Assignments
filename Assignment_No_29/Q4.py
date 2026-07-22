#Q4: Write a program which accept 2 file names from command line and comapre content of both files if it same display success else fails.
import sys

def main():
    file_name1 = sys.argv[1]
    file_name2 = sys.argv[2]

    fobj1 = open(file_name1,"r")
    fobj2 = open(file_name2,"r")

    data1 = fobj1.read()
    data2 = fobj2.read()

    if(data1 == data2):
        print("Success,Both files have same content...")
    else:
        print("Fail, files not contain same content...")

    fobj1.close()
    fobj2.close()

if __name__=="__main__":
    main()