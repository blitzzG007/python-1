def hello():
    print('Hello World')


hello()  # terminal output = Hello World


def create_name(first, last):
    first = first.capitalize()
    last = last.capitalize()
    return first + " " + last


full_name = create_name("Jack", "Cent")

print(f'Hello my name is {full_name}')  # terminal output = Jack Cent


def name(firstname, lastname):
    firstname = firstname.upper()
    lastname = lastname.upper()
    return firstname + " " + lastname


my_full_name = name("Scott", "Summers")
print(my_full_name)  # terminal output = SCOTT SUMMERS


# Local scope means that a variable declared inside a function or class can only be accessed within that function or class.
def my_func():
    my_var = "Something to say"
    print(my_var)


my_func()


# Enclosing scope means that a function that's nested inside another function can access the variables of the function it's nested within.
def outer_msg():
    msg = "Hello there friend"

    def inner_msg():
        print(msg)

    inner_msg()


outer_msg()


def outer_func():
    message = "What do you wanna do to day?"
    res = ""

    def inner_func():
        nonlocal res
        res = "And also what do wanna eat for lunch and dinner later?"
        print(message)

    inner_func()
    print(res)


outer_func()

# Global scope refers to variables that are declared outside any functions or classes which can be accessed from
# anywhere in the program. Here, my_test can be accessed anywhere, even inside a function it's not defined in
my_test = "This is a test"


def show_test():
    print(my_test)


show_test()

# And if you want to make a locally scoped variable defined inside a function globally accessible,
# you can use the global keyword:
my_Test_1 = "Different test"


def test_show():
    global is_an_int
    global my_Test_2
    my_Test_2 = 50
    is_an_int = str(my_Test_2)
    print(my_Test_1)
    print(is_an_int)


test_show()
print("'my_Test_2' is now a global variable and can be accessed anywhere in the program: " + is_an_int)

# You can also use the global keyword to modify a global variable
my_var_test = 30


def change_global():
    global my_var_test  # Allows modification of a global variable
    my_var_test = 10


change_global()
print(my_var_test)



# Built-in scope refers to all of Python's built-in functions, modules, and keywords, and are available anywhere in your program
print(str(45)) # '45'
print(type(3.14)) # <class 'float'>
print(isinstance(3, str)) # False