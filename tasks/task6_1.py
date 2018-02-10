import inspect
import dis

# def f():
#     class Pet(int):
#         pass


#     class Animal(float, Pet):
#         def __int__(self, name, )

#     print(inspect.getmro(Pet))
#     t = Pet(1)
#     print(t)
#     print(dir(t))

#     print(Animal())

class Vec2D(object):
    def __init__(self):
        self.c = 0

    def __add__(self, other):
        self.c += 1
        print(type(self))
        return self + other

    def __str__(self):
        return str(self.c)


class Vehicle(object):
    wheels = 4 
    def __init__(self, make, model):
        self.make = make
        self.model = model
        return self



class Car(Vehicle):
    wheels = 4 
    def __init__(self, make, model):
        self.make = make
        self.model = model
        return self

