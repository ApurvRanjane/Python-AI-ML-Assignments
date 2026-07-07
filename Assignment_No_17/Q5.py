#Q5: Write a program which accept one number and display it is prime or not

def PrimeChecker(No):
    if(No<2):
        return False
    count = 0
    for i in range(1,No+1):
        if(No % i == 0):
            count = count+1
    if(count==2):
        return True
    else:
        return False

def main():
    value = int(input("Enter the number : "))
    ret = PrimeChecker(value)
    if(ret):
        print(f"The {value} is a prime number..")
    else:
        print(f"The {value} is not a prime number..")


if(__name__=="__main__"):
    main()
 