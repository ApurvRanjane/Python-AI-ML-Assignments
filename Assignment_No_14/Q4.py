#Q4 : Write a program of lambda function which accept two number and return minimum number.

minimum = lambda a,b: a if (a<b) else b

def main():
    value1 = int(input("Enter number1 : "))
    value2 = int(input("Enter number2 : "))
    ret = minimum(value1,value2)
    print("Minimum number from both numbers is  : ",ret)

if(__name__=="__main__"):
    main()
    