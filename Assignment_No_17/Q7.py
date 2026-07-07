#Q7: Write a program which accept one number and display pattern
def PatternFactory(No):
    for i in range(1,No+1):
        for j in range(1,No+1):
            print(j,end=" ")
        print()

def main():
    value = int(input("Enter the number : "))
    PatternFactory(value)

if(__name__=="__main__"):
    main()
 