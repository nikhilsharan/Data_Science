"""
Python does not support traditional constructor overloading natively. Create a class `Employee` whose
default `__init__` constructor maps basic details, but add a explicit `@classmethod` named `from_string()`
that parses a raw hyphen-delimited text record to initialize and return a fully hydrated class object model.
Sample Input: emp = Employee.from_string('John-Doe-DataEngineer')
Expected Output: emp.first_name = 'John', emp.role = 'DataEngineer'
"""

class Employee:
    def __init__(self, first_name, last_name, role):
        self.first_name = first_name
        self.last_name = last_name
        self.role = role

    @classmethod
    def from_string(cls, emp_string):
        first_name, last_name, role = emp_string.split('-')
        return cls(first_name, last_name, role)


# Sample Input
emp = Employee.from_string('John-Doe-DataEngineer')

# Output
print("emp.first_name =", repr(emp.first_name))
print("emp.last_name =", repr(emp.last_name))
print("emp.role =", repr(emp.role))