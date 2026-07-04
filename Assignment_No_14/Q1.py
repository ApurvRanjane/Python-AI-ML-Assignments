#Q1 : Write a program of lambda function which accept one number and return square of that number.

square = lambda a: (a*a)

def main():
    value = int(input("Enter number : "))
    ret = square(value)
    print("Square of ",value," is : ",ret)

if(__name__=="__main__"):
    main()