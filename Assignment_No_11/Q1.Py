#Q1 : Write a program which accept one number and check wheather it is prime or not.

def primeChecker(No):
    count = 0
    for i in range(1,No+1):
        if(No%i == 0):
            count = count+1

    if (count==2):
        return True
    else:
        return False
    
def main():
    value = int(input("Enter Number : "))
    ret = primeChecker(value)
    if(ret):
        print(value," is prime number...")
    else:
        print(value," is not prime number...")

if(__name__=="__main__"):
    main()