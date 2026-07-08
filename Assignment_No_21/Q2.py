#Q2 : Design a python application that creates two threads named Thread1 and Thread2.
#Both threads should accept list of integers.
#The Thread1 should display maximum number from the list.
#The Thread2 should display mainimum number from the list.

import threading

def Maximum(list):
    max = -100000000
    for i in list:
        if(i>max):
            max = i
    print(f"Maximum number from list is : {max}")

def Minimum(list):
    min = 100000000
    for i in list:
        if(i<min):
            min = i
    print(f"Minimum number from list is : {min}")
   

def main():
    list = []
    size = int(input("Enter the size of list : "))
    for i in range(size):
        value = int(input('enter element: '))
        list.append(value)
    Thread1 = threading.Thread(name="Thread1",target=Maximum,args=(list,))
    Thread2 = threading.Thread(name="Thread2",target=Minimum,args=(list,))
    Thread1.start()
    Thread2.start()
    Thread1.join()
    Thread2.join()

if(__name__=="__main__"):
    main()