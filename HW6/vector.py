from __future__ import annotations
from math import sqrt

class Vector:
    def __init__(self, *args):
        'Initialize'
        self.__points = list(args)

    def __str__(self):
        msg = 'vector empty'
        if len(self.__points) > 0:
            msg = 'Vector = ' + str(self.__points[0])
            for index in self.__points[1:]:
               msg += ', ' + str(index) 
        return msg
    
    def __bool__(self):
        flag = False
        for index in self.__points:
            if index != 0:
                flag = True
                return flag
        return flag
    
    def __add__(self, other_vector: Vector):
        result = []
        for index in range(len(self.__points)):
            result.append(self.__points[index] + other_vector.__points[index])
        new_vector = Vector(result) 
        return new_vector
    
    
    def __sub__(self, other_vector: Vector):
        result = []
        for index in range(len(self.__points)):
            result.append(self.__points[index] - other_vector.__points[index])
        new_vector = Vector(result) 
        return new_vector
    
    def __mul__(self, other_vector: Vector):
        result = []
        for index in range(len(self.__points)):
            result.append(self.__points[index] * other_vector.__points[index])
        new_vector = Vector(result) 
        return new_vector

    def __eqq__(self, other_vector: Vector):
        flag = True
        for index in range(len(self.__points)):
            if self.__points[index] != other_vector.__points[index]:
                flag = False
                return flag
        return flag
    
    def len(self):
        return(len(self.__points))
    
    def __abs__(self):
        value = 0
        for index in self.__points:
            value += index**2
        value = sqrt(value)
        return(value)

    def __scm__(self, number:float):
        for index in range(len(self.__points)):
            self.__points[index] *= number
            
    def __scd__(self, number:float):
        for index in range(len(self.__points)):
            self.__points[index] /= number

    def __negative__(self):
        for index in range(len(self.__points)):
            self.__points[index] *= -1
    
    def __getitem__(self, index):
        return self.__points[index]
    
vector1 = Vector(2,4)
print(vector1)
print(vector1.__bool__())
vector2 = Vector(2,3)
print(vector1 + vector2)
# print(vector1.__sub__(vector2))
# print(vector1.__eqq__(vector2))
# print(vector1.len())
# print(vector1.__abs__())
# vector1.__scd__(2)
# print(vector1)
# # print(len(vector1))
# print(vector1[0])