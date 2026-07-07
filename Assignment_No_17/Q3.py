#Q3: Write a program which accept one number and return its factorial

def Factorial(No):
    ans = 1
    for i in range(1,No+1):
        ans = ans*i
    return ans

def main():
    value = int(input("Enter the number : "))
    ret = Factorial(value)
    print(f"The factorial of {value} is : {ret}")

if(__name__=="__main__"):
    main()
 