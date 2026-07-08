#Q2 : Write a program which conatin one lambda function which accept two numbers and return its multiplication.

Multiplication = lambda a,b:(a * b)

def main():
    value1 = int(input("Enter the number1 : "))
    value2 = int(input("Enter the number2 : "))
    ret = Multiplication(value1,value2)
    print(f"The multiplication of {value1} and {value2} is : {ret}")

if(__name__=="__main__"):
    main()
    