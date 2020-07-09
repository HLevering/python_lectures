# classes can be used to represent objects in an object orientated system or to
# compose data and to increase the expression of your code
# we saw already how a class is defined

class A:
    pass

a = A()
# a is an instance of class A

class B:
    # a method
    def __init__(self, a):
        # a member variable
        self.a = a
        # self represents the instance of a class. In other languages it may
        # have a name like "this"

    def do(self):
        print("foo")

    def __str__(self):
        return "Tolle beschreibung von b"

    def __repr__(self):
        return f"B(a={self.a})"


b = B(42)
s = repr(b)
print(s)


b = B(a)

# __init__ is a special method. it is used for class initialization (it is not
# a constructur compared to other languages like c++).
# If defined, the python interpreter will call __init__ automatically
# methods which start with __ double underscores (often called dunder methods)
# are special methods which you can define for your class. If defined they
# enable rich capabilities for your class. We'll cover this later

# invoke a method
b.do()

# classes can inherit from other classes

class Rad():
    pass

class Auto:
    def __init__(self, rad):
        self.rad = rad

class C(B):
    def do(self):
        #call method from parent class
        super().do()

c = C(42)
c.do()

# in the above case super() calls the parents method. However super() is much
# more powerful than that. We'll cover this later

# Inheritance should only by used if you have a "is a" relationship between the
# child and the parent class. Otherwise if it is a "has a" relationship you
# should allways prefer composition (make it a member variable) over inheritance
# Inheritance is also used to provide Mixin-classes. Mixins are a powerful
# technique to extend the behaviour of your class and enable you to reuse your
# code.
# Remember: Code repition is almost allways a code smell which can provide you
# a lot of trouble in the long run of a project. (see DRY -> don't repeat
# yourself)





