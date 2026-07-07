#Q5:Write a program which accepts N numbers from the user and stores them into a List. Return the addition of all prime numbers from that list.
# The main Python file should accept N numbers from the user and pass each number to the ChkPrime() function, which is a part of a user-defined module named MarvellousNum.
# The name of the function in the main Python file should be ListPrime().

from MarvellousNum import chkPrime

def ListPrime(List):
   sum = 0
   for i in List:
       if(chkPrime(i)):
           sum = sum + i
   return sum

def main():
    List = []
    No = int(input("Enter the number of elements you want to insert in list : "))
    for i in range(No):
        num = int(input("Enter element in list : "))
        List.append(num)
    ret = ListPrime(List)
    print(f"The Addition of prime elements in the list is: {ret}")

if(__name__=="__main__"):
    main()

