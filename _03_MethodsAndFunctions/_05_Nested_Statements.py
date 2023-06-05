# LEGB
# L - local
# E - Enclosing function locals
# G - Global (module)
# B - Built-in (Python)
x = 25


def printer():
    x = 50
    return x


print(x)
print(printer())

name = "This is a global string"


def greet():  # enclosing funtion
    # Enclosing
    # name = "Sammy"

    def hello():
        # Local
        # name = "I am local"
        print("Hello " + name)

    hello()


greet()

# len built in

x = 50


# global keywords
def func():
    global x
    print(f"X is  {x}")

    x = "New Value"
    print(f"i just locally changed global X to {x}")


print(x)
func()
print(x)


def palindrome(s):
    s = s.replace(" ", "")
    return s == s[::-1]


print(palindrome("nurses run"))

# Pangrams are words or sentences containing every letter of the alphabet at least once

import string


def is_pangram(str1, alphabet=string.ascii_lowercase):
    alphabet_set = set(alphabet)
    s = str1.replace(" ", "").lower()
    s = set(s)
    return s == alphabet_set


print(is_pangram("The quick brown fox jumps over the lazy dog"))
