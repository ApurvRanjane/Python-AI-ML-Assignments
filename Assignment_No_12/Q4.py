#Q4 : Write a program which accept one number and prints that many numbers starting from 1.

def Numbers(No):
    result = list()
    for i in range(1,No+1):
        result.append(i)
    return result

def main():
    value = int(input("Enter Number : "))
    ret = Numbers(value)
    print("The numbers starting from 1 to ",value," are : ",ret )
    

if(__name__=="__main__"):
    main()


