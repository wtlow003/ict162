# Introduction to Object-Oriented Programming

## Object-Oriented Programming (OOP) Principles

<details>
<summary>Encapsulation</summary>

### What is it?
> Encapsulation is the result of abstracting related data and operations simultaneously
and applying information hiding.

Encapsulation results in class definition; a class defines data and operation,
applies information-hiding to wrap up implementation details so that its objects are black boxes.
By knowing the interface or the method signatures of methods implemented in a class,
the clients or collaborators can call an object of that class to perform a service on the object. The clients or collaborators need not be concerned or know about the implementation of the instance variables and methods.

Hiding implementation details means that instances variables can be accessed only indirectly via service calls
to invoke methods that provides <i>controlled access</i> to private instance variables.

### How does it work?
The methods that provides <i>controlled access</i> are:
1. <b> accessor methods </b>

    Accessor methods allow inspection of instance variables.
2. <b> mutator methods </b>

    Mutator methods allow values of instance variables to be changed.

```python
class Student:
    def __init__(self, name, age):
        self._name = name
        self._age = age

        # defining accessor methods
        @property
        def age(self):
            print(f"Retrieving {self.name}'s age")
            return self._age

        # defining mutator methods
        @age.setter
        def age(self, value):
            if type(value) is not int:
                raise TypeError("Age must be a number!")
            if value < 0:
                raise ValueError("Age can't be negative")
            print(f"Setting {self.name}'s age to {value}...'")
            self._age = value

```
</details>
<details>
<summary>Abstraction</summary>

### What is it?
> Abstraction refers to using simple things to represented complexity.

For instance, you may know how to drive a car, but you do not necessarily need to know
how the car works in order for you to drive a car. In essence, it takes away the need for details,
and allows users to utilise the object as a whole.

### How does it work?

Given a class variable such as `student`, the student may attend different faculties within the university
and hence as such, the students may be identifed as `science students`, `humanities students` or `math students`.

```python
from abc import ABC, abstractmethod

class ABSclass(ABC):
    def state_name(self, x):
        print(f"Name is {x}")

    @abstractmethod
    def task(self):
        print("We are Abstract student now.")

class ScienceClass(ABSclass):
    def task(self):
        print("We are Science student now.")

class MathClass(ABSclass):
    def task(self):
        print("We are Math student now.")

sci_obj = ScienceClass()
sci_obj.task()                  # We are Science student now
sci_obj.state_name('Jensen')    # Name is Jensen

math_obj = MathClass()
math_obj.task()                 # We are Math student now
math_obj.state_name('Max')      # Name is Max
```

</details>


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
---
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

---
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

---
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
