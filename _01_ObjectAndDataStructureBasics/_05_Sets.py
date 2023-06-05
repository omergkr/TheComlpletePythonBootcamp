# Sets are unordered collections of unique elements.
# Meaning there can only be one representative of the same object.

my_set = set()
my_set.add(1)
print(my_set)
my_set.add(2)
print(my_set)
my_set.add(2)
print(my_set)

my_list = [1, 2, 1, 1, 1, 1, 3, 4, 5, 5, 5, 6]
my_new_set = set(my_list)
print(my_new_set)    # {1, 2, 3, 4, 5, 6}
