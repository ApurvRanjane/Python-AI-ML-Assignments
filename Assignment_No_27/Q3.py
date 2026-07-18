# 3: Write a Python program to implement a class named Numbers with the following specifications:

# • The class should contain one instance variable:
#     - Value
# • Define a constructor (__init__) that accepts a number from the user and initializes Value.
# • Implement the following instance methods:
#     - ChkPrime()  -> returns True if the number is prime, otherwise returns False.
#     - ChkPerfect() -> returns True if the number is perfect, otherwise returns False.
#     - Factors() -> displays all factors of the number.
#     - SumFactors() -> returns the sum of all factors.
# • Create multiple objects and call all methods.

class Numbers:
    def __init__(self,Value):
        self.Value = Value
    
    def ChkPrime(self):
        if(self.Value<2):
            return False
        count =0
        for i in range(1,self.Value+1):
            if(self.Value%i==0):
                count= count+1
        if(count==2):
            return True
        else:
            return False
    def ChkPerfect(self):
        sum = 0
        for i in range(1,self.Value):
            if(self.Value%i == 0):
                sum = sum+i
        if(sum == self.Value):
            return True
        else:
            return False
        
    def Factors(self):
        for i in range(1,self.Value):
            if(self.Value%i == 0):
                print(f" {i} ")
    
    def SumFactors(self):
        sum = 0
        for i in range(1,self.Value):
            if(self.Value%i == 0):
                sum = sum +i
        return sum

obj1 = Numbers(25)
ret = obj1.ChkPrime()
if(ret):
    print(f"The {obj1.Value} is prime..")
else:
    print(f"The {obj1.Value} is not prime..")

ret = obj1.ChkPerfect()
if(ret):
    print(f"The {obj1.Value} is perfect..")
else:
    print(f"The {obj1.Value} is not perfect..")

print(f"The factors of {obj1.Value} are:")
obj1.Factors()

ret = obj1.SumFactors()
print(f"The sum of factors of{obj1.Value} is : {ret}")

obj2 = Numbers(18)
ret = obj2.ChkPrime()
if(ret):
    print(f"The {obj2.Value} is prime..")
else:
    print(f"The {obj2.Value}  is not prime..")

ret = obj2.ChkPerfect()
if(ret):
    print(f"The {obj2.Value}  is perfect..")
else:
    print(f"The {obj2.Value}  is not perfect..")

print(f"The factors of {obj2.Value} are:")
obj2.Factors()

ret = obj2.SumFactors()
print(f"The sum of factors of {obj2.Value}  is : {ret}")

