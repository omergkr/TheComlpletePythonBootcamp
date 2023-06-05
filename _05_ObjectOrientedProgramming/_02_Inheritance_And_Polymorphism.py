class Animal:

    def __int__(self):
        print("Animal Created")

    def who_am_i(self):
        print("i am an animal")

    def eat(self):
        print("i am eating")


class Cat(Animal):
    def __int__(self):
        Animal.__int__(self)
        print("Cat created")

    def who_am_i(self):
        print("i am a cat")


myCat = Cat()
my_animal = Animal()

myCat.who_am_i()
