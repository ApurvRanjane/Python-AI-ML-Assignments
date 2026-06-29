#Q4: Write a program which accept one number and prints all even number till that number.

def Even(No):
    result = []
    for i in range(1,No+1):
        if(i%2 == 0):
            result.append(i)
    return result   

def main():
    value = int(input("Enter Number : "))
    ret = Even(value)
    print("The Even numbers till that",value, "are : ",ret)

if(__name__=="__main__"):
    main()