#Q4 : Write a program which accepts one number and prints its binary equivalent.

def Binary(No):
    ans=0
    pow=1
    while(No>0):
        rem=No%2
        No=No//2
        ans = ans+(rem*pow)
        pow=pow*10
    
    return ans

def main():
    value = int(input("Enter Number : "))
    ret = Binary(value)
    print("The binary equivalent for number is :",ret)

if(__name__=="__main__"):
    main()