#Q5: Write a program which accept file name and 1 word for search in file from user and check wheather that word present in file.

def main():
    file_name = input("Enter the name of file with extension: ")
    word = input("Enter the word which want to search in file: ")

    fobj = open(file_name,"r")
    data = fobj.read()

    if word in data:
        print(f"{word} is present in file..")
    else:
        print(f"{word} not present in file..")

    fobj.close()

if __name__=="__main__":
    main()