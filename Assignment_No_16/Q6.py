#Q6 : Write a program which accept one parameter as number and check wheather it is positive,negative,or zero.

def ChkNum(number):
    if(number > 0):
        return "Positive"

    elif(number < 0):
        return "Negative"
    
    else:
        return 0
    
def main():
    num = int(input("Enter Number : "))
    ret = ChkNum(num)
    print("The ",num," is : ",ret)

if(__name__=="__main__"):
    main()