from personnel.person import Person
from personnel.person import Employee
from personnel.person import Customer

# person
aiman_profile = Person('Aiman','Ahmed',23)
print(aiman_profile)

aiman_profile.get_first_name()
# aiman_profile = object
# get_first_name() = method (function inside the class) called on the object (aiman_profile)
print(aiman_profile.get_first_name())

aiman_profile.set_first_name("SANYA")
print(aiman_profile.get_first_name())

# aiman_profile.set_age()
# print(aiman_profile.set_age())

aiman_profile.set_age(14)
print(aiman_profile.set_age(14))

# employee
new_employee = Employee('Sanya','Puri','Research Assistant','Full-time',20000,3)
print(new_employee)

new_employee.display_role()
print(new_employee.display_role())

new_employee.add_service_years(2)
print(new_employee)

# customer
new_customer = Customer('Mark','Baldock',45,'Yes' ,'Hounslow',2000)
print(new_customer)

new_customer.get_data_protection_agreement()
print(new_customer.get_data_protection_agreement())


