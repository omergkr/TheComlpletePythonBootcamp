from random import shuffle, randint

myList = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
for num in myList:
    print(num)

for num in myList:
    if num % 2 == 0:
        print(num)
    else:
        print(f'Odd number: {num}')

list_num = 0
for num in myList:
    list_num += num
    print(list_num)
print(list_num)

for letter in "Hello World":
    print(letter)
    print(letter.upper())

for _ in "Hello World":
    print("Cool")

tup = (1, 2, 3)
for item in tup:
    print(item)

myList = [(1, 2), (3, 4), (5, 6)]
print(len(myList))

for item in myList:
    print(item)

for item in myList:
    print(item[0])

for (a, b) in myList:
    print(a)
    print(b)

for a, b in myList:
    print(a)
    print(b)

d = {'k1': 1, 'k2': 2, 'k3': 3}

for item in d:
    print(item)

for item in d.items():
    print(item)

for key, value in d.items():
    print(key)
    print(value)

for item in d:
    print(d[item])

for value in d.values():
    print(value)

# range
# for (int i=10; i>=0; i--) {
#    System.out.println(i);
# }
for i in range(10, -1, -1):
    print(i)

for i in range(10):  # 0 1 2 ..... 9
    print(i)

for i in range(0, 11, 2):  # 0 2 4..... 8 10
    print(i)

list(range(0, 11, 2))
print(list(range(0, 11, 2)))

for i in range(10, 0, -2):
    print(i)

# Enumerate

index_count = 0

for letter in "abcdefgh":
    print("At index {} the letter is {} ".format(index_count, letter))
    index_count += 1

index_count = 0
word = "abcdefgh"
for letter in word:
    print(word[index_count])
    index_count += 1

for item in enumerate(word):
    print(item)

for index, letter in enumerate(word):
    print(index)
    print(letter)
    print("\n")

myList1 = ["a", "b", "c"]
myList2 = [1, 2, 3]

for item in zip(myList2, myList1):
    print(item)

print(list(zip(myList2, myList1)))

print("x" in [1, 2, 3])
print("x" in ["x", "y", "z"])
print("x" in "x is a letter")
print("mykey" in {'mykey': 234})

dic = {'my_key': 234}
print(234 in dic.values())

myList = [10, 20, 30, 40, 100]
print(min(myList))
print(max(myList))

shuffle(myList)
print(myList)

randint(0, 100)
print(randint(0, 100))  # 0.... 100

# result = input("what is your number?")
# print(type(result))
# print(result)

myString = "Hello"
myList3 = []
for letter in myString:
    myList3.append(letter)

print(myList3)

myList4 = [letter for letter in myList3]
print(myList4)
myList5 = [x for x in range(0, 10)]
print(myList5)
myList5 = [x ** 2 for x in range(0, 11)]
print(myList5)
myList5 = [x ** 2 for x in range(0, 11) if x % 2 == 0]
print(myList5)
celcius = [0, 10, 20, 34.5]
fahrenheit = [((9 / 5) * temp + 32) for temp in celcius]
print(fahrenheit)

results = [x if x % 2 == 0 else "ODD" for x in range(0, 11)]
print(results)
results = [x * y for x in range(1, 11) for y in range(1, 11)]
print(results)

