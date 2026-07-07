#Q10: Write a program which accept one number and return its addition of digits

def DigitAddition(No):
    ans = 0
    while(No > 0):
       last = No % 10
       ans = ans +last
       No = No // 10
    return ans

def main():
    value = int(input("Enter the number : "))
    ret = DigitAddition(value)
    print(f"The sum of digits in the {value} are : {ret}")

if(__name__=="__main__"):
    main()
 