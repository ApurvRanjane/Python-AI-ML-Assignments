# Q3:
# Write a program which contains filter(), map() and reduce() in it.
# Python application contains one list of numbers. List contains the numbers
# which are accepted from user.
# Filter should filter out all such numbers which are greater than or equal to
# 70 and less than or equal to 90.
# Map function will increase each number by 10.
# Reduce will return product of all those numbers.

from functools import reduce

filterfun = lambda a : a >= 70 and a <= 90

mapfun  = lambda a : a+10

reducefun = lambda a,b : a*b

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