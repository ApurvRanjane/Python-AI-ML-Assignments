#Q7 : Write a lambda function using filter(), which accepts one list of strings and returns list of strings whose length greater than 5.
StringChecker = lambda a: len(a)>5

def List_Maker(size):
    List = []
    for i in range(size):
        print("Enter string",i+1,":")
        value = input()
        List.append(value)
    return List

def main():
    size = int(input("Enter size of list : "))
    ret = List_Maker(size)
    result = list(filter(StringChecker,ret))
    print("The list before filter operation : ",ret)
    print("The list after filter operation : ",result)

if(__name__=="__main__"):
    main()

