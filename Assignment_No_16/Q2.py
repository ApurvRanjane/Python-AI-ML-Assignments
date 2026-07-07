#Q2 : Write a program which conatins function named as ChkNum(), which accept one parameter as number if number is even it should display even else odd.

def ChkNum(number):
    if(number % 2 == 0):
        return True

    else:
        return False
    
def main():
    num = int(input("Enter Number : "))
    ret = ChkNum(num)
    if(ret):
        print("Even number..")
    else:
        print("Odd number...")

if(__name__=="__main__"):
    main()