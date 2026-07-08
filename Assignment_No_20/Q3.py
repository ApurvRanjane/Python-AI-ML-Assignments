# Q3:
# Design a Python application that creates two threads named EvenList and OddList.
#
# Both threads should accept a list of integers as input.
#
# The EvenList thread should:
# - Extract all even elements from the list.
# - Calculate and display their sum.
#
# The OddList thread should:
# - Extract all odd elements from the list.
# - Calculate and display their sum.
#
# Threads should run concurrently.

import threading

def ListMaker(size):
    list = []
    for i in range(size):
        value = int(input("Enter element in list : "))
        list.append(value)
    return list

def evensum(list):
    sum = 0
    for i in list:
        if(i%2==0):
            sum = sum + i
    print(f"The sum of even numbers in list is : {sum}")

def oddsum(list):
    sum = 0
    for i in list:
        if(i%2!=0):
            sum = sum + i
    print(f"The sum of odd numbers in list is : {sum}")


def main():
    size = int(input("Enter size of list: "))
    ret1 = ListMaker(size)

    EvenList = threading.Thread(name="EvenList",target=evensum,args=(ret1,))
    oddList = threading.Thread(name="OddList",target=oddsum,args=(ret1,))

    EvenList.start()
    oddList.start()

    EvenList.join()
    oddList.join()

    print("Exit from main..")

if(__name__=="__main__"):
    main()