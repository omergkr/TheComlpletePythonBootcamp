# Once an element is inside a tuple, it can not be reassigned.
# Tuples use parenthesis:  (1,2,3)

t = (1, 2, 3)
new_t = ("one", 2, 3)
my_list = [1, 2, 3]

print(type(t))
print(type(my_list))

print(len(t))

new_t2 = ('a', 'b', 'c', 'a')
print(new_t2.count('a'))
print(new_t2.index('a'))


my_list[0] = "new_list"

# new_t[0] = 5  immutable
