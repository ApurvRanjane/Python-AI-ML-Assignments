#Q9: Write a program which accepet name from user and display its length.

def length_name(name):
    count = len(name)
    return count

def main():
    value = input("Enter the name : ")
    ret = length_name(value)
    print(f"The length of name is : {ret}")


if(__name__=="__main__"):
    main()
 