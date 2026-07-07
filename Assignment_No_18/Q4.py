#Q4: Write a program which accept N numbers from user and stored it into list and accept one number and give its frequency in that list.

def ListFrequency(List,element):
    count = 0
    for i in List:
        if i==element:
            count = count +1
    return count

def main():
    List = []
    No = int(input("Enter the number of elements you want to insert in list : "))
    for i in range(No):
        num = int(input("Enter element in list : "))
        List.append(num)
    element = int(input("Enter the number for frquency checking : "))
    ret = ListFrequency(List,element)
    print(f"The frquency of {element} in the list is: {ret}")

if(__name__=="__main__"):
    main()

