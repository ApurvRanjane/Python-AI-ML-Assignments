#Q5: Write a program which accept one number and prints all odd number till that number.

def Odd(No):
    result = []
    for i in range(1,No+1):
        if(i%2 != 0):
            result.append(i)
    return result   

def main():
    value = int(input("Enter Number : "))
    ret = Odd(value)
    print("The odd numbers till that",value, "are : ",ret)

if(__name__=="__main__"):
    main()