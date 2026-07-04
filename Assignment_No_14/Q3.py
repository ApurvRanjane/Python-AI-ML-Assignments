#Q3 : Write a program of lambda function which accept two number and return maximum number.

maximum = lambda a,b: a if (a>b) else b

def main():
    value1 = int(input("Enter number1 : "))
    value2 = int(input("Enter number2 : "))
    ret = maximum(value1,value2)
    print("Maximum number from both numbers is  : ",ret)

if(__name__=="__main__"):
    main()
    