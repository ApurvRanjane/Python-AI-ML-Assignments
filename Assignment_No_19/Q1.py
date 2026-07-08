#Q1 : Write a program which conatin one lambda function which accept one number and return its power of two.

Powertwo = lambda a:(a ** 2)

def main():
    value = int(input("Enter the number : "))
    ret = Powertwo(value)
    print(f"The power of 2 of {value} is : {ret}")

if(__name__=="__main__"):
    main()
    