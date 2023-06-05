def add(n1, n2):
    print(n1 + n2)


add(33, 5)

number1 = 10
number2 = int(input("please provide a number: "))

try:
    # want to attempt this code
    # my have an error
    add(number1, number2)
except TypeError:
    print("hey it looks like you arent adding correctly!!")
else:
    print("ok")

try:
    f = open("test.txt", "r")
    f.write("write a test line 2")
except TypeError:
    print("hey. there was a typo error")
except OSError:
    print("hey. there was a OS error")
finally:
    print("hey. allways run")


def ask_for_int():

    while True:
        try:
            result = int(input("please provide number: "))
        except:
            print("hey, there was a typo error")
            continue
        else:
            print("Yes thank you")
            break
        finally:
            print("hey, i am going to ask you again")


ask_for_int()
