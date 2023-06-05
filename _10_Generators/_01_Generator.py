"""
A generator expression is like a list comprehension,
but instead of finding all the items you're interested and packing them into list,
it waits, and yields each item out of the expression, one by one.
Because a generator expression only has to yield one item at a time,
bit can lead to big savings in memory usage.
Generator expressions make the most sense in scenarios where you need to take one item at a time,
do a lot of calculations based on that item,
and then move on to the next item. If you need more than one value,
you can also use a generator expression and grab a few at a time.
If you need all the values before your program proceeds, use a list comprehension instead.
"""


def create_cubes(n):
    result = []
    for x in range(n):
        result.append(x ** 3)
    return result


for x in create_cubes(10):
    print(x)

print(list(create_cubes(5)))


def create_cubes_yield(n):
    for x in range(n):
        yield x ** 3


for x in create_cubes_yield(10):
    print(x)

print(list(create_cubes_yield(5)))


def gen_fibon(n):
    a = 1
    b = 1
    for i in range(n):
        yield a
        a, b = b, a + b


for number in gen_fibon(10):
    print(number)


def gen_fibon2(n):
    a = 1
    b = 1
    output = []

    for i in range(n):
        output.append(a)
        a, b = b, a + b
    return output


for number in gen_fibon2(10):
    print(number)


def sample_generator():
    for x in range(3):
        yield x


print(type(sample_generator()))
g = sample_generator()

print(next(g))
print(next(g))
print(next(g))
# print(next(g)) -> stop iteration


s = "hello"
s_iter = iter(s)
print(next(s_iter))
print(next(s_iter))
