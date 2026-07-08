#Q1 : Design a python application that creates two threads named Prime and NonPrime.
#Both threads should accept list of integers.
#The Prime thread should display all prime numbers from the list.
#The NonPrime thread should display all non-prime nubers from the list.

import threading

def PrimeChecker(No):
    count = 0
    if(No<2):
        return False
    for i in range(1,No+1):
        if(No%i==0):
            count =count +1
    if(count == 2):
        return True
    else:
        return False


def PrimeNumbers(list):
    for i in list:
        if(PrimeChecker(i)):
            print(f"Prime:{i}")

def NonPrimeNumbers(list):
    for i in list:
        if(PrimeChecker(i) == False):
            print(f"NonPrime:{i}")


def main():
    list = []
    size = int(input("Enter the size of list : "))
    for i in range(size):
        value = int(input('enter element: '))
        list.append(value)
    Prime = threading.Thread(name="Prime",target=PrimeNumbers,args=(list,))
    NonPrime = threading.Thread(name="NonPrime",target=NonPrimeNumbers,args=(list,))
    Prime.start()
    NonPrime.start()
    Prime.join()
    NonPrime.join()

if(__name__=="__main__"):
    main()