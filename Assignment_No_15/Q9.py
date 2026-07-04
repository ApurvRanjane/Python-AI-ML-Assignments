#Q9 : Write a lambda function using reduce(), which accepts one list of numbers and returns product of numbers in list.

from functools import reduce

Mutiplication = lambda a,b: a*b

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
    result = reduce(Mutiplication,ret)
    print("The list before reduce operation : ",ret)
    print(" Result of reduce operation : ",result)

if(__name__=="__main__"):
    main()

