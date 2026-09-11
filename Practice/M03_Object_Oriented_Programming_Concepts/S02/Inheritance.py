'''
Inheritance: Acquiring properties from one class to another class
1.Single - one parent to on child A---B
2.Multilevel - one parent to another child to another child A---B---C
3.Hierarchical - one parent to multiple child A---B
4.Multiple Multiple parent to single child
5.Hybrid - combination of one or more inheritace 

'''
class A:
    def display1(self):
        print("This is class A display method")
class B(A):
    def display2(self):
        print("This is Class B display method")
class C(B):
    def display3(self):
        print("This is Class C display method")
b = C()
b.display1()
b.display2()
b.display3()
#Multilevel Inheritance

#Hierachical Inherirtance
