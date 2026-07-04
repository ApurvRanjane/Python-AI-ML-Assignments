#6 : Write a lambda function using reduce(), which accepts one list of numbers and returns minimum element in list.

from functools import reduce

Minimum = lambda a,b: a if a<b else b

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
    result = reduce(Minimum,ret)
    print("The list before reduce operation : ",ret)
    print(" Result of reduce operation : ",result)

if(__name__=="__main__"):
    main()

