# So you decided to learn Python.
# A good choice. Python is the 2nd most popular language (2020, right behind
# JavaScript).
# In contrast to languages like C or C++, Python is an interpreted language.
# You'll need a python interpreter to run your programs, but once you've
# written a program it can be (almost) run on any platform, which has a python
# interpreter installed ("write once, run anywhere") 
# Compared to other languages, python may be considered "slow" because of it is
# an dynamic, interpreted language. However, with today's hardware python is
# fast enough for a vast variety of programming tasks. It can be used either
# for small scripts or for a backend of a internet site like instagram. It is
# widely used in the machine learning data science domain. But enough said for
# now. Let's start programming

# the first thing to grasp is, that in python variable names are references to
# objects

x = 5
print("x", x)
# x points to an object representing the value 5
# the next statement won't change the value 5, but x is now pointing to the
# value 6
x = 6
print("x", x)

x=5
y=x
x=6
print("x", x, "y", y)
# Now it should be clear that x is pointing to a new value instead modifying 5
# in place. Otherwise y would be 6, too.
# So in other words:
# The assignment operator "=" does to change the value of a name, but it
# let point the name to a new object

# python has a bunch of arithmetic operators
print("1+2=", 1+2)
print("1-2=", 1-2)
print("1*2=", 1*2)
print("1/2=", 1/2)
print("2**2=", 2**2)
print("7%4", 7%4, "remainder")
print("7 // 4", 7//4, "integer division")

# python * / operators have precedence over + - like you would expect it from
# math
print( "3 + 2 * 2" , 3+2*2)

# python has a set of builtin types
a_string = "hello"
a_special_char_does_not_exist = "c" 
an_int = 42
a_float = 1.0
complex_numbers = 4 + 4j
#booleans
a = True
b = False
# a null type
c = None

# collections
a_list = [1, 2, 3, 4]
# you can access elements by index with 
print("first element of list", a_list[0])
# the first index starts at 0 and the last index is the length of the list -1
print("length of list", a_list)
print("last element of list", a_list[-1])
print("slice of a list", a_list[2: 5]) # including element at index 2,
#excluding index 5


# collection types
a_key_value_map = {"a": 1, "b": 2}
# In python it is called a "dictionary" are short just "dict"
# access a value by key
print(a_key_value_map["a"])
a_set_of_unique_values = {1, 2, 3}
a_tuple_of_values = (1,2,3)
# the collection types can be arbitrarily nested.
person = {"name": "Walter",
          "likes": ["Pizza", "Cola"]}
# and compared to normal variables. collection types can be mutated in place
a_list.append(5)
print(a_list)


# Control flow operators
for i in range(10):
    print(i)

# python uses indention to define scopes. By convention every scope is indented
# by 4 whitespaces each. Tabs are not used (so it makes sense to configure your
# editor to replace a tab by 4 whitespace characters
for x in range(3):
    #scope of outer for loop:
    for y in range(3):
        #scope of inner for loop:
        print("x",x, "y", y)

# conditional
if 5 == 5:
    print("yeah")
else:
    print("nop")

# use a resource, e.g. read file content
with open("data.txt") as my_file:
    print(my_file.read())
    # the file is closed  automatically

# catch errors
try:
    # an expression that might fail
    5 / 0
except ZeroDivisionError: 
    # catch the error. in this case a ZeroDivisionError error and handle it
    print("only Chuck Norris can divide by zero")
finally:
    # this executed allways
    print("some cleanup which must be done every time")


#define a function
def a_function_name(parameter1, another_parameter):
    # since python is a dynamic language, you do not  have to specify types,
    # but you can (we'll cover this later)
    print(parameter1, another_parameter)

#invoke a function
a_function_name(3, 4)


#define a class
class A:
    def __init__(self, a):
        # self represents an instance of class A
        # define a member variable
        self.a = a

    # define a method
    def my_print(self):
        # use member variable
        print(self.a)

    def do_nothing(self):
        # the pass statement does nothing and is used when the python syntax
        # expects a statement. like in this case ...
        pass

#make an instance of a class
my_a = A(100)
#invoke a method
my_a.my_print()
# you don't have to pass self as an argument. Self is passed implicitly as the
# first argument by the python interpreter

# One last thing for this lesson:
# pythons dynamic nature gives the programer much freedom and enforces very
# little. Therefore, there are some convetions for naming things to show the 
# intention of a variable
# class names are
class CamelCase:
    pass
# variables are small with under scores
my_var = 5
# a variable which should be considered as constant is CAPITALIZED
MY_CONST = 42

# Task:
# - Write a datastructure that contains information about a person:
#   name, fullname, adress, hobbies
#   a) using maps and list
#   b) using classes
#
# - write a function that calculates the first 10 fibonacci numbers 
#   1 1 2 3 5 8 13 21 ...

# scroll down for solutions








































# 1a
my_person = {"name": "Jack",
             "fullname": "Spearow",
             "address": {"street": "island street",
                        "street number": 42,
                        "city": "Port Royal"},
             "hobbies": ["fighting", "stealing"]}

# 2b


class Address:
    def __init__(self, street, street_number, city):
        self.street = street
        self.street_number = street_number
        self.city = city

class Person:
    def __init__(self, name, fullname, address, hobbies):
        self.name = name
        self.fullname = fullname
        self.address = address
        self.hobbies = hobbies

my_person_2 = Person("Brad", "Pitt", Address("Hollywodd", 1, "L.A."),
        ["acting"])

#2
def fib():
    x, y = 1, 1
    numbers = []
    for i in range(10):
        numbers.append(y)
        x, y = x+y, x
    return numbers
print(fib())
             












