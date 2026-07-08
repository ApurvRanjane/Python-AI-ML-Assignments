# Q5:
# Write a program which contains filter(), map() and reduce() in it.
# Python application contains one list of numbers. List contains the numbers
# which are accepted from user.
# Filter should filter out all prime numbers.
# Map function will multiply each number by 2.
# Reduce will return maximum number from those numbers.
# (You can also use normal functions instead of lambda functions.)

from functools import reduce

def filterfun(a):
    count = 0
    if(a<2):
        return False
    for i in range(1,a+1):
        if(a%i==0):
            count = count+1
    if(count ==2):
        return True
    else:
        return False

mapfun  = lambda a : a*2

reducefun = lambda a,b : a if a>b else b

def main():
    size = int(input("Enter the size of list : "))
    List = []
    for i in range(size):
        value = int(input("Enter the value in list: "))
        List.append(value)
    
    print(f" the original list is: {List}")
    ret1 = list(filter(filterfun,List))
    print(f" the list after filter is: {ret1}")
    ret2 = list(map(mapfun,ret1))
    print(f" the list after map is: {ret2}")
    ret3 = reduce(reducefun,ret2)
    print(f" the answer after reduce is: {ret3}")
    


if(__name__=="__main__"):
    main()