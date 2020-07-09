# Now, we will cover context managers.
# We already saw a context manager in action, when we opened a file

with open("s1_advanced_iterators.py") as h:
    pass

# context managers are extremly useful for managing resources. A file handle
# must always be closed. A lock must be always released. Now, we learn how to
# built our own contextmanager

class Greeter:
    def __init__(self, name):
        self._name = name

    def __enter__(self):
        print("Hello", self._name)
        pass

    def __exit__(self, type, value, traceback):
        print("Bye Bye")


with Greeter("Joe"):
    print("do something")


# a class which has implemented __enter__ and __exit__ methods fulfills the
# context manager protocol. Enter is called every time when the context manager
# is used with the 'with' statement. __enter__ can return something. you can refer to
# this via:

with Greeter("Bill") as g:
    print(g)

# in this particular case it will print 'None', because g did None (None is
# implicitly returned, when no return value is defined)
# __exit__ is called after the last statement in the with statement was
# executed. __exit__ takes several parameters, but this parameters won't matter
# us at the moment (you'll can look them up in the docs later)
# pythons standard library provides some cool contextmanagers
# you saw already with open(... for using files
# the contextlib defines some more

#suppress takes an exception type and catches this type of exceptions
from contextlib import suppress

with suppress(ValueError):
    raise ValueError()
print("I did not care")

# with contextlib.redirect_stdout you can specify a stream and all print output
# is redirected to this stream.

# lets revisit generator functions
# maybe we have 3 functions which must be invoked in the right order
def f1():
    print("1")

def f2():
    print("2")

def f3():
    print("3")

# if you swap the order, something very bad will happen
f1()
f2()
f3()
# generator functions can be used to enforce the right execution order

def f():
    yield f1()
    yield f2()
    yield f3()

f_order = f()
next(f_order)
next(f_order)
next(f_order)

# now, what if if youre f1 funcion opens a file and your f3 function closes a
# file. Do you see a similiarity to contextmanagers?
# however using the generator function like this with the next calls is
# cumbersome.


def f1(filename):
    return open(filename)


def f2(handle):
    return handle.close()

def filehandler(filename):
    h = f1(filename)
    yield h
    f2(h)

# lets define a contextmanager to handle the next call

class MyCtx:
    def __init__(self, handler_func):
        self._handler_func = handler_func

    def __call__(self, filename):  # __call__ is invoked if you use a class
        # instance like a function and try to call it 
        # ctx = MyCtx(42)
        # ctx("hello")
        self._handler_func = self._handler_func(filename)
        return self

    def __enter__(self):
        return next(self._handler_func)

    def __exit__(self, type, value, traceback):
        try:
            next(self._handler_func)
        except StopIteration:
            pass


filehandler = MyCtx(filehandler)
with filehandler("data.txt") as h:
    print(h.read())


# now, we have build our own version of a file open context manager, which
# automatically closes the file handle after usage. But didn't we see this
# pattern filehandler = MyCtx(filehandler) somewhere. Right, it is the
# decorator pattern.

# and if we rewrite our filehandler function a little bit and guard if with a
# try: finally clause, we get a nice working context manager

@MyCtx
def filehandler(filename):
    h = open(filename)
    try:
        yield h
    finally:
        h.close()

with filehandler("data.txt") as h:
    print(h.read())

# now we can easily build our own context managers with MyCtx. We just wrap a
# generator function which yields exactly ones and we are done. And 
# contextlib already contains a decorator for exactly this purpose 

from contextlib import contextmanager


@contextmanager
def greet(arg):
    print("hello")
    try:
        yield arg
    finally:
        print("bye")

with greet("Joe") as g:
    print(g)


# You have learned how context managers work and you have learned how to
# combine them with generator functions and decorators to build expressive and
# powerfull expressions



