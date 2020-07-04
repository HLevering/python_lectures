# functions are an important part of python programming. Functions are used to
# seperate your program in small building blocks. These building blocks are
# then combined to provide more complex features.

# a function is defined in the following way:


def a_function_name(arg1, arg2):
    print(arg1, arg2)
# arg1 and arg2 are parameters. Use don't need to define functions, that take
# parameters
# a function is called by writing its name and providing the parameters in
# parenthesis

a_function_name("i like", 3)
# here "i like" and '3' are positional arguments, because these values are
# bound the function parameters by its position

# python also provides so called keyword arguments:

a_function_name(arg2="i like", arg1=3)

# keyword arguments have two advantages:
# 1. they are more readable , e.g. consider the following call
# my_func(1,0,2,True)
# 2. they give you the ability to change the order of parameters without the
# need to change your function calls

# python also let you define functions, which take an arbitrarely amount of
# parameters

def my_sum(*numbers):
    print(sum(numbers))

my_sum(1, 2, 3, 4, 5)

# in the example above *numbers is a list of positional arguments

def my_pairs(**pairs):
    for key, value in pairs.items():
        print(key, value)

my_pairs(size="small", color="red")

# in the example above **pairs is dictionary of keyword arguments (it is often
# defined and refered to as **kwargs (short for keyword arguments)
# you can define functions which take arbitrarely amounts of positional and
# keyword arguments, too. 
# in this case the positional arguments have to be defined first, and 

def my_func(*numbers, **pairs):
    print(numbers, pairs)
    pass

my_func(1,2,3, a=3)

# if you use the asterix * operator without a name in a function definition,
# than all arguments after the * have to be provided as keyword arguments. They
# are so called "keyword only arguments"

def keyword_only(*, arg1, arg2, **kwargs):
    pass

# arbitrarely keywordarguments are always defined as the last parameter

# keyword_only(1,2) # invalid function call

# on the other side it is possible to define positional only parameters:

def positional_only(a, b, /):
    pass

#inavlid  positional_only(a=2, b=4)
# positional arguments must be the first parameters in the parameter list
# followed by a '/'
# if you define positional arguments, then their names are available as
# parameter names together with the **kwargs parameter
# so the following is valid
def cool_func(a, /, **kwargs):
    print(a, kwargs)

cool_func(0, a=1)

# you can also define default values for function parameters
def default_params(a, b=2,*,c, d=4, **kwargs):
    print(a, b, c, d, kwargs)

default_params(1, c=3, e=5)

# default parameters must be provided from right to left. **kwargs parameter
# has no default value. you can provide default parameters for 'keyword only'
# and 'non keyword only' parameters independently

# functions are first class objects in python. So they can be used as a
# variable and you can define functions that take functions and functions that
# return functions

def doer(func, arg):
    func(arg)

doer(print, "hello functional")

def dispatch(arg):
    if arg == 1:
        return max
    else:
        return sum

print(dispatch(1)([1,2,3]))
print(dispatch(0)([1,2,3]))

# sometimes you want to bind a function to a variable or pass it as a function
# parameters without declaring the function
# For this cases we have lambdas
s = lambda arg1, arg2: arg1 + arg2
# a lambda is defined with the lambda keyword followed by the parameters it
# takes, a colon ":" and an expression. The result of the expression is the
# result of the lambda. Because we cannot define any statements in lambda.
# lambdas are normally used define short, simple functions
print(s(1,2))
# lambda is not a very expressive name. A better name for lambda would have
# been "make function"
# The statement "s = lambda arg1, arg2: arg1 + arg2" can be read as:
# make a function which takes two parameters (arg1 and arg2) and returns the
# result of the expression arg1 + arg2








