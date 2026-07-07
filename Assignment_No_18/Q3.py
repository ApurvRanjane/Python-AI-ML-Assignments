#Q3: Write a program which accept N numbers from user and stored it into list and return minimum number in that list.

def ListMaximum(List):
    min = 100000000000000
    for i in List:
        if i < min:
            min = i
    return min

def main():
    List = []
    No = int(input("Enter the number of elements you want to insert in list : "))
    for i in range(No):
        num = int(input("Enter element in list : "))
        List.append(num)
    ret = ListMaximum(List)
    print(f"The minimum number in the list is: {ret}")

if(__name__=="__main__"):
    main()

