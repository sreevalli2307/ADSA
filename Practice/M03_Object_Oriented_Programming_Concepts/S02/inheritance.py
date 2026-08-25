'''
Inheritance: Acquiring properties from one class to another
Types of inheritance:
1.single
2.Multi-level
3.Hierarchical
4.Multiple
5.Hybrid


#single
class A:
    def display1(self):
        print("This is class A display method")
class B(A):
    def display2(self):
        print("this is class B display method")
b =B()
b.display1()
b.display2()

#Multilevel
class A:
    def display1(self):
        print("This is class A display method")
class B(A):
    def display2(self):
        print("this is class B display method")
class c(A):
    def display3(self):
        print("this is class c display method")
#hierarchical

class A:
    def display1(self):
        print("This is class A display method")
class B(A):
    def display2(self):
        print("this is class B display method")
class c(A):
    def display3(self):
        print("this is class c display method")
'''
#Multiple
class A:
    def display(self):
        print("This is class A display method")
class B(A):
    def display(self):
        print("this is class B display method")
class C(A,B):
    def display3(self):
        print("this is class C display method")
c = C()
c.display()
#Hybrid:
# Base class
class A:
    def display1(self):
        print("This is class A display method")

# Class B inherits from A (single inheritance)
class B(A):
    def display2(self):
        print("This is class B display method")

# Class C also inherits from A (hierarchical inheritance)
class C(A):
    def display3(self):
        print("This is class C display method")

# Class D inherits from both B and C (multiple inheritance)
class D(B, C):
    def display4(self):
        print("This is class D display method")

# Usage
obj = D()
obj.display1()  # From A
obj.display2()  # From B
obj.display3()  # From C
obj.display4()  # From D

#MRO= Method Resolution order