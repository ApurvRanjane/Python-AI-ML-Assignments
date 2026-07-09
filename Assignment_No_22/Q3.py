# 3. For every number in the given list, count how many prime numbers exist between 1 and N using multiprocessing Pool.

# Example:
# 10000
# 20000
# 30000
# 40000

# Display total prime count for each number.

import os 
import multiprocessing
import time

def PrimeChecker(No):
   count = 0
   if(No<2):
       return False
   
   for i in range(1,No+1):
       if(No%i == 0):
           count = count+1
   if(count == 2):
       return True
   else:
       return False

def Primer(No):
    count = 0
    print(f"The Process ID: {os.getpid()}")
    for i in range(1,No+1):
        if(PrimeChecker(i)):
            count = count+1
    print(f"The count of prime numbers between 1 to {No} is {count}")
    return count


def main():
    start_time=time.time()
    data = [10000, 20000, 30000, 40000]
    result = []
    p = multiprocessing.Pool()
    result = p.map(Primer,data)
    p.close()
    p.join()
    print(result)
    end_time = time.time()
    print("Execution time is : ",end_time-start_time)

if __name__=="__main__":
    main()