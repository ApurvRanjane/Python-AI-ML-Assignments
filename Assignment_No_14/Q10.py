#Q10 : Write a program of lambda function which accept three numbers and return maximum number.

maximum = lambda a,b,c: a if (a>b and a>c) else b if (b>c and b>a) else c

def main():
    value1 = int(input("Enter number1 : "))
    value2 = int(input("Enter number2 : "))
    value3 = int(input("Enter number3 : "))
    ret = maximum(value1,value2,value3)
    print("Maximum number from 3 numbers is  : ",ret)

if(__name__=="__main__"):
    main()
    