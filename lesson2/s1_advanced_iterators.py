# Iterators implement the iterator protocoll, that means: They have a __next__
# method. Every time __next__ is called the iterator returns a value and when
# it cannot return a value anymore a StopIteration is raised, which gives the
# caller of __next__ the signal to stop calling __next__ again and again. But
# why is this usefull.
# Well, first of all. Iterators provide lazyness
# Lets' take this example from the last lesson:

for i in range(1_000_000):
    if i>3:
        break

# range will only calculate the first 3 elements as needed instead of creating
# a list of 1 Million items and throwing away 999997 of them.

# Secondly, iterators are a powerful abstraction, which enable your
# datastructures to interact efficiently with the rest of the python ecosystem
# Iterators can be used in for loops, in tuple unpacking and they can be
# combined with other iterators to create more complex functions:
# Let's see how combined iterators work in action

items = ["red", "green", "yellow", "blue"]
for i, item in enumerate(items, start=10):
    print(i, item)

# you already saw enumerate. But now, we can explain better what it does.
# enumerate takes an iterator and a start value (default is 0) and returns a
# new iterator. The new iterator returns a tuple of a counter(starting at
# start) and the next item of the initial iterator.

# range creates an iterator which returns numbers from start to stop with in
# increments of step

# reverse takes a finite iterator and reverses it
for i in reversed(range(10)):
    print(i)

# I mentioned that reverse takes a finite iterator, because there are also
# iterators, which produce infinite sequences, without consuming infinite
# memory
# an example of an infinite iterator is count from the itertools module
from itertools import count
# for i in count():
#    print(i)
# execute at your own risk, this will run forever
# so pay attention when you use  infinite iterators and functions, which try to
# realize the whole sequency. Since this is impossible, because the sequency has
# inifinity elements, this will consume all your systems memory until it
# crashes

# you can create lists from iterators
l = list(range(10))
print(l)

from itertools import count
# list(count()) # do not run this

# zip takes 2 iterators and combines them into one
items1 = ["red", "green", "blue"]
items2 = ["square", "circle", "triangle"]
for i1, i2 in zip(items1, items2):
    print(i1, i2)

# filter takes an iteator and filters out all elements, where a predicate is
# False. predicate is a function which takes one argument (an item from the
# iterator) and returns True or False. If it returns False, the item will be
# filtered out

for i in filter(lambda x: x>5, range(10)):
    print(i)

# map takes a function and an iterator and applies the function to each element
# in the iterator and returns the result

for i in map(lambda x: x**2, range(10)):
    print(i)

# Since filter and map and other iterator functions take functions which
# recieve one argument. So if we have a function which takes more arguments we
# are doomed and cannot use it, or can we? Yes, we can!. There is a small,
# little function called partial which resides in the functools module
def less_than(x, y):
    return x < y
from functools import partial
less_than_3 = partial(less_than, y=3)
for i in filter(less_than_3, range(10)):
    print(i)

# partial takes a function and a couple of arguments and returns a function
# which partially applies this arguments to the function

# Now, that we know how usefull iterators are, lets learn how to implement them
# method1 generator comprehension
my_it = (i + 1 for i in range(10))
print(my_it)
for i in my_it:
    print(i)

#method2 generator expression
def squared_numbers(i):
    for i in range(i):
        yield i**2

for i in squared_numbers(10):
    print(i)

# generator expressions are something, which we haven't seen, yet.
# they are defined like a normal function, but instead of returning a value,
# they are yielding a value. The generator expression, will execute until a
# yield statement is reached. A value will be returned and the next time when
# the generator expression shall return another value. It resumes its execution
# at the yield statement, where it stopped the last time, and executes until
# the next yield statement is reached.

# Method 3. Implement the iterator protocol directly for an object.
# Before we examine this, let's have another look on the iterator protocol
# when we use a for loop like this:
for i in range(9):
    print(i)
# what happens is roughly this

it = iter(range(9)) # 1
while True:
    try:
        i = next(it) # 2
        print(i)
    except StopIteration: # 3
        break

# (1) first of all the iter function is called on the object (in this case object
# is the thing, which is returned by range(9)). iter wil call object.__iter__()
# and __iter__ will return an iterator. So we say, that object is an iterable.
# An iterable is anything, which has implemented the __iter__ method and
# returns an iterator.
# (2) we repeatedly call next on the iterator. next will call the __next__
# method and __next__ will return a value on each call. In general, an iterator
# is something, which has implement the __next__ method. In this case __next__
# will return 0 on it's first call, then 1, then 2 and so on. When the iterator
# is exhausted it must raise a StopIteration exception. The caller of the
# iterator  will watch out for the StopIteration and stop calling next(3). If
# __next__ will not raise a StopIteration, we have an infinite iterator.
# so now we are able to write an iterable object


class SquareValues:
    def __init__(self, stop):
        self._stop = stop  # we will produce square values up to stop
        self._current_value = -1

    def __iter__(self):  # (1)
        return self  # SquareValues is its own iterator, because it has
    # implemented a next method. So we can return self

    def __next__(self):  # (2)
        self._current_value += 1
        if self._current_value == self._stop:
            raise StopIteration()  # (3)
        return self._current_value ** 2
   

for i in SquareValues(10):
    print(i)


# The python interpreter knows one more way to produce an iterator.
# Every object which implements __len__ and __getitem__ is an iterator, too.
# Let's look, how this works.


class MyContainer:
    def __init__(self, a_list):  # for simplicity let's wrap a list
        self._list = a_list

    def __len__(self):
        return len(self._list)

    def __getitem__(self, index):
        return self._list[index]

container = MyContainer([1,2,3,4,5])
print(len(container))
print(container[0])
for i in container:
    print(i)

# __len__ returns the length of a sequency (the elements in a sequence). In
# this case MyContainer returns the number of elements, which it stores.
# __getitem__ should return an item for a given index. In this way, you obtain
# values from a list or dictionary for example. With both this methods present,
# the python interpreter can figure out, how to iterate over the object

# you may want to explore the builtin itertools and 3rd party more-itertools
# packages, which provide lots of usefull functions, when working with
# iterators



