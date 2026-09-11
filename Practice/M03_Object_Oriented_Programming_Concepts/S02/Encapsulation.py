'''Data higing:
access speciers:
Private 🡺_ _ variable(2 underscores)
Protected🡺 _ variable (single underscore)
Public🡺no underscores
'''
class A:
    a=10 #public
    _b=20#protected
    __c=30#private
obj =A()
print(obj.a)
print(obj._b)
print(obj._A__c)
#access and modify private members from class using methods
class Bank:
    def __init__(self,balance):
        self._balance = balance
    def credit(self,amount):
        self._balance += amount
    def debit(self,amount):
        self._balance -= amount 
    def display(self):
        print("Current balance:",self._balance)
b = Bank(1000)
b.display()
b.credit(1500)
b.display()
b.debit(500)
b.display()