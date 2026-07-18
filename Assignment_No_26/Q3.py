# 3: Write a Python program to implement a class named Arithmetic with the following characteristics:

# • The class should contain two instance variables: Value1 and Value2.
# • Define a constructor (__init__) that initializes all instance variables to 0.
# • Implement the following instance methods:
#     - Accept()         -> accepts values for Value1 and Value2 from the user.
#     - Addition()       -> returns the addition of Value1 and Value2.
#     - Subtraction()    -> returns the subtraction of Value1 and Value2.
#     - Multiplication() -> returns the multiplication of Value1 and Value2.
#     - Division()       -> returns the division of Value1 and Value2 (handle division by zero properly).
# • Create multiple objects of the Arithmetic class and invoke all the instance methods.

class Arithmetic:
    def __init__(self):
        self.value1 = 0
        self.value2 = 0

    def Accept(self):
        self.value1 = int(input("Enter the number1: "))
        self.value2 = int(input("Enter the number2: "))

    def Addition(self):
        return self.value1 + self.value2
        
    def Substraction(self):
        return self.value1 - self.value2

    def Multiplication(self):
        return self.value1 * self.value2

    def Division(self):
        try:
            ans = self.value1 / self.value2
            return ans
        
        except ZeroDivisionError as zerr:
            print("The second operand is zero...")

obj1 = Arithmetic()
obj1.Accept()
ret = obj1.Addition()
print("Addititon is : ",ret)

ret = obj1.Substraction()
print("Substraction is : ",ret)

ret = obj1.Multiplication()
print("Multiplication is : ",ret)

ret = obj1.Division()
print("Division is : ",ret)
print("------------------------------------------------")
obj2 = Arithmetic()
obj2.Accept()
ret = obj2.Addition()
print("Addititon is : ",ret)

ret = obj2.Substraction()
print("Substraction is : ",ret)

ret = obj2.Multiplication()
print("Multiplication is : ",ret)

ret = obj2.Division()
print("Division is : ",ret)