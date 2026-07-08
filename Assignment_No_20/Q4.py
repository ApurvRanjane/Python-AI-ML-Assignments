# Q4:
# Design a Python application that creates three threads named Small, Capital, and Digits.
#
# All threads should accept a string as input.
#
# The Small thread should:
# - Count and display the number of lowercase characters.
#
# The Capital thread should:
# - Count and display the number of uppercase characters.
#
# The Digits thread should:
# - Count and display the number of numeric digits.
#
# Each thread must also display:
# - Thread ID
# - Thread Name

import threading

def lower(str):
    print(f"Thread ID : {threading.get_ident()}")
    print(f"Thread Name is : {threading.current_thread().name}")
    count = 0
    for i in str:
        if(i.islower()):
            count = count+1
    print(f"The lowercase letter count in string are : {count}")

def upper(str):
    print(f"Thread ID : {threading.get_ident()}")
    print(f"Thread Name is : {threading.current_thread().name}")
    count = 0
    for i in str:
        if(i.isupper()):
            count = count+1
    print(f"The uppercase letter count in string are : {count}")

def digit(str):
    print(f"Thread ID : {threading.get_ident()}")
    print(f"Thread Name is : {threading.current_thread().name}")
    count = 0
    for i in str:
        if(i.isdigit()):
            count = count+1
    print(f"The digits count in string are : {count}")

def main():
    str = input("Enter string here: ")

    Small = threading.Thread(name="Small",target=lower,args=(str,))
    Capital = threading.Thread(name="Capital",target=upper,args=(str,))
    Digits = threading.Thread(name="Digits",target=digit,args=(str,))

    Small.start()
    Capital.start()
    Digits.start()

    Small.join()
    Capital.join()
    Digits.join()

    print("Exit from main..")

if(__name__=="__main__"):
    main()