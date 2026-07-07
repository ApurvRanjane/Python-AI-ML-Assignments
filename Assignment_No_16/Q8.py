#Q8 : Write a program which accept number from user and print number of times * on screen.

def Fun(Number):
    for i in range(Number):
        print("*", end=" ")

def main():
    num = int(input("Enter Number : "))
    Fun(num)

if(__name__=="__main__"):
    main()
    