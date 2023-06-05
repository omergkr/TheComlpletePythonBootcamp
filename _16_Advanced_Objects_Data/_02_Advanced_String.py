s = 'hello world'
print(s.capitalize())
print(s.upper())
print(s.lower())
# Remember, strings are immutable.
# None of the above methods change the string in place,
# they only return modified copies of the original string.
s = s.upper()
print(s)

print(s.count('O'))  # returns the number of occurrences, without overlap

print(s.find('O'))  # returns the starting index position of the first occurrence

print(s.center(20, 'z'))

print('hello\thi'.expandtabs())
print('hello\thi')


s = 'hello'
# isalnum() will return True if all characters in s are alphanumeric
print(s.isalnum())

# isalpha() will return True if all characters in s are alphabetic
print(s.isalpha())

# islower() will return True if all cased characters in s are lowercase and there is at least one cased character in s,
# False otherwise.
print(s.islower())
# isspace() will return True if all characters in s are whitespace.
print(s.isspace())
# istitle() will return True if s is a title cased string and there is at least one character in s,
# i.e. uppercase characters may only follow uncased characters and lowercase characters only cased ones.
# It returns False otherwise.
print(s.istitle())
# isupper() will return True if all cased characters in s are uppercase
# and there is at least one cased character in s, False otherwise.
print(s.isupper())
# endswith() which is essentially the same as a boolean check on s[-1]
print(s.endswith("o"))

# split() to split the string at a certain element and return a list of the results.
print(s.split("e"))
# partition() to return a tuple that includes the first occurrence of the separator sandwiched
# between the first half and the end half.
print(s.partition('l'))
