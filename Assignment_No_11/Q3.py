#Q3 : Write a program which accept one number and prints sum of digit in that number.

def digitSummation(No):
    sum = 0
    while(No>0):
        last = No % 10
        sum = sum + last 
        No = No//10
    return sum

def main():
    value = int(input("Enter Number : "))
    ret = digitSummation(value)
    print("Addition of digits in ",value," is :",ret)

if(__name__=="__main__"):
    main()

