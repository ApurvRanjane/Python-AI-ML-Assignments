#Q9: Write a program which accept one number and return its number of digits
def DigitChecker(No):
    count = 0
    while(No > 0):
       No = No // 10
       count = count +1

    return count

def main():
    value = int(input("Enter the number : "))
    ret = DigitChecker(value)
    print(f"The digits in the {value} are : {ret}")

if(__name__=="__main__"):
    main()
 