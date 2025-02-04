
# inheritance in python
class Pet:
    def __init__(self,name):
        self.name = name
    def info(self):
        print(f"the pet name is {self.name}")
class Dog(Pet):
    pass
class Cat(Pet):
    pass
class Hamster(Pet):
    pass

pet2 = Dog("tommy")
print(pet2.name)
pet2.info()


# multiple inheritance in python
class A:
    a = int(input("enter 1st number : "))
class B:
    b = int(input("enter 2nd number : "))
class C(A,B):
    def add():
        c = C.a + C.b
        print(c)
add1 = C
add1.add()