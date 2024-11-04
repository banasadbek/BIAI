class Animal:
    def __init__(self, name, legs, sound) -> None:
        self.__name = name
        self.__legs = legs
        self.__sound = sound
        self.__action = ''
    
    def get_name(self):
        return(self.__name)

    def speak(self):
        return(self.__sound)
    
    def action(self):
        return(self.__action)
    
    def get_legs(self):
        return(self.__legs)
    
class Horse(Animal):
    def __init__(self, name):
        super().__init__(name, 4, 'Hi-hi-ha')
        self.__action = 'run'

class Dog(Animal):
    def __init__(self, name):
        super().__init__(name, 4, 'Wov-Wov')
        self.__action = 'bark'

class Chicken(Animal):
    def __init__(self, name):
        super().__init__(name, 2, 'Qu-quru-qu')
        self.__action = 'fly'

class Cow(Animal):
    def __init__(self, name):
        super().__init__(name, 4, 'Moo-Moo')
        self.__action = 'walk'
        

Horse1 = Horse('Ferrari')
Chicken1 = Chicken('Chick')
Dog1 = Dog('Alex')
Cow1 = Cow('Hayitvoy')

Farm = [Horse1, Chicken1, Dog1, Cow1]
for index in Farm:
    print(index.get_name(), index.speak(), index.get_legs(), index.action())
