class Person:

    def __init__ (self, name, age):
        self._name = name
        self._age = age

    @property
    def name (self):
        return self._name

    @name.setter
    def name(self, name):
        self._name = name

    @property
    def age(self):
        return self._age

    @age.setter
    def age (self, age):
        self._age = age

    def __str__(self):
        return f'Person[name: {self._name}, age: {self._age}]'

class Employee(Person):

    def __init__(self, salary, name, age):
        super().__init__(name, age)
        self._salary = salary

    def __str__ (self):
        return f'[Employee[salary: {self._salary}], {super().__str__()}]'
