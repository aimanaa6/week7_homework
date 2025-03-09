class Person:
    def __init__(self,firstname,lastname,age, occupation, depositamount):
        self.__firstname= firstname
        self.__lastname = lastname
        self.__age = age
        self.__occupation = occupation
        self.__depositamount = depositamount

    def get_first_name(self):
        return self.__firstname

    def get_age(self):
        return self.__age

    def set_first_name(self, first_name):
        if str(first_name).isupper():
            self.__firstname = first_name
        else:
            raise ValueError("First name must be alphabetical")

    def set_age(self,age):
        if int(age)>16:
            self.__age= age
        else:
            raise TypeError("Age must be over 16")

class Employee:
    def __init__(self, firstname, lastname, role, annualsalary, serviceyears):
        self.__firstname = firstname
        self.__lastname = lastname
        self.__role = role
        self.__annualsalary = annualsalary
        self.__serviceyears = serviceyears

    def get_first_name(self):
        return self.__firstname

    def get_last_name(self):
        return self.__lastname

    def display_role(self):
        return self.__role

    def get_service_years(self):
        return self.__serviceyears

    def add_service_years(self,amount):
        self.__serviceyears = self.__serviceyears + amount

    def __str__(self):
            return f"Employee: {self.__firstname} {self.__lastname}.\n{self.__firstname} has worked here for {self.__serviceyears} years as a {self.__role}."

new_employee = Employee('Prableen','Gujral','Research Assistant','Full-time','3')
print(new_employee)

# new_employee.display_role()
# print(new_employee.display_role())

# new_employee.add_service_years()
# print(new_employee)

class Customer:
    def __init__(self,fullname,age,dataprotectionagreement,localbranch,withdrawallimit):
        self.__fullname = fullname
        self.__age = age
        self.__dataprotectionagreement = dataprotectionagreement
        self.__localbranch = localbranch
        self.__withdrawallimit = withdrawallimit

    def answer_dataprotectionagreement(self,answer):
        if answer == "Y":
            return "Yes"
        else:
            return "No"

    def get_fullname(self):
        return self.__fullname

    def __str__(self):
        return (f"New Customer Name: {self.__fullname}\nThe customer is {self.__age} years old.\nDoes the customer agree to the data protection policy? {new_customer.answer_dataprotectionagreement('Y')PR}."
                f"\n{self.__fullname}'s local branch is {self.__localbranch}. Their max withdrawal limit is {self.__withdrawallimit}")

new_customer = Customer('Mark Baldock','45','Y' ,'Hounslow', '2000')
print(new_customer)

new_customer.answer_dataprotectionagreement('Y')
print(new_customer.answer_dataprotectionagreement('Y'))
print(new_customer.get_fullname())
