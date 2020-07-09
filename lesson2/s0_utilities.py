# in the last sesson we rushed through the basics of the python language
# In this lesson we'll start with some helpfull utilities, before we'll dive
# into the more advanced language features

# iter with 2 arguments
for user_input in iter(input, ""):
    print("user typed in", user_input)
# iter can take two arguments. the first one is a function which takes no
# arguments. the 2nd argument is a sentinel value
# For each step in the forloop the defined function will be called. The return
# value of the function is compared to the sentinel value. If it is the
# sentinel value, the for loop will stop. Otherwise the forloop will use the
# return value in its current iteration step. This is particularly usefull when
# dealing with old C-style APIs

# looping throug dictionaries there are multiple ways to loop through a
# dictionary.
# The first one will iterate through the keys

my_dict = {"color": "red", "size": "medium", "count": 42}

for key in my_dict:
    print(key)

# use the .values() method to iterate through the values of a dictionary.

for value in my_dict.values():
    print(value)

# use .items() to iterate through keys and values at the same time
for key, value in my_dict.items():
    print(key, value)

# iterate through the keys again
for key in my_dict.keys():
    print(key)

# what is the difference between in my_dict.keys() and in my_dict you may ask?
# In python 3 there is none, but the former is shorter to write
# If you want to add / delete items to the dictionary while iterating over it,
# you'll have to make a copy of the keys. Otherwise you will modify an iterator
# while using it and you deserve what you get.

my_dict = {"color": "red", "size": "medium", "count": 42}
for key in list(my_dict):
    if key == "color":
        del my_dict[key]  # remove the entry

print(my_dict)

# as you saw in the previous example 
del my_dict["size"]  # will delete the entry "red" from the dictionary

# the module collections offers further datastructures, which we didn't cover
# yet. One of it is defaultdict, but feel free to go to the docs and discover
# the others by your own
# defaultdict takes a type and will construct a new instance of this type
# everytime when a key is not available in the dict

from collections import defaultdict
my_dict = defaultdict(list)
print(my_dict)
my_dict["foo"].append("bar")
print(my_dict)

# Why is this usefull? One usecase is a "groupby" function
from collections import defaultdict
items = [("red", "house"), ("red", "appel"), ("green", "gras"), ("blue",
    "ocean")]
groupby = defaultdict(list)
for color, item in items:
    groupby[color].append(item)
print(groupby)

# another usefull datastructure is ChainMap
# let's assume that we have a couple of options from different sources
# some defaults
default_options = {"verbose": True, "debug": False, "background": "light"}
# some environmens var options
env_options = {"background": "dark", "debug": True}
# some options set via cmd line
cmd_options = {"debug": False, "user": "Walter"}
# ChainMap allows you to combine all these options and let take cmd_options
# precedence over env_options and env_options precedence over default_options
from collections import ChainMap
chain_map = ChainMap(cmd_options, env_options, default_options)
print(chain_map["debug"])
print(chain_map["background"])
print(chain_map["verbose"])
# ChainMap takes a bunch of maps and it tries to lookup a key in the first map.
# If it does not find the key, then it will try to lookup the key in the second
# map, then in the 3rd map and so on and if the key isn't found in none of
# these it will raise ValueError

# tuple unpacking. tuples have a superpower called tuple unpacking. You already
# saw it multiple times, when we were iterating over a collection in a for loop
# See how it works
point = (1, 2, 3)
x, y, z = point
print(x,y,z)
# the same will work with lists, too, but since lists can change in size
# it will fail, when the number of elements on the left hand and right hand side do not
# match. Therefore you can use tuple unpacking together with the * operator,
# which will catch all remaining elements in one list:

x, *rest, z = point
print(x, rest, z)

# in general tuple unpacking will work with any iterable, as long as the length
# of the iterable and the number of elements (consider * operator) match.

cmd_options = {"debug": False, "user": "Walter"}
opt1, opt2 = cmd_options
print(opt1, opt2)

# Apropro iterators. We mentioned iterators a couple of times already.
# Iterators are objects which implement a "next" method. In the next section
# we'll cover why iterators are usefull and how to implement your own iterators






