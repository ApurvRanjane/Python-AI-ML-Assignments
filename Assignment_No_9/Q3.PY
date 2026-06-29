#Q3: Write a program which accept one number and prints square of that number.

def Square(No):
   ans = No*No
   print("Square is ",ans)

def main():
    value = int(input("Enter Number: "))
    Square(value)
    

if (__name__=="__main__"):
    main()

    