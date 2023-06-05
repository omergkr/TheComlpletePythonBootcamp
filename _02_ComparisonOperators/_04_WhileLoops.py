# while some_boolean_condition:
#         do something

x = 0
while x < 5:
    print(f'current value of x is {x}')
    x += 1
else:
    print("x is not less then 5")

# break, continue, pass

myList = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

for item in myList:
    pass

for item in myList:
    if item % 2 == 0:
        continue
    print(item)

for item in myList:
    if item == 5:
        break
    print(item)

x = 0
while x < 5:
    if x == 3:
        break
    print(x)
    x += 1
