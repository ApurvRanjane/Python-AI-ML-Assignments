#Q4: Write a program which accept 2 file names from user and copy data of 1st file in seond file which is new file.

def main():
    Source_file = input("Enter the name of Source file with extension: ")
    Destination_file = input("Enter the name of Destination file with extension: ")

    fobj1 = open(Source_file,"r")
    fobj2 = open(Destination_file,"w")
    
    file_data = fobj1.read()
    fobj2.write(file_data)

    print(f"{Source_file} data copied into {Destination_file}...")

    fobj1.close()
    fobj2.close()

if __name__=="__main__":
    main()