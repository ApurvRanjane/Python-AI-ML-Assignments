#Q2 : Write a program of lambda function which accept one number and return cube of that number.

cube = lambda a: (a*a*a)

def main():
    value = int(input("Enter number : "))
    ret = cube(value)
    print("Cube of ",value," is : ",ret)

if(__name__=="__main__"):
    main()