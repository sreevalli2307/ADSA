from math import pi 
class Circle:
    r = 7
    count = 0
    def __init__(self):
        Circle.count +=1
    def area(self):
        return pi*self.r*self.r 
    def perimeter(self):
        return 2*pi*self.r 
c1 = Circle(7)
c2 = Circle(10)
c3 = Circle(15)
print(c1.area())
print(c1.perimeter())
print(c2.area())
print(c2.perimeter())
print(c3.area())
print(c3.perimeter())
'''
1603. Design Parking System

class ParkingSystem:

    def __init__(self, big: int, medium: int, small: int):
        self.slots = [0, big, medium, small]
        

    def addCar(self, carType: int) -> bool:
        if self.slots[carType] > 0:
            self.slots[carType] -= 1
            return True
        return False

class ParkingSystem:

    def __init__(self, big: int, medium: int, small: int):
        self.big = big
        self.medium = medium
        self.small = small
        

    def addCar(self, carType: int) -> bool:
        if carType==1:
            if self.big>0:
                self.big-=1
                return True
        if carType==2:
            if self.medium>0:
                self.medium-=1
                return True
        if carType==3:
            if self.small>0:
                self.small-=1
                return True
        return False
            

  1845. Seat Reservation Manager

'''