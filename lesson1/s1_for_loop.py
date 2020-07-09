# let's have a deeper look on for loops
# the traditional way in C would be to write a for loop in this way
# for (int i=0, i<10, i++){
#   do_something()
#}
# let's say we have a list and want to print each element

letters = ["a", "b", "c", "d", "e"]
# the c++ way
for i in range(len(letters)):
    print(letters[i])

    # len returns the length of a collection
    # range(n) returns a collection from zero to n-1 [0, 1, ..., n-1]

# There is a better way:
# However, python's for loop works different. It is a "foreach" loop. It takes
# a collection and iterates through each element of the collection
for letter in letters:
    print(letter)

# But now we lost our index i. If we need the index in the loop we can retain
# it with enumerate
for i, letter in enumerate(letters):
    print(i, letter)

# one note to range
# what happens, if you want to iterate from 0 to 1000000. 
for i in range(1_000_000):
    pass

# if range would build a collection, that would be at least 4 MB of memory
# (with a native 32bit int, with pyton objects even much more)
# this could hurt performance, if called often ( nd it screws up your cpu
# cache)
# So since Python3 range is lazy and does not return a list, but an object
# which return one element after elment on demand. This is especially handy,
# when you do not need to process all elements of list
for i in range(1_000_000):
    if i > 3:
        break
        # the break commands quits a for loop

# On each step the for loop will ask the range object: "give me the next value"
# and range will calculate and hand over the next value to the for loop without
# having allocated all 1 mio. elements
# Later we will see, that a for loop is very generic and works on every object,
# which can provide a "next value". The correct term is: the object must
# fulfill the "iterator protocol"
# This makes the for loop very powerful

# if you want to skip a step you can use the continue keyword
print("skip 3 element")
for i in range(10):
    if i==3:
        continue
    print(i)

# there is one further form of a for loop. It can have an else clause
values = [1, 2, 3 ,4]
to_find = 5
for value in values:
    if value == to_find:
        break
else:
    print("did not found", to_find, "in", values)

# the else clause will be executed if the for loop was not stopped by a break
# prematurely. A better name for the else would have been "nobreak". Then the
# intention would have been clearer
# the else clause isn't that comman and also not widely known, but it is
# usefull for algorithms which try to find a condition in a collection

# The for loop is also used in so called list comprehensions
some_list = [i for i in range(10)]
print(some_list)
# some_list == [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
# a list comprehension is a short way to create a list, which is already filled
# with certain values
# the same works for dictionaries, too
my_dict = {i: "some_value" for i in range(3)}
print(my_dict)
# my_dict == {0: "some_value", 1: "some_value"}


# In Python there is another loop construct. The while loop

#while condition_is_true:
#    do_something

i=0
while i<3:
    i += 1










