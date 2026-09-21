# 1️⃣ Single Inheritance
class Parent:
    def func1(self):
        print("This is Parent class")

class Child(Parent):
    def func2(self):
        print("This is Child class")

obj1 = Child()
obj1.func1()
obj1.func2()


# 2️⃣ Multiple Inheritance
class Mother:
    def mother_func(self):
        print("This is Mother class")

class Father:
    def father_func(self):
        print("This is Father class")

class Child(Mother, Father):
    def child_func(self):
        print("This is Child class")

obj2 = Child()
obj2.mother_func()
obj2.father_func()
obj2.child_func()

# 3️⃣ Multilevel Inheritance
class Grandparent:
    def grandparent_func(self):
        print("This is Grandparent class")

class Parent(Grandparent):
    def parent_func(self):
        print("This is Parent class")

class Child(Parent):
    def child_func(self):
        print("This is Child class")

obj3 = Child()
obj3.grandparent_func()
obj3.parent_func()
obj3.child_func()


# 4️⃣ Hierarchical Inheritance
class Parent:
    def parent_func(self):
        print("This is Parent class")

class Child1(Parent):
    def child1_func(self):
        print("This is Child1 class")

class Child2(Parent):
    def child2_func(self):
        print("This is Child2 class")

obj4 = Child1()
obj5 = Child2()
obj4.parent_func()
obj4.child1_func()
obj5.parent_func()
obj5.child2_func()


# 5️⃣ Hybrid Inheritance (combination of multiple types)
class A:
    def funcA(self):
        print("This is class A")

class B(A):
    def funcB(self):
        print("This is class B")

class C(A):
    def funcC(self):
        print("This is class C")

class D(B, C):  # Multiple + Multilevel + Hierarchical
    def funcD(self):
        print("This is class D")

obj6 = D()
obj6.funcA()
obj6.funcB()
obj6.funcC()
obj6.funcD()
