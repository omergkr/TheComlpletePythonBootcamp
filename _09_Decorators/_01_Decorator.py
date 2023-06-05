def func():
    return 1


def hello():
    print("Hello")


greet = hello

hello()
greet()

del hello
# hello()
greet()  # we can call greet function even if hello function  was deleted


def hello(name="Jose"):
    print("The hello() function has been executed")

    def greet2():
        return "\t This is the greet() func inside hello"

    def welcome():
        return "\t This is the welcome() func inside hello"

    if name == "Jose":
        return greet2
    else:
        return welcome


my_new_func = hello("Jose")
print(my_new_func())

my_new_func2 = hello("Omer")
print(my_new_func2())


def cool():
    def super_cool():
        return "I am very cool"

    return super_cool()


some_func = cool()
print(some_func)


def hello3():
    return "Hi Jose"


def other(some_def_func):
    print("Other coder runs here ")
    print(some_def_func())


other(hello3)


def new_decorator(original_func):
    def wrap_func():
        print("some extra code before the original func")

        original_func()

        print("some extra code, after the original func")

    return wrap_func


def func_needs_decorator():
    print("i want to be decorated!!")


decorated_func = new_decorator(func_needs_decorator)
decorated_func()


@new_decorator
def func_needs_decorator():
    print("i want to be decorated!!")


func_needs_decorator()
