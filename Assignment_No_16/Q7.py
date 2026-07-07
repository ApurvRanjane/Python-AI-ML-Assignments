#Q7 : Write a program which accept one parameter as number from user and return true if it is divisible by 5 else return false.

def ChkNum(number):
    if(number % 5 == 0):
        return True

    else:
        return False
    
def main():
    num = int(input("Enter Number : "))
    ret = ChkNum(num)
    
    if(ret):
        print(num," is divisible by 5..")
    else:
        print(num," is not divisible by 5..")

if(__name__=="__main__"):
    main()