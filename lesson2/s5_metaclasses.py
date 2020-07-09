# now we'll cover a topic called metaclasses. Some people say, that metaclasses
# are something magic and that an ordinary python developer probably won't need
# them.
# But there is one simple practical reason for metaclasses.
# They enable  the author of an class to enforce constraints in derived
# classes.
# Here is an example:

class A:
    def foo(self):
        self.bar()

# the above class has a method foo which wants to invoke a method bar. If you
# create an instance of A and try to invoke method foo, it will fail with an
# error, saying that A has no attribute "bar".
# You have to sublcass A and implement a method bar to use foo.

class B(A):
    def bar(self):
        print(42)

b = B()
b.foo()

# So class A has to rely on B, that it will implement method bar. The only way
# to inforce this is via metaclasses. Ok it was the only method, but now we
# can implement __init_subclass__, which is easier to use. Therefore we use
# __init_subclass__, but you should know, that there are metaclasses and one of
# their purposes is to enforce constraints for subclasses
# one example of a metaclass is ABC from module abc. ABC is short for abstract
# base class. abc offers a decorator abstractmethod
from abc import ABC, abstractmethod

class Foo(ABC):
    @abstractmethod
    def bar(self):
        pass

# f = Foo()  # this will fail. you must provide concrete implementations for
# all abstractmethods to create an instance of Foo

class Bar(Foo):
    def bar(self):
        print("wohoo")


bar = Bar()  # this will work

# now, lets the __init_subclass__ in action


class A:
    def __init_subclass__(cls, /, **kwargs):
        print(cls.__name__, "inherited from A")
        if not hasattr(cls, "foo"):
            raise TypeError(f"{cls.__name__} has no attribute foo")
        super().__init_subclass__(**kwargs)


class B(A):
    foo = 42
    pass

class C(A):
    pass

# Whenever a new class which inherits from A is defined, __init_subclass__ will
# be called. It gives you the ability to hook into the class creation process
# and enforce constraints on the deriving class

