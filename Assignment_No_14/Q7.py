#Q7 : Write a program of lambda function which accept one number and return true if it is divisible by 5 otherwise give false.

Checker = lambda a: a%5==0

def main():
    value = int(input("Enter number : "))
    ret = Checker(value)
    print("Number is divisible by 5 : ",ret)



if(__name__=="__main__"):
    main()