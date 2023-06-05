def myfunc(a, b):
    return (a + b) * 0.05


x = myfunc(40, 60)
print(x)


def myfunc2(*args):
    return sum(args) * 0.05


def myfunc3(*args):
    for item in args:
        print(item)


print(myfunc2(2, 5, 7, 8, 90, 100))
myfunc3(2, 5, 7, 8, 90, 100)


def myfunc4(**kwargs):
    print(kwargs)
    if "fruit" in kwargs:
        print("My fruit of choice is {}".format(kwargs["fruit"]))
    else:
        print("i did not find any fruit here")


myfunc4(fruit='apple', veggie="lettuce")


def myfunc5(*args, **kwargs):
    print(args)
    print(kwargs)
    print("i would like {} {}".format(args[0], kwargs["food"]))


myfunc5(10, 20, 30, fruit="orange", food="eggs", animal="dog")


def myfunc6(text):
    changed_text = ''
    for i in range(len(text)):
        if i % 2 == 0:
            changed_text += text[i].lower()
        else:
            changed_text += text[i].upper()
    return changed_text


print(myfunc6("OmerGoker"))

myTuple = ("John", "Peter", "Vicky")

x = "#".join(myTuple)

print(x)

myDict = {"name": "John", "country": "Norway"}
mySeparator = "TEST"

x = mySeparator.join(myDict)

print(x)


def summer_69(arr):

    sum_num = 0
    del arr[arr.index(6): arr.index(9) + 1]
    for num in arr:
        sum_num += num
    return sum_num


array = [3, 8, 4, 5, 6, 7, 15, 11, 10, 8, 9, 10]
print(summer_69(array))
