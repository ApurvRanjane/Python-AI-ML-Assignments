#Q3 : Write a program which accepts one number and check wheather it is perfect number or not.

def PerfectNum(No):
    sum = 0
    for i in range(1,No):
        if(No%i == 0):
            sum = sum + i
            
    if(No == sum ):
        return True
    else: 
        return False

def main():
    value = int(input("Enter Number : "))
    ret = PerfectNum(value)
    if(ret):
        print(value ," is a perfect number..")
    else:
        print(value ," is not a perfect number..")

if(__name__=="__main__"):
    main()