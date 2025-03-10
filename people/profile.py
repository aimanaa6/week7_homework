from people.person import Person
from people.person import Employee
from people.person import Customer

# person
aiman_profile = Person('Aiman','Ahmed',23)
print(aiman_profile)

aiman_profile.get_first_name()
# aiman_profile = object
# get_first_name() = method (function inside the class) called on the object (aiman_profile)
print(aiman_profile.get_first_name())

aiman_profile.set_first_name("PRABLEEN")
print(aiman_profile.get_first_name())

aiman_profile.get_age()
print(aiman_profile.get_age())

aiman_profile.set_age(18)
print(aiman_profile.get_age())

# employee
new_employee = Employee('Prableen','Gujral','Research Assistant','Full-time',20000,3)
print(new_employee)

new_employee.display_role()
print(new_employee.display_role())

new_employee.add_service_years(2)
print(new_employee)

# customer
new_customer = Customer('Mark','Baldock',45,'Yes' ,'Hounslow',2000)
print(new_customer)

new_customer.get_dataprotection_agreement()
print(new_customer.get_dataprotection_agreement())

employee1 = Employee("John", "Doe", 30, "Manager", 50000, 5)
print(employee1)

customer1 = Customer("Jane", "Smith", 25, False, "Downtown", 2000)
print(customer1)