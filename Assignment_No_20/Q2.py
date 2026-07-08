# Q2:
# Design a Python application that creates two threads named EvenFactor and OddFactor.
#
# Both threads should accept one integer number as a parameter.
#
# The EvenFactor thread should:
# - Identify all even factors of the given number.
# - Calculate and display the sum of even factors.
#
# The OddFactor thread should:
# - Identify all odd factors of the given number.
# - Calculate and display the sum of odd factors.
#
# After both threads complete execution, the main thread should display:
# "Exit from main"

import threading

def evenfactors(No):
    sum = 0
    for i in range(1,No):
        if(No%i == 0 and i%2 ==0):
            sum = sum+i
    print(f"The addition of even factors of {No} is :{sum}")

def oddfactors(No):
    sum = 0
    for i in range(1,No):
        if(No%i == 0 and i%2 !=0):
            sum = sum+i
    print(f"The addition of odd factors of {No} is :{sum}")


def main():
    value = int(input("Enter number: "))
    EvenFactor = threading.Thread(name="EvenFactor",target=evenfactors,args=(value,))
    oddFactor = threading.Thread(name="OddFactor",target=oddfactors,args=(value,))
    EvenFactor.start()
    oddFactor.start()

    EvenFactor.join()
    oddFactor.join()

    print("Exit from main..")

if(__name__=="__main__"):
    main()