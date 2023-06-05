# Booleans are operators that allow you to convey True or False statements.
# These are very important later on when we deal with control flow and logic!

# True
# False

print(type(True))

my_file = open("test.txt")
print(my_file.read())

my_file.seek(0)
content = my_file.read()
print(content)

my_file.seek(0)
print(my_file.readlines())

my_file2 = open("C:\\Users\\ÖmerGöker\\Desktop\\test2.txt")
print(my_file2.read())
my_file.close()
my_file2.close()

with open("C:\\Users\\ÖmerGöker\\Desktop\\test2.txt") as my_new_file:
    contents = my_new_file.read()

print(contents)

# with open("test.txt", mode="r+") as my_new_file2:  # mode="r" w  a
#   contents2 = my_new_file.read()

with open("test.txt", mode="a") as my_new_file3:  # mode="r" w  a
    my_new_file3.write("\nfour")


with open("test.txt", mode="r") as my_new_file3:  # mode="r" w  a
    print(my_new_file3.read())

with open("test2.txt", mode="w") as my_new_file4:  # mode="r" w  a
    my_new_file4.write("i created this file")


with open("test2.txt", mode="r") as my_new_file5:  # mode="r" w  a
    print(my_new_file5.read())
    