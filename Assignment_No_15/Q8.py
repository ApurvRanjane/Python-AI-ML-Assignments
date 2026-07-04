#Q8 : Write a lambda function using filter(), which accepts one list of numbers and returns list of numbers divisible by 3 and 5.
Checker = lambda a: a%3==0 and a%5==0

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
    result = list(filter(Checker,ret))
    print("The list before filter operation : ",ret)
    print("The list after filter operation : ",result)

if(__name__=="__main__"):
    main()

