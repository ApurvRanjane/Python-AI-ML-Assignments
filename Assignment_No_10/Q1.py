#Q1: Write a program which accept one number and prints multiplication table of that number.

def table(No):
    result = list()
    i = 1
    while(i <= 10):
        ans = No*i
        result.append(ans)
        i = i+1

    return result


def main():
    value = int(input("Enter Number : "))
    ret = table(value)
    print("The table of ",value," is : ",ret)

if(__name__=="__main__"):
    main()