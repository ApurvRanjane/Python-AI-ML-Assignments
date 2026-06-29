#Q4 : Write a program which accept one number and prints sum of digit in that number.

def numberSize(No):
    count = 0
    while(No>0):
        count = count +1
        No = No//10
    return count

def ReverseNumber(No):
    size = numberSize(No)
    num = 0
    count = 0
    while(No>0):
        last = No % 10
        count = count +1
        num = num + (last * (10**(size-count))) 
        No = No//10
    return num

def main():
    value = int(input("Enter Number : "))
    ret = ReverseNumber(value)
    print("Reverse number is : ",ret)

if(__name__=="__main__"):
    main()

    