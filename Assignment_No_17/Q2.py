#Q2: Write a program which accept one number and display pattern
def PatternFactory(No):
    for i in range(No):
        for j in range(No):
            print("*",end=" ")
        print()

def main():
    value = int(input("Enter the number : "))
    PatternFactory(value)

if(__name__=="__main__"):
    main()
 