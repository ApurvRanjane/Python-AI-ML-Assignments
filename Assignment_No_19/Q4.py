# Q4:
# Write a program which contains filter(), map() and reduce() in it.
# Python application contains one list of numbers. List contains the numbers
# which are accepted from user.
# Filter should filter out all such numbers which are even.
# Map function will calculate its square.
# Reduce will return addition of all those numbers.

from functools import reduce

filterfun = lambda a : a%2==0

mapfun  = lambda a : a*a

reducefun = lambda a,b : a+b

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