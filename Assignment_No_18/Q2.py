#Q2: Write a program which accept N numbers from user and stored it into list and return maximum number in that list.

def ListMaximum(List):
    max = -1
    for i in List:
        if i > max:
            max = i
    return max

def main():
    List = []
    No = int(input("Enter the number of elements you want to insert in list : "))
    for i in range(No):
        num = int(input("Enter element in list : "))
        List.append(num)
    ret = ListMaximum(List)
    print(f"The maximum number in the list is: {ret}")

if(__name__=="__main__"):
    main()

