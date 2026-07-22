#Q5: Write a program which accept file name and string from user and return frequency of that string in file..

def main():
    file_name = input("Enter the name of file with extension: ")
    word = input("Enter the word for frequency checking..")

    fobj = open(file_name,"r")
    data = fobj.read()

    words = data.split()
    frequency = words.count(word)

    print(f"The frequency of {word} in file is: {frequency}")
    fobj.close()

if __name__=="__main__":
    main()