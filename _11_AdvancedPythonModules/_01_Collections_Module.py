from collections import Counter

mylist = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2, 2, 3, 3, 3, 3, 3, 3]
print(Counter(mylist))  # Counter({1: 12, 3: 6, 2: 2})
print(Counter("aaaabbbbbbbbbccccccceeeeeeee"))

sentence = "How many times does each word shoe up in this sentence with a word"
print(Counter(sentence.lower().split()))

letters = "aaabbbbbbbbbbbssssssssssskkkkkkkk"
c = Counter(letters)
print(c.values())
print(c.keys())
print(c.most_common(3))
print(list(c))
print(list(c.keys()))
print(list(c.values()))

from collections import defaultdict

d = defaultdict(lambda: 0)
d["correct"] = 100
print(d["correct"])
print(d["wrong key!!!"])

mytuple = (10, 20, 30)
print(mytuple[0])

from collections import namedtuple

Dog = namedtuple("Dog", ["age", "breed", "name"])
sammy = Dog(age=5, breed="Husky", name="Sam")
print(type(sammy))
print(sammy)
print(sammy.age)
print(sammy[0])
