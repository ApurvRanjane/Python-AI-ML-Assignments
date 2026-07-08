
# Q3: Design a Python application where multiple threads update a shared variable.
#     Use a Lock to avoid race conditions.
#     Each thread should increment the shared counter multiple times.
#     Display the final value of the counter after all threads complete execution.

import threading

counter = 0

lock = threading.Lock()

def Increment():
    global counter
    for i in range(100000):
        lock.acquire()
        counter = counter+1
        lock.release()

def main():
    Thread1 = threading.Thread(target=Increment)
    Thread2 = threading.Thread(target=Increment)
    Thread3 = threading.Thread(target=Increment)
    Thread4 = threading.Thread(target=Increment)

    Thread1.start()
    Thread2.start()
    Thread3.start()
    Thread4.start()

    Thread1.join()
    Thread2.join()
    Thread3.join()
    Thread4.join()

    print(f"Final value of counter is : {counter}")

if(__name__=="__main__"):
    main()

