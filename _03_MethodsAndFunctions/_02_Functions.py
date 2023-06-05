# def name_of_function(parameter):
#   ''' Docstring explains function'''
#   code
#   return

def add_function(num1, num2):
    """sum of two number"""
    return num1 + num2


result = add_function(3, 7)
print(result)


def is_even(number):
    return number % 2 == 0


print(is_even(20))


def get_even_number_list(num_list):
    """return all rhe even numbers un a list"""

    even_numbers = []
    for number in num_list:
        if number % 2 == 0:
            even_numbers.append(number)

    return even_numbers


from random import shuffle


def shuffle_list(my_list):
    shuffle(my_list)


def player_guess():
    guess = ''
    while guess not in ["0", "1", "2"]:
        guess = input("Pick a number: 0 ,1 or 2 ")

    return int(guess)


def check_guess(mylist, guess):
    if mylist[guess] == "O":
        print("correct")
    else:
        print("wrong guess")
        print(mylist)


cups = [' ', "O", " "]
shuffle_list(cups)
guess_index = player_guess()
check_guess(cups, guess_index)


