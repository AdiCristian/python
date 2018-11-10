import sys

"""
    This is an example demostrating how to reference the different
    scopes and namespaces
"""
def scope_test():
    def do_local():
        spam = "local spam"

    def do_nonlocal():
        nonlocal spam
        spam = "nonlocal spam"

    def do_global():
        global spam
        spam = "global spam"

    spam = "test spam"
    do_local()
    print("After local assignment: ", spam)
    do_nonlocal()
    print("After nonlocal assignment: ", spam)
    do_global()
    print("After global assignment: ", spam)


# Class definition syntax
class ClassName:
    i = 12345
    # <statement-1>
    # ...
    # ...
    # <statement-N>


class MyClass:
    """ A simple example class """
    i = 12345

    def f(self):
        return 'hello world from a class'


class Complex:
    def __init__(self, realpart, imagpart):
        self.r = realpart
        self.i = imagpart


# Class and Instance Variables
class Dog:
    kind = 'canine'     # Class variable shared by all instances

    tricks = []         # Mistaken use of a class variable

    def __init__(self, name):
        self.name = name    # Instance variable unique to each instance

    def add_trick(self, trick):
        self.tricks.append(trick)


class Cat:
    def __init__(self, name):
        self.name = name
        self.tricks = []    # Creates a new empty tricks list for each Cat instance

    def add_trick(self, trick):
        self.tricks.append(trick)


# Methods may call other mathods by using method attributes of the self argument
class Bag:
    def __init__(self):
        self.data = []

    def add(self, x):
        self.data.append(x)

    def addTwice(self, x):
        self.add(x)
        self.add(x)

# Data type similar to C "struct"
class Employee:
    pass

# Iterators
class Reverse:
    """ Iterator for looping over a sequence backwards. """
    def __init__(self, data):
        self.data = data
        self.index = len(data)

    def __iter__(self):
        return self

    def __next__(self):
        if self.index == 0:
            raise StopIteration
        self.index = self.index - 1
        return self.data[self.index]


def main():
    print("Classes chapter !!")

    scope_test()
    print("In global scope: ", spam)

    # Class instantiation
    x = MyClass()

    print(x.i)
    print(x.f())
    print(x.__doc__)

    x = Complex(3.0, -4.5)
    print(x.r)
    print(x.i)

    # attribute reference
    x.counter = 1
    while x.counter < 10:
        x.counter = x.counter * 2
    print(x.counter)
    del x.counter

    d = Dog('Fido')
    e = Dog('Buddy')
    print(d.kind)
    print(d.name)
    print(e.name)

    d.add_trick('roll over')
    e.add_trick('play dead')
    print(d.tricks)     # Unexpectedly shared by all Dog instances

    d = Cat('Lilu')
    e = Cat('Garfield')
    d.add_trick('Jump')
    e.add_trick('Roll over')
    print(d.tricks)
    print(e.tricks)

    john = Employee() # Create an empty employee record
    john.name = 'John Doe'
    john.dept = 'computer lab'
    john.salary = 1000

    rev = Reverse('spam')
    for char in rev:
        print(char)

    print(john.__dict__)


if __name__ == '__main__':
    main()