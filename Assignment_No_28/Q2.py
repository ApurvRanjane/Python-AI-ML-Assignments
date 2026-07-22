#Q2: Write a program which accept file name from user and count words in that file.

def main():
    file_name = input("Enter the name of file with extension: ")
    fobj = open(file_name,"r")
    file_data = fobj.read()
    words = file_data.split()
    word_count = len(words)
    fobj.close()
    print("The number of words present in file are: ",word_count)

if __name__=="__main__":
    main()