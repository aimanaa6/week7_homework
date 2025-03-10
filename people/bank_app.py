from people.accounts import Account,SavingsAccount,GraduateAccount
from people.accounts import InsufficientFundsException

account_one = Account("POP09", 1000)
# NEW variable using Account Class
saving_account_one = SavingsAccount("C4RT67", 5000, 0.02, 3000)
grad_account_one = GraduateAccount("PL890", 2000, 500, 4)

# print(account_one.deposit(500))
# print(account_one.withdraw(300))
# print(saving_account_one.apply_interest())
# print(grad_account_one.withdraw(2500))
# Exceeds balance but within overdraft limit
# print(grad_account_one.withdraw(3000))
# print(saving_account_one.display_withdrawal_allowance())


try:
    print(account_one.withdraw(1500))
# 1500 is above the balance
except InsufficientFundsException as e:
    print(f"Exception Caught: {e}")
# created a new class
except ValueError as e:
    print("An error has occurred")
    print(e)
except Exception as ex:
    # catch all
    print("An unexpected error has occurred. Please contact your bank.")
    print(e)
finally:
    print("The FINALLY block always runs")