# Introduction to Object-Oriented Programming


## Encapsulation


## Object Composition


## Inheritance


## Polymorphism


## Defining Classes

### Defining Classes with Object Composition

```python
# General signature of a class
class <className><(superClass)>:
    <body>

# Example of a class definition – Student:
class Student:
    # constructor: initialise the object
    def __init__(self, name, date_enrolled, contact, is_active, student_credit=None):
        # defining instance variables
        # using underscore _ to define instance variable to not be access directly
        # if you __ (dunder), it will return an error if variable is accessed
        self._name = name
        self._date_enrolled = date_enrolled
        self._contact = contact
        self._is_active = is_active
        self._student_credit = 500 if student_credit is None else student_credit
```

#### Constructor
> Constructor is a special method to initialise the instance variables of a newly
created object.

All instance variables should be initialised in a a special method called constructor.
The instance variables begin to exist when the assignment statements are executed to initialise
their values, consistent in the manner in which local variables come into existent.

In Python, the constructor is defined by the following signature:

```python
def __init__(self, <parameters-list>):
    pass
```
where, <,parameters-list> is optional.

#### Instance Variable
If <,parameters-list> is passed in or default instance attribute exist, it will be initialise
when the constructor is called.

```python
def __init__(self, name, date_enrolled, contact, is_active):
    # defining a set of private instance variables
    self._name = _name
    self._date_enrolled = date_enrolled
    self._contact = contact
    self._is_active = is_active
```

Notice that all instance attribute names were prefixed with `_`, where this is to communicate to clients
that the instance variable shall not be accessed directly.

Here are some ways you can define instance variables:
```python
self.name = name    # Directly accessible by clients.
self._name = name   # Directly accessible by clients, but serve as a notice to refrain from doing it.
self.__name = name  # Not directly accessible by clients. Will result in error (attribute does not exist).

```

Hence, if instance attributes is define with `._<attribute-name>`, users will instead access such instance variables
through accessor (or `getter`) and mutator (or `setter`) methods.

#### Method Overloading
> In each class, there can only be at most one constructor. However, just like in functions, we may give
default values to the formal parameters in the constructor, to achieve the effect of "overloading".

```python
# Defining constructor with default values (overloading)
def __init__(self, n, num, salary=None, performance=None):
    self._name = n
    self._emp_id = num
    self._salary = 2000 if salary is None else salary
    self._performance = 1 if performance is None else performance
```
