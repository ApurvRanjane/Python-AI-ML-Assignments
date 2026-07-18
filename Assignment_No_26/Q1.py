# 1: Write a Python program to implement a class named Demo with the following specifications:

# • The class should contain two instance variables: no1 and no2.
# • The class should contain one class variable named Value.
# • Define a constructor (__init__) that accepts two parameters and initializes the instance variables.
# • Implement two instance methods:
#     - Fun()  -> displays the values of instance variables no1 and no2.
#     - Gun()  -> displays the values of instance variables no1 and no2.
# • Create two objects of Demo class as follows:
#     Obj1 = Demo(11, 21)
#     Obj2 = Demo(51, 101)
# • Call the instance methods in the following sequence:
#     Obj1.Fun()
#     Obj2.Fun()
#     Obj1.Gun()
#     Obj2.Gun()

class Demo:
    value = 0

    def __init__(self,i,j):
        self.no1=i
        self.no2=j

    def fun(self):
        print(self.no1)
        print(self.no2)
    
    def gun(self):
        print(self.no1)
        print(self.no2)

obj1 = Demo(11,21)
obj2 = Demo(51,101)

obj1.fun()
obj2.fun()
obj1.gun()
obj2.gun()