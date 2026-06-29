#Q2 : Write a program which accept one number and prints its all factors.

def Factor(No):
    result = list()
    for i in range(1,No+1):
        if(No%i == 0):
            result.append(i)
    return result

def main():
    value = int(input("Enter Number : "))
    ret = Factor(value)
    print("The Factors of ",value," are : ",ret )
    

if(__name__=="__main__"):
    main()