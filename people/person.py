class Person:
    def __init__(self, firstname, lastname, age):
        self._firstname = firstname  # Single underscore for convention
        self._lastname = lastname
        self._age = age

    def get_first_name(self):
        return self._firstname

    def get_last_name(self):
        return self._lastname

    def get_age(self):
        return self._age

    def set_first_name(self, first_name):
        if first_name.isalpha():  # Check if name contains only letters
            self._firstname = first_name
        else:
            raise ValueError("First name must only contain letters.")

    def set_age(self, age):
        if age > 16:
            self._age = age
        else:
            raise ValueError("Age must be over 16.")

    def __str__(self):
        return f"{self._firstname} {self._lastname}, Age: {self._age}"

class Employee(Person):
    def __init__(self, firstname, lastname, age, role, annualsalary, serviceyears):
        super().__init__(firstname, lastname, age)  # Call parent constructor
        self._role = role
        self._annualsalary = annualsalary
        self._serviceyears = serviceyears

    def display_role(self):
        return self._role

    def get_service_years(self):
        return self._serviceyears

    def add_service_years(self, amount):
        if amount > 0:
            self._serviceyears += amount
        else:
            raise ValueError("Service years must be positive.")

    def __str__(self):
        return (f"Employee: {self._firstname} {self._lastname}, Age: {self._age}, "
                f"Role: {self._role}, Salary: ${self._annualsalary}, "
                f"Years of Service: {self._serviceyears}")

class Customer(Person):
    def __init__(self,firstname,lastname,age,dataprotectionagreement,localbranch,withdrawallimit):
        super().__init__(firstname, lastname, age)  # Call parent constructor
        self._dataprotectionagreement = bool(dataprotectionagreement)  # Store as Boolean
        self._localbranch = localbranch
        self._withdrawallimit = withdrawallimit


    def get_dataprotection_agreement(self):
            return "Yes" if self._dataprotectionagreement else "No"

    def get_withdrawal_limit(self):
        return self._withdrawallimit

    def __str__(self):
        return (f"Customer: {self._firstname} {self._lastname}, Age: {self._age}, "
                f"Data Protection Agreement: {self.get_dataprotection_agreement()}, "
                f"Local Branch: {self._localbranch}, Withdrawal Limit: ${self._withdrawallimit}")
