#Q4: Write a program which accept one number and return its addition of factors

def FactorAddition(No):
    ans = 0
    for i in range(1,No):
        if(No % i == 0):
            ans = ans + i
    return ans

def main():
    value = int(input("Enter the number : "))
    ret = FactorAddition(value)
    print(f"The Addition of factors of {value} is : {ret}")

if(__name__=="__main__"):
    main()
 