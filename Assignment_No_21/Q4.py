#Q1: Desgin a Python application that createstwo threads.
#Thread1 should compute the sum of elements from a list
#Thread2 should compute the product of elements from a list
#Return the results to the main thread and display them.

import threading

def Summation(list):
   sum = 0
   for i in list:
       sum = sum + i
   print(f"Sum of elements in list is : {sum}")

def Product(list):
    mul = 1
    for i in list:
        mul = mul * i
    print(f"Poduct of elements in list is : {mul}")
    

def main():
    list = []
    size = int(input("Enter the size of list : "))
    for i in range(size):
        value = int(input('enter element: '))
        list.append(value)
    Thread1 = threading.Thread(name="Thread1",target=Summation,args=(list,))
    Thread2 = threading.Thread(name="Thread2",target=Product,args=(list,))
    Thread1.start()
    Thread2.start()
    Thread1.join()
    Thread2.join()

if(__name__=="__main__"):
    main()