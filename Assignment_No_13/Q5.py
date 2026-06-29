#Q5 : Write a program which accepts marks and prints grades.

def GradeSystem(No):
    if(No >= 75):
        return "Distinction"
    
    elif(No >=60):
        return "First Class"
    
    elif(No >=50):
        return "Second Class"
    
    else:
        return "Fail"
    

def main():
    value = int(input("Enter Marks : "))
    ret = GradeSystem(value)
    print("the grade is :",ret)

if(__name__=="__main__"):
    main()