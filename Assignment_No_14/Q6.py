
#Q6 : Write a program of lambda function which accept one number and return true if it is odd otherwise give false.

oddChecker = lambda a: a%2 != 0

def main():
    value = int(input("Enter number : "))
    ret = oddChecker(value)
    print("Number is odd : ",ret)



if(__name__=="__main__"):
    main()