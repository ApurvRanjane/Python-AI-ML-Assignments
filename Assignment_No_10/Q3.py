#Q3: Write a program which accept one number and prints factorial of that number.

def Factorial(No):
    mul = 1
    for i in range(1,No+1):
        mul = mul * i
    return mul


def main():
    value = int(input("Enter Number : "))
    ret = Factorial(value)
    print("The Factorial of ",value," is : ",ret)

if(__name__=="__main__"):
    main()