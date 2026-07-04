#Q9 : Write a program of lambda function which accept two number and return multiplication of numbers.

Multiplication = lambda a,b: a*b

def main():
    value1 = int(input("Enter number1 : "))
    value2 = int(input("Enter number2 : "))
    ret = Multiplication(value1,value2)
    print("Multiplication of numbers is  : ",ret)

if(__name__=="__main__"):
    main()
    