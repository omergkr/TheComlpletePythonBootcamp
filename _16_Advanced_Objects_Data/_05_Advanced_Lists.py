my_list_1 = [1, 2, 3, 4]
my_list_1.append(4)
print(my_list_1)
print(my_list_1.count(10))
print(my_list_1.count(4))
print(my_list_1.count(2))

x = [1, 2, 3]
x.append([4, 5])
print(x)

x = [1, 2, 3]
x.extend([4, 5])
print(x)

print(my_list_1.index(2))

my_list_1.insert(2, 'inserted')
print(my_list_1)

ele = my_list_1.pop(1)
print(my_list_1)

my_list_1.remove('inserted')
print(my_list_1)
my_list_1.remove(4)
print(my_list_1)

print(my_list_1.reverse())
print(my_list_1)

my_list_1.sort()
print(my_list_1)
my_list_1.sort(reverse=True)
print(my_list_1)

"""
A common programming mistake is to assume you can assign a modified list to a new variable. 
While this typically works with immutable objects like strings and tuples:

x = 'hello world'
y = x.upper()
print(y) -> HELLO WORLD

This will NOT work the same way with lists:

x = [1,2,3]
y = x.append(4)
print(y)  -> None
What happened? In this case, since list methods like append() affect the list in-place, 
the operation returns a None value. 
This is what was passed to y. 
In order to retain x you would have to assign a copy of x to y, and then modify y:
"""


x = [1, 2, 3]
y = x.copy()
y.append(4)
print(x)
print(y)
