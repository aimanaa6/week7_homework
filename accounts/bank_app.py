from customer_profile.person import Person
from customer_profile.person import Employee
from customer_profile.person import Customer

# person
aiman_profile = Person('Aiman','Ahmed',23)
print(aiman_profile)

aiman_profile.get_first_name()
# aiman_profile = object
# get_first_name() = method (function inside the class) called on the object (aiman_profile)
print(aiman_profile.get_first_name())

aiman_profile.set_first_name("PRABLEEN")
print(aiman_profile.get_first_name())

# aiman_profile.set_age()
# print(aiman_profile.set_age())

aiman_profile.set_age(18)
print(aiman_profile.set_age(18))

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

new_customer.get_data_protection_agreement()
print(new_customer.get_data_protection_agreement())

employee1 = Employee("John", "Doe", 30, "Manager", 50000, 5)
print(employee1)

customer1 = Customer("Jane", "Smith", 25, False, "Downtown", 2000)
print(customer1)

from accounts.account_types import Account,SavingsAccount,GraduateAccount,InsufficientFundsException
# from people.accounts import InsufficientFundsException

account_one = Account("POP09", 2000)
# NEW variable using Account Class
saving_account_one = SavingsAccount("C4RT67", 5000, 0.02, 3000)
grad_account_one = GraduateAccount("PL890", 2000, 500, 4)


# testing the account methods

# print(account_one.deposit(500))
# print(account_one.withdraw(300))
# print(saving_account_one.apply_interest())
# print(grad_account_one.withdraw(2500))
# # Exceeds balance but within overdraft limit
# print(grad_account_one.withdraw(3000))
# print(saving_account_one.display_withdrawal_allowance())



# exception handling
try:
    print(aiman_profile.set_age(13))
# 1500 is above the balance
except InsufficientFundsException as error:
    print(f"Exception Caught: {error}")
# created a new class
except ValueError as error:
    print("An error has occurred")
    print(error)
except Exception as error:
    # catch all
    print("An unexpected error has occurred. Please contact your bank.")
    print(error)
finally:
    print("Thank you for using the app!")
