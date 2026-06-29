#Q4: Write a program which accept one number and prints cube of that number.

def Cube(No):
   ans = No*No*No
   print("Cube is ",ans)

def main():
    value = int(input("Enter Number: "))
    Cube(value)
    

if (__name__=="__main__"):
    main()

    