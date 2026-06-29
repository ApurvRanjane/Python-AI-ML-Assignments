#Q1 : Write a program which accepts radius of circle and prints its area.

def Area(radius):
    ans = 3.14 * radius * radius
    return ans

def main():
    r = int(input("Enter radius of circle: "))
    ret = Area(r)
    print("The area of circle is : ",ret)

if(__name__=="__main__"):
    main()