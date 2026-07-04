#Q10 : Write a lambda function using filter(), which accepts one list of numbers and returns count of even numbers.
EvenChecker = lambda a: a%2==0 

def List_Maker(size):
    List = []
    for i in range(size):
        print("Enter Number",i+1,":")
        value = int(input())
        List.append(value)
    return List

def main():
    size = int(input("Enter size of list : "))
    ret = List_Maker(size)
    result = list(filter(EvenChecker,ret))
    length = len(result)
    print("The list before filter operation : ",ret)
    print("The list after filter operation : ",result)
    print("The count of even numbers is : ",length)

if(__name__=="__main__"):
    main()

