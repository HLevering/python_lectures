# This file is inspired by the class development toolkit talk by Raymond
# Hettinger.
# We'll have a deeper look into classes. Python supports you working in an
# agile workflow. 
# Agile means:
# fast iterations
# get feedback quickly

# We will see how this works, when we explore classes


# start by writing a class with a docstring
# a docstring can be attached to classes, functions and modules. Its purpose is
# documentation. It should briefly say, what your class does. It gives you a
# moment to think about your problem and you can also handover the class /
# function with a docstring to colleques, stackholders or customers and get
# their feedback. That is agile ...


class Circle:
    """the best circle in the world"""


# The __init__ method is not a constructor. When __init__ is called. The class
# has already been created and the parameter self represents the created
# instance. The task of __init__ is to initialize all instance member variables
# You could change self to any name you want, but every one is using self and
# you want your code to look like python. So don't do that.

class Circle:
    """the best circle in the world"""
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return math.pi * radius ** 2

c = Circle(1)
print(c.radius)
print(c.area())



# Store variables which are shared between instances directly in the class.

class Circle:
    """the best circle in the world"""
    version = "0.1"
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return math.pi * radius ** 2

c1 = Circle(1)
c2 = Circle(2)
print(c1.version, c2.version)

# In fact your class defintion acts like a namespace and everything in side it
# is similiar to the content of a module. If you put your defintions of your
# class in a module it would be indistinguishable. Therefore you can but any
# code (e.g. for loops print statements) in a class defintion
class F:
    for i in range(10):
        print(i)


class Circle:
    """the best circle in the world"""
    version = "0.2"
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return math.pi * radius ** 2

    #we can add new features, when they are needed

    def perimeter(self):
        return math.pi * radius * 2


# the class is used and subclassed 


class HotCircle(Circle):
    def perimeter(self):
        return Circle.perimeter() * 1.25


# your class will be used in ways you could not event think about
# Some want to create circles from the perimeter like so:
# c = Circle(perimeter_to_radius(5))
# But our init function does already take a radius. What shall we do? Change it
# and break all already written code? Or shall the perimeter guys stale in
# frustration? Fortunately, python lets us do both
# alternative constructors can be defined with @classmethod

class Circle:
    """the best circle in the world"""
    version = "0.3"
    def __init__(self, radius):
        self.radius = radius

    @classmethod
    def from_perimeter(cls, perimeter):
        return Circle(perimeter / 2 / math.pi

    def area(self):
        return math.pi * radius ** 2

# but what is with HotCircle. Should it not be able to take advantage of the
# new from_perimeter constructor? We hardwired the Circle dependency. So we'll
# fix that.


class Circle:
    """the best circle in the world"""
    version = "0.4"
    def __init__(self, radius):
        self.radius = radius

    @classmethod
    def from_perimeter(cls, perimeter):
        return cls(perimeter / 2 / math.pi  # cls is the type which shall be created

    def perimeter(self):
        return math.pi * radius * 2

    def area(self):
        return math.pi * radius ** 2


# People are using a geomtry function.
def grad_to_rad(grad):
    return grad / (2 * math.pi) 

# Although not directly related to Circle, we can put into our class, so that
# users can find it easier.


class Circle:
    """the best circle in the world"""
    version = "0.5"
    def __init__(self, radius):
        self.radius = radius

    @classmethod
    def from_perimeter(cls, perimeter):
        return cls(perimeter / 2 / math.pi  # cls is the type which shall be created

    def perimeter(self):
        return math.pi * radius * 2

    def area(self):
        return math.pi * radius ** 2

    def grad_to_rad(self, grad):
        return grad / (2 * math.pi) 

# But we don't use the self parameter and constructing a circle object to use
# grad_to_rad seems strange. For this case we have @staticmethod

class Circle:
    """the best circle in the world"""
    version = "0.6"
    def __init__(self, radius):
        self.radius = radius

    @classmethod
    def from_perimeter(cls, perimeter):
        return cls(perimeter / 2 / math.pi  # cls is the type which shall be created

    def perimeter(self):
        return math.pi * radius * 2

    def area(self):
        return math.pi * radius ** 2

    @staticmethod
    def grad_to_rad(grad):
        return grad / (2 * math.pi) 

# With staticmethod, we can non related functions to a class. In this way users
# can easier find the right auxilliary functions


# New constraint arrives.sThere is a law that forces us to calculate the area
# from the perimeter


class Circle:
    """the best circle in the world"""
    version = "0.7"
    def __init__(self, radius):
        self.radius = radius

    @classmethod
    def from_perimeter(cls, perimeter):
        return cls(perimeter / 2 / math.pi  # cls is the type which shall be created

    def perimeter(self):
        return math.pi * radius * 2

    def area(self):
        p = self.perimeter()
        r = p / 2 / math.pi
        return math.pi * radius ** 2

    @staticmethod
    def grad_to_rad(grad):
        return grad / (2 * math.pi) 


# But now the area method of HotCircle is broken, because they have overwritten
# the perimter method
class HotCircle(Circle):
    def perimeter(self):
        return Circle.perimeter() * 1.25


# we can add variables /methods which are exclusive to one class, if they start
# with "__" dunder
import math


class Circle:
    """the best circle in the world"""
    version = "0.8"
    def __init__(self, radius):
        self.radius = radius

    @classmethod
    def from_perimeter(cls, perimeter):
        return cls(perimeter / 2 / math.pi)  # cls is the type which shall be created

    def perimeter(self):
        return math.pi * self.radius * 2

    _perimeter = perimeter  # wont work, see below
    __perimeter = perimeter

    def area(self):
        p = self.__perimeter()
        r = p / 2 / math.pi
        return math.pi * r ** 2

    @staticmethod
    def grad_to_rad(grad):
        return grad / (2 * math.pi) 

class HotCircle(Circle):
    def perimeter(self):
        return Circle.perimeter() * 1.25
    _perimeter = perimeter
    __perimeter = perimeter  # won't override Circle.__perimeter attribute


print(HotCircle(1).area())

# attributes which start with __ as A.__my_var are automatically namemangled
# into _A__my_var. It is not for declaring private variables. Its sole purpose
# is to give each class the opertunity to define its own atributes.

# And here arrives the next request. Circles must store its diameter and not
# its radius. In other languages like Java or C++ you would be doomed, because
# you were so foolish to expose your member variables. You wish you had written
# some getter and setter methods. But don't worry, this is python
# @property to the rescue


class Circle:
    """the best circle in the world"""
    version = "0.9"
    def __init__(self, radius):
        self.radius = radius

    @property
    def radius(self):
        return self.diameter / 2

    @radius.setter
    def radius(self, radius):
        self.diameter = 2 * radius

    @classmethod
    def from_perimeter(cls, perimeter):
        return cls(perimeter / 2 / math.pi)  # cls is the type which shall be created

    def perimeter(self):
        return math.pi * self.radius * 2

    __perimeter = perimeter

    def area(self):
        p = self.__perimeter()
        r = p / 2 / math.pi
        return math.pi * r ** 2

    @staticmethod
    def grad_to_rad(grad):
        return grad / (2 * math.pi) 

c = Circle(2)
c.radius -= 1
print(c.radius)

# @property allows you to encapsulate a member variable behind getter and
# setter methods without breaking any existing client code, which relies on
# this variable
# Therefore, don't waste your time to hide member variablse upfront because you
# can do so easily later, if you need it.

# Circle is used quite heavily. But a python class(~>100 bytes) is relativ big compared to
# the fact that it only stores a diameter

for i in range(1_000_000):
    c = Circle(1)

# use slots to make your class smaller and faster, but only if you need to,
# because you loose flexibility.

class Circle:
    """the best circle in the world"""
    version = "0.10"
    __slots__ = ["diameter"]
    def __init__(self, radius):
        self.radius = radius

    @property
    def radius(self):
        return self.diameter / 2

    @radius.setter
    def radius(self, radius):
        self.diameter = 2 * radius

    @classmethod
    def from_perimeter(cls, perimeter):
        return cls(perimeter / 2 / math.pi)  # cls is the type which shall be created

    def perimeter(self):
        return math.pi * self.radius * 2

    __perimeter = perimeter

    def area(self):
        p = self.__perimeter()
        r = p / 2 / math.pi
        return math.pi * r ** 2

    @staticmethod
    def grad_to_rad(grad):
        return grad / (2 * math.pi) 


print(Circle(1).radius)


# Now, you know how to use classes and how they support you in a lean workflow

# One last point. Attribute access
class A:
    f = 42

a = A()
a.f

# the dot operator is equivalent to
print("get the attribute", getattr(a, "f"))
# there are also
print("check if an attribute exists", hasattr(a, "b")) 
setattr(a, "f", 5) # equivalent to a.f = 5
print(a.f)


# By the way getattr, setattr, hasattr work on every object. This means, that
# you can use them to lookup / retrieve / change  attributes in modules and
# functions, too.



