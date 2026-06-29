#Q1 : Write a program which accept one character and identify it is vowel or consonent.

def Checker(Ch):
    vowels = ["A","E","I","O",'U',"a","e","i","o","u"]
    for i in range(len(vowels)):
        if(Ch==vowels[i]):
            return "Vowel"
    return "Consonent"

def main():
    value = input("Enter Charcter : ")
    ret = Checker(value)
    if(ret == "Vowel"):
        print("The ",value," is Vowel..")
    else:
        print("The ",value," is Consonent..")

if(__name__=="__main__"):
    main()