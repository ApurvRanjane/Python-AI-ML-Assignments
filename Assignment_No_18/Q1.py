#Q1: Write a program which accept N numbers from user and stored it into list and return addition of all elements in that list.

def ListAddition(List):
    ans = 0
    for i in List:
        ans = ans+i
    return ans

def main():
    List = []
    No = int(input("Enter the number of elements you want to insert in list : "))
    for i in range(No):
        num = int(input("Enter element in list : "))
        List.append(num)
    ret = ListAddition(List)
    print(f"The addition of elements in list is: {ret}")

if(__name__=="__main__"):
    main()

