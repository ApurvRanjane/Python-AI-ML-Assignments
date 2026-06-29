#Q2 : Write a program which accept two numbers and prints addition,substraction,multiplication and division.

def Addition(No1,No2):
    ans = No1 + No2
    return ans

def Substraction(No1,No2):
    ans = No1 - No2
    return ans

def Multiplication(No1,No2):
    ans = No1 * No2
    return ans

def Division(No1,No2):
    ans = No1 / No2
    return ans

def main():
    value1 = int(input("Enter Number1 : "))
    value2 = int(input("Enter Number2 : "))
    
    print("Addition of ",value1," and ",value2," is : ",Addition(value1,value2) )
    print("Substraction of ",value1," and ",value2," is : ",Substraction(value1,value2) )
    print("Multiplication of ",value1," and ",value2," is : ",Multiplication(value1,value2) )
    print("Division of ",value1," and ",value2," is : ",Division(value1,value2) )

if(__name__=="__main__"):
    main()