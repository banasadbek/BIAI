class Car:
    def __init__(self, yearModel, make):
        self.__yearModel = yearModel
        self.__make = make
        self.__speed = 0
    
    def get_yearModel(self):
        return self.__yearModel

    def get_make(self):
        return self.__make

    def accelerate(self):
        self.__speed += 5
        return(self.__speed)
    
    def brake(self):
        self.__speed -= 5
        return(self.__speed)

Car1 = Car('2012', 'BMW x5 2003')
for index in range(5):
    print(Car1.accelerate())

for index in range(5):
    print(Car1.brake())

