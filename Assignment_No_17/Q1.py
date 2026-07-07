#Q1: Write a program which import functions from Arithmetic_Module.py for Add,Sub,Mul,Div:

import Arithmetic_Module

def main():
    num1 = int(input("Enter number 1: "))
    num2 = int(input("Enter number 2: "))
    ret = Arithmetic_Module.Add(num1,num2)
    print(f"The addition of {num1} and {num2} is {ret}")
    print(f"The Substraction of {num1} and {num2} is {Arithmetic_Module.Sub(num1,num2)}")
    print(f"The Multiplication of {num1} and {num2} is {Arithmetic_Module.Mul(num1,num2)}")
    print(f"The Division of {num1} and {num2} is {Arithmetic_Module.Div(num1,num2)}")

if(__name__=="__main__"):
    main()
 