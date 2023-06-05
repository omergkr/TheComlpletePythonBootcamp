my_list = [1, 2, 3, 4, 5]
my_list2 = ["String", 1, 2, 3, 4, 5.2, True]
print(len(my_list2))
print(my_list2[0])
print(my_list2[3:])
another_list = my_list + my_list2
print(another_list)
my_list2[0] = "change"
print(my_list2)
my_list2.append("six")
print(my_list2)
popped_item = my_list2.pop()
print(popped_item)
print(my_list2)
my_list2.pop(0)
print(my_list2)
new_list = ["a", "e", "c", "x"]
num_list = [4, 1, 8, 2]
new_list.sort()
print(new_list)
num_list.reverse()
print(num_list)
