from personnel.person import Person, Employee, Customer
from personnel.account_types import Account,SavingsAccount,GraduateAccount,FundsUnavailableException

# person
new_profile = Person('Aiman', 'Ahmed', 23)
print(new_profile)

new_employee = Employee('Shria','Malik','Research Assistant','Full-time',20000,3)
print(new_employee)

new_customer = Customer('Mark','Baldock',45,True ,'Hounslow',2000)
print(new_customer)

employee1 = Employee("Reece", "Wilson", 30, "Manager", 50000, 5)
print(employee1)

customer1 = Customer("Elaine", "Smith", 55, False, "Downtown", 2000)
print(customer1)

# account_types
account_one = Account("POP09", 2000)
# NEW variable using Account Class
saving_account_one = SavingsAccount("C4RT67", 5000, 0.02, 3000)

grad_account_one = GraduateAccount("PL890", 2000, 500, 4)
print(new_profile, grad_account_one)

# print(new_profile.set_age(14))
# print(account_one.deposit(500))
# print(saving_account_one.add_interest())

# exception handling
try:
    print(grad_account_one.withdraw(10000))
# 1500 is above the balance
except FundsUnavailableException as error:
    print(f"Transaction denied: {error}")
# created a new class
except ValueError as error:
    print(f"An error has occurred: {error}")
except Exception as error:
    # catch all
    print(f"An unexpected error has occurred. Please contact your bank: {error}")
finally:
    print("Thank you for using the app!")



# person
# aiman_profile.get_first_name()
# # get_first_name() = method (function inside the class) called on the object (aiman_profile)
# print(aiman_profile.get_first_name())

# aiman_profile.set_first_name("PRABLEEN")
# print(aiman_profile.get_first_name())

# # aiman_profile.set_age()
# # print(aiman_profile.set_age())

# aiman_profile.set_age(18)
# print(aiman_profile.set_age(18))

# new_employee.display_role()
# print(new_employee.display_role())

# new_employee.add_service_years(2)
# print(new_employee)
#
# # customer
# new_customer.get_data_protection_agreement()
# print(new_customer.get_data_protection_agreement())


# testing the account methods

# print(account_one.deposit(500))
# print(account_one.withdraw(300))
# print(saving_account_one.apply_interest())
# print(grad_account_one.withdraw(2500))
# # Exceeds balance but within overdraft limit
# print(grad_account_one.withdraw(3000))
# print(saving_account_one.display_withdrawal_allowance())



