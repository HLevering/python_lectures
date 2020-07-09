# we already learned, that functions are first class objects in Python and we
# learned that functions can accept other functions as parameters and return
# functions

# let's assume, we have the following function

def add(a, b):
    return a + b

# let's assume, that we want to write some html

def tagged(message):
    return f"<p>{message}</p>"

print(tagged(add(1, 2)))

# now we can print our tagged result, but we have to use tagged every time
# together with add

#lets write another function

def tagged1(func):
    def tagged_func(arg1, arg2):
        return f"<p>{func(arg1, arg2)}<p>"
    return tagged_func

add = tagged1(add)
print(add(1,2))
print(add(2,2))

# Lets pause for a moment. We created a function that takes another function,
# wrapped it another function and returned the wrapped version and assigned to
# the initial function name. Now, we have a new function that not only
# calculates the addition but also tagges the result in html. This pattern:
# 1. call a function with a function
# 2. return a new function
# 3. assign the new function to original function name
# is called decorator pattern and it is so common that we have a special
# syntax for it

def tagged(func):
    def tagged_func(arg1, arg2):
        return f"<p>{func(arg1, arg2)}<p>"
    return tagged_func

@tagged
def add(a, b):
    return a + b

print(add(1,2))

# the @tagged is syntactic sugar for the above mentioned 3 steps
# now we are able to tag further functions
@tagged
def sub(a, b):
    return a - b

print(sub(2,1))

# but there is one problem, what happens, if we want to tag other functions
# which do not take exactly 2 arguments


@tagged
def squared(a):
    return a**2

#print(squared(2))  # this will fail

# However, if we change our tagged function a little bit ...

def tagged(func):
    def tagged_func(*args, **kwargs):
        return f"<p>{func(*args, **kwargs)}<p>"
    return tagged_func

# it can decorate every function, no matter what kind of parameters this
# function expects

@tagged
def squared(a):
    return a**2

print(squared(2))  # now, this will work

# there is one further problem. After decorating the squared function its
# original name has vanished
print(squared)
# The functools module provides a decorator wraps, which conserves the original
# function name (and some further attributes)

from functools import wraps
def tagged(func):
    @wraps(func)
    def tagged_func(*args, **kwargs):
        return f"<p>{func(*args, **kwargs)}<p>"
    return tagged_func

@tagged
def squared(a):
    return a**2

print(squared(2))
print(squared)
# now, the function's name will stay the same

# Let's go one step further. We can only tag functions with a <p> tag, which is
# in some kind limiting. If we add one further layer, we can solve this
# problem, too

from functools import wraps
def tagged(tag):
    def tag_with_tag(func):
        @wraps(func)
        def tagged_func(*args, **kwargs):
            return f"<{tag}>{func(*args, **kwargs)}</{tag}>"
        return tagged_func
    return tag_with_tag

@tagged("h1")
def squared(a):
    return a**2

print(squared(2))

# now, we have a flexible tagged function
# decorators are a powerfull tool, which enable you to combine orthogonal
# functionality in your program

@tagged("h1")
@tagged("p")
def squared(a):
    return a**2

print(squared(2))

# the functools module provides some decorators
# lru_cache caches a function result and returns the cached value on subsequent
# calls
from functools import lru_cache
from time import sleep


@lru_cache()
def expensive_job(arg):
    sleep(2)  # wait for 2 seconds
    return arg

print(expensive_job(42))
print(expensive_job(42))

# we already saw @wraps which is used in function decorators to preserve names.
# Checkout the docs for functools to discover more usefull stuff





