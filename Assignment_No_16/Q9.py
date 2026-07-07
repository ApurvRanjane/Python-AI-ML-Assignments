#Q9: Write a program which display first 10  even numbers 

def even(num):
    count = 0
    no = 1
    while(count<num):
        if(no%2==0):
            print(no)
            count= count+1
        no = no+1

def main():
    value = int(input("Enter the number : "))
    even(value)


if(__name__=="__main__"):
    main()
 