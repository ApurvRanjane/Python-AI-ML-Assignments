#Q5 : Write a program which accept one number and prints that many numbers starting from 1 in reverse order.

def RevNumbers(No):
    result = list()
    for i in range(No,0,-1):
        result.append(i)
    return result

def main():
    value = int(input("Enter Number : "))
    ret = RevNumbers(value)
    print("The numbers starting from ",value,"to 1 are : ",ret )
    

if(__name__=="__main__"):
    main()


