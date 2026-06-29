#Q2 : Write a program which accept one number and prints count of digit in that number.

def digitChecker(No):
    count = 0
    while(No>0):
        # last = No % 10
        count = count +1
        No = No//10
    return count
    
def main():
    value = int(input("Enter Number : "))
    ret = digitChecker(value)
    print(value," has ",ret," digits...")

if(__name__=="__main__"):
    main()