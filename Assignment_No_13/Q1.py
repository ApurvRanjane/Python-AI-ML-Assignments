#Q1 : Write a program which accepts length and width of rectangle and prints its area.

def Area(Length,Breadth):
    ans = Length * Breadth
    return ans

def main():
    l = int(input("Enter length of rectagle: "))
    b = int(input("Enter breadth of rectagle: "))
    ret = Area(l,b)
    print("The area of rectangle is : ",ret)

if(__name__=="__main__"):
    main()