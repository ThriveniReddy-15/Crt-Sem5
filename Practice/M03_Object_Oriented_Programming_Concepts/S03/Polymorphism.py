'''
Polymorphism :
Poly ===> Many
Morph ===> Forms

Types of polymorphism :
1.Compile-time
   1. Function Overloading - Creating 
   2. Operator Overloading 
2. Runtime 
    1. Method Overriding
'''
# Function Overloading 
'''
def add(a,b):
    return a+b 
def add(a,b,c):
    return a+b+c 
def add(a,b,c,d):
    return a+b+c+d 
print(add(10,20))
print(add(10,20,30))
print(add(10,20,30,40))'''
'''
Python does not support Function overloading directly 
we can use variable length arguments(using *) '''
def add(*values):
    return sum(values)
print(add(10,20))
print(add(10,20,30))
print(add(10,20,30,40))
# Operator Overloading
class A:
    def __init__(self,x):
        self.x = x
    def __add__(self, val):
        return self.x + val.x
    def __sub__(self, val):
        return self.x - val.x
    def __lt__(self, val):
        return self.x < val.x
        
a = A(10)
b = A(20)
print(a + b)
print(a - b)
print(a < b)
# Example 
class B:
    def __init__(self,x,y):
        self.x = x 
        self.y = y 
    def __add__(self, val):
        return (self.x + val.x,self.y + val.y)
    def __sub__(self, val):
        return (self.y - val.y,self.y - val.y)
a = B(10,20)
b = B(30,40)
print(a+b)
print(a-b)
# Method Overriding: Same method in both parent and child class
class Parent:
    def display(self):
        print("Parent class display method")
class child(Parent):
    def display(self):
        print("Child class display method")
c = child()
c.display()
Parent.display(c)
# Duck Typing
class Dog:
    def Sounds(self):
        print("Brak")
class  Cat:
    def Sounds(self):
        print("Meow")
def make_sound(animal):
    animal.Sounds()
d = Dog()
c = Cat()
make_sound(d)
make_sound(c)