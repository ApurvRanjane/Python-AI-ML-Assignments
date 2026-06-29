#Q2: Write a function chkGreater() which accepts two numbers and prints greater number.

def chkGreater(No1,No2):
    if(No1 > No2):
        print(No1," is greater")
    else:
        print(No2," is greater")

def main():
    chkGreater(10,20)

if (__name__=="__main__"):
    main()