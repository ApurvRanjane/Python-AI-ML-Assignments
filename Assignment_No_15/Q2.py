#Q2 : Write a lambda function using filter(), which accepts one list of numbers and returns list of even numbers.
even = lambda a: a%2==0

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
    result = list(filter(even,ret))
    print("The list before filter operation : ",ret)
    print("The list after filter operation : ",result)

if(__name__=="__main__"):
    main()

