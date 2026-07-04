#Q1 : Write a lambda function using map(), which accepts one list of numbers and returns list of square of each number.
square = lambda a: a*a

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
    result = list(map(square,ret))
    print("The list before map operation(squaring each element): ",ret)
    print("The list after map operation(squaring each element): ",result)

if(__name__=="__main__"):
    main()

