#Q8 : Write a program of lambda function which accept two number and return addition of numbers.

Summation = lambda a,b: a+b

def main():
    value1 = int(input("Enter number1 : "))
    value2 = int(input("Enter number2 : "))
    ret = Summation(value1,value2)
    print("Addition of numbers is  : ",ret)

if(__name__=="__main__"):
    main()
    