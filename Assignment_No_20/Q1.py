# Q1:
# Design a Python application that creates two separate threads named Even and Odd.
#
# The Even thread should display the first 10 even numbers.
# The Odd thread should display the first 10 odd numbers.
#
# Both threads should execute independently using the threading module.
# Ensure proper thread creation and execution.

import threading

def evendisplay():
    count = 0
    start = 2
    while(count<10):
        print(start)
        start = start+2
        count = count+1

def odddisplay():
    count = 0
    start = 1
    while(count<10):
        print(start)
        start = start+2
        count = count+1

def main():
    Even = threading.Thread(name="Even",target=evendisplay)
    odd = threading.Thread(name="Odd",target=odddisplay)
    Even.start()
    odd.start()

    Even.join()
    odd.join()

if(__name__=="__main__"):
    main()