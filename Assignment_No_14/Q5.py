#Q5 : Write a program of lambda function which accept one number and return true if it is even otherwise give false.

evenChecker = lambda a: a%2==0

def main():
    value = int(input("Enter number : "))
    ret = evenChecker(value)
    print("Number is even : ",ret)



if(__name__=="__main__"):
    main()