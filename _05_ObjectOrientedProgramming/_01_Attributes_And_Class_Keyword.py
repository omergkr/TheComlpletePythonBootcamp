class Dog:
    # Class attribute
    species = "mammal"

    def __init__(self, breed, name, spots):
        self.breed = breed
        self.name = name
        self.spots = spots

    # operations/ actions
    def bark(self, number):
        print("Wooff! my name is {} and the number is {} ".format(self.name, number))


my_dog = Dog(breed="Huskie", name="Sammy", spots=False)

print(my_dog.breed)
my_dog.bark(5)
