my_name = "Jose"
print(my_name + "Hallo")

# .format() method -> 'String here {} then also {}'.format('something1','something2')
# f-strings (formatted string literals) ->Float formatting follows "result: {value:{width}.{precision}}"


print("This is a string {}".format("INSERTED"))
print("The {} {} {} ".format("fox", "brown", "quick"))
print("The {2} {1} {0} ".format("fox", "brown", "quick"))
print("The {0} {0} {0} ".format("fox", "brown", "quick"))
print("The {q} {b} {f} ".format(f="fox", b="brown", q="quick"))


result = 104.234242342
print("The result was {r}".format(r=result))
print("The result was {r:1.3f}".format(r=result))

name = "Jose"
print(f"Hello, his name is {name}")

name = "Sam"
age = 3

print(f"{name} is {age} years old")