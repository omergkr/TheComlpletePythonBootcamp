"""Phone Number
(555)-555-5555
Regex Pattern
r”(\d\d\d)-\d\d\d-\d\d\d\d”
r”(\d{3})-\d{3}-\d{4}”
"""
import re

text = "The agent's phone number is 408-555-1234. Call soon!"
print("phone" in text)

pattern = "phone"
print(re.search(pattern, text))

pattern = "Not in Text"
print(re.search(pattern, text))

pattern = "phone"
match = re.search(pattern, text)
print(match.span())
print(match.start())
print(match.end())

text2 = "my phone once, my phone twice "
match = re.search(pattern, text2)
print(match)  # it only turns back first match

matches = re.findall(pattern, text2)
print(matches)
print(len(matches))

for match in re.finditer(pattern, text2):
    print(match)
    print(match.span())
    print(match.group())

"""
Character	Description	        Example Pattern Code	Exammple Match
\d	        A digit	            file_\d\d	            file_25
\w	        Alphanumeric	    \w-\w\w\w	            A-b_1
\s	        White space	        a\sb\sc	                a b c
\D	        A non digit	        \D\D\D	                ABC
\W	        Non-alphanumeric	\W\W\W\W\W	            *-+=)
\S	        Non-whitespace	    \S\S\S\S	            Yoyo
"""

text = "My telephone number is 408-555-1234"

phone = re.search(r'\d\d\d-\d\d\d-\d\d\d\d', text)
print(phone)
print(phone.group())

# Quantifiers
"""
Character	Description	                Example Pattern Code	    Exammple Match
+	            Occurs one or more times	Version \w-\w+	            Version A-b1_1
{3}	            Occurs exactly 3 times	    \D{3}	                    abc
{2,4}	        Occurs 2 to 4 times	        \d{2,4}	                    123
{3,}	        Occurs 3 or more	        \w{3,}	                    anycharacters
\*	            Occurs zero or more times	A\*B\*C*	                AAACC
?	            Once or none	            plurals?	                plural
"""

phone = re.search(r'\d{3}-\d{3}-\d{4}', text)
print(phone)
print(phone.group())
print()

phone_pattern = re.compile(r'(\d{3})-(\d{3})-(\d{4})')
results = re.search(phone_pattern, text)
print(results.group())
print(results.group(1))
print(results.group(2))
print(results.group(3))

# Or operator |
match2 = re.search(r"man|woman", "This man was here.")
print(match2)
match3 = re.search(r"man|woman", "This woman was here.")
print(match3)

# The Wildcard Character
match4 = re.findall(r".at", "The cat in the hat sat here.")
print(list(match4))
match4 = re.findall(r"...at", "The bat went splat")
print(list(match4))
match4 = re.findall(r'\S+at', "The bat went splat")
print(list(match4))
match4 = re.findall(r'^\d', "1 is a number")
print(list(match4))
match4 = re.findall(r'\d$', "1 is a number 2")
print(list(match4))


phrase = "there are 3 numbers 34 inside 5 this sentence."
pattern = r'[^\d]+'
print(re.findall(pattern, phrase))

test_phrase = 'This is a string! But it has punctuation. How can we remove it?'
clean = re.findall('[^!.? ]+', test_phrase)
print(clean)
print(" ".join(clean))


phrase = "there are 3 numbers 34 inside 5 this sentence."
pattern = r'[^\D]+'
print(re.findall(pattern, phrase))

text = 'Only find the hypen-words in this sentence. But you do not know how long-ish they are'
# print(re.findall(r'[\w]+-[\w]+', text))
print(re.findall(r'\w+-\w+', text))


text = 'Hello, would you like some catfish?'
texttwo = "Hello, would you like to take a catnap?"
textthree = "Hello, have you seen this caterpillar?"

print(re.search(r'cat(fish|nap|claw)', text))
