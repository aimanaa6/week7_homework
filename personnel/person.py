class Person:
    # class is a template/blueprint
    # base class - other classes with inherit
    def __init__(self, firstname, lastname, age):
        # __init__ constructor method initialises the class
        # self is the first argument passes to an object
        # dunder either side = special attribute
        # attributes to the class
        self._firstname = firstname
        self._lastname = lastname
        self._age = age
    # Single underscore is a protected attribute (encapsulation)
    # name is meant for internal use only in a class

    # method = function that belongs to a class
    # control access through getter and setter methods
    # getter methods enable READ access
    def get_first_name(self):
        return self._firstname
    # will return the attribute value

    def get_last_name(self):
        return self._lastname

    # setter methods use validation logic to modify attributes
    def set_first_name(self, first_name):
        if first_name.isalpha():
            self._firstname = first_name
        else:
            raise ValueError("First name must only contain letters.")
    # conditional statement is used to validate value
    # sets a new first name - must be alphabetical otherwise an error will be raised

    def set_age(self, age):
        if age > 16:
            self._age = age
        else:
            raise ValueError("Age must be over 16.")
    # sets a new age
    # conditional statement - must be over 16 to set up a bank account

    def __str__(self):
        return f"{self._firstname} {self._lastname}, Age: {self._age}"
    # print statement returns a string

class Employee(Person):
    # Inherited from Person (subclass)
    # Instantiation of Employee
    def __init__(self, firstname, lastname, age, role, annual_salary, service_years):
        super().__init__(firstname, lastname, age)  # Call parent constructor
        # super() calls the __init__ method of the Person class and returns the base class object
        self._role = role
        self._annual_salary = annual_salary
        self._service_years = service_years

    def display_role(self):
        return self._role

    def get_service_years(self):
        return self._service_years

    def add_service_years(self, amount):
        if amount > 0:
            self._service_years += amount
        else:
            raise ValueError("Service years must be positive.")
    # add service years function
    # augmented assignment (+=) - add the service years (value must be more than zero)
    # example: employee review

    def __str__(self):
        return (f"Employee: {self._firstname} {self._lastname}, Age: {self._age}, "
                f"Role: {self._role}, Salary: ${self._annual_salary}, "
                f"Years of Service: {self._service_years}")
    # string representation of Employee profile (using f string to embed the variables)

class Customer(Person):
    # inherits from Person
    def __init__(self,firstname,lastname,age,data_protection_agreement,local_branch,withdrawal_limit):
        super().__init__(firstname, lastname, age)
        # Call parent constructor
        self._data_protection_agreement = bool(data_protection_agreement)
        # Store as Boolean - does the customer agree with the data protection agreement?
        self._local_branch = local_branch
        self._withdrawal_limit = withdrawal_limit
    # mix of strings,integers and boolean

    def get_data_protection_agreement(self):
        if self._data_protection_agreement:
            return "Yes"
        else: "No"
    # returns True of False value based on Yes/Np

    def get_withdrawal_limit(self):
        return self._withdrawal_limit

    def __str__(self):
        return (f"Customer: {self._firstname} {self._lastname}, Age: {self._age}, "
                f"Data Protection Agreement: {self.get_data_protection_agreement()}, "
                f"Local Branch: {self._local_branch}, Withdrawal Limit: ${self._withdrawal_limit}")
    # Customer profile
