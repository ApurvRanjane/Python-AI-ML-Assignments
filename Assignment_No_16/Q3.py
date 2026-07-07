#Q3 : Write a program which conatins function named as Add(), which accept 2  numbers from user and return addition of that numbers.

def Add(number1,number2):
    sum = number1 + number2
    return sum
    
def main():
    num1 = int(input("Enter Number1 : "))
    num2 = int(input("Enter Number2 : "))
    ret = Add(num1,num2)
    
    print("The addition of ",num1," and ",num2," is : ",ret)

if(__name__=="__main__"):
    main()