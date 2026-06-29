#Q2: Write a program which accept one number and prints sum of first n natural numbers.

def Summation(No):
    sum = 0
    for i in range(1,No+1):
        sum = sum + i
    return sum


def main():
    value = int(input("Enter Number : "))
    ret = Summation(value)
    print("The sum of first n natural number is : ",ret)

if(__name__=="__main__"):
    main()