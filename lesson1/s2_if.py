# the if statement is used to conditionally execute one branch of code or
# another
if 5>4:
    print("5>4")

# it can have an optional else clause
if 2 > 3:
    pass
else:
    print("2 < 3")

# you can chain multiple conditions
if 2 >3:
    pass
elif 3> 3:
    pass
else:
    print("4>3")

# the code behind the if is executed, if a condition is True. If the condition
# is False, then the else branch is executed depending on if it was specified
# There are values which are interpreted as a false condition:

# the obvious one
if False:
    print("wont print")

#null type
if None:
    print("wont print")

#0 value
if 0:
    print("wont print")

#the empty string
if "":
    print("wont print")

#the empty list and also the empty set, dictionary and tuple
if []:
    print("wont print")

# other values are interpreted as True 
# objects can define a special bool method, which is used to determine the
# truthiness of an object. We'll cover this later

# comparison for equality
# python provides 2 methods to check if 2 objects are equal
# the equality operator "==" and the identity operator "is"
# they have different semantics
# "==" is used to check if two objects have the same values. e.g. 
# one_dollar == one_dollar should be true. They are considered equal if their
# values(amount) are the same even if these are two different notes of amount one
# dollar
# on the other hand identity is used to check if two objects are the same
# Person("George") is Person("George") should be only True if it is the same
# person. And if there are two different persons, who have incendently the same
# name it should be False



# if you want to check multiple conditions, than you can use the and, or and
# not operator

if 3>2 and 2>1:
    # both conditions must be true
    print("this is damn true")

if  1>2 or 3 >2:
    # at least one condition must be True
    print("this is true, too")

if not 1>2:
    print("not inverts a boolean value from True to False or False to True")

# if want to check if a number is in a certain range, python supports an
# intuitive syntax
a = 3
if  1< a < 5:
    print("in range")
    # this would fail in C++ and other languages, but works in python

#comparison operators
# < less
# <= less equal
# > bigger
# >= bigger equal

# logical operators
# and
# or
# not

# logical operators will return the value which caused the statement to be True
# this can be used in a pattern to initialize variables
x = [] or 4
# x will be 4
# or returns the first value which is True

# you can use if statements in other statements and expressions
# E.g. during assignment
x = 5 if True else 2
# x == 5
# or in list comprehension
even_values = [ x for x in range(10) if x % 2 == 0]
print(even_values)





