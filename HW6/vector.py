from __future__ import annotations
from math import sqrt

class Vector:
    def __init__(self, *args):
        'Initialize'
        self.points = list(args)

    def __str__(self):
        msg = 'vector empty'
        if len(self.points) > 0:
            msg = 'Vector = ' + str(self.points[0])
            for index in self.points[1:]:
               msg += ', ' + str(index) 
        return msg
    
    def __bool__(self):
        flag = False
        for index in self.points:
            if index != 0:
                flag = True
                return flag
        return flag
    
    def __add__(self, other_vector: Vector):
        result = []
        for index in range(len(self.points)):
            result.append(self.points[index] + other_vector.points[index])
        new_vector = Vector(result) 
        return new_vector
    
    
    def __sub__(self, other_vector: Vector):
        result = []
        for index in range(len(self.points)):
            result.append(self.points[index] - other_vector.points[index])
        new_vector = Vector(result) 
        return new_vector
    
    def __mul__(self, other_vector: Vector):
        result = []
        for index in range(len(self.points)):
            result.append(self.points[index] * other_vector.points[index])
        new_vector = Vector(result) 
        return new_vector

    def __eqq__(self, other_vector: Vector):
        flag = True
        for index in range(len(self.points)):
            if self.points[index] != other_vector.points[index]:
                flag = False
                return flag
        return flag
    
    def __len__(self):
        return(len(self.points))
    
    def __abs__(self):
        value = 0
        for index in self.points:
            value += index**2
        value = sqrt(value)
        return(value)

    def __scm__(self, number:float):
        for index in range(len(self.points)):
            self.points[index] *= number
            
    def __scd__(self, number:float):
        for index in range(len(self.points)):
            self.points[index] /= number

    def __negative__(self):
        for index in range(len(self.points)):
            self.points[index] *= -1
    
vector1 = Vector(2,4)
print(vector1)
print(vector1.__bool__())
vector2 = Vector(2,3)
print(vector1.__add__(vector2))
print(vector1.__sub__(vector2))
print(vector1.__eqq__(vector2))
print(vector1.__len__())
print(vector1.__abs__())
vector1.__scd__(2)
print(vector1)
