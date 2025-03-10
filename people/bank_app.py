from people.accounts import Account,SavingsAccount,GraduateAccount
from people.accounts import InsufficientFundsException
a1 = Account("A1001", 1000)
s1 = SavingsAccount("S1001", 5000, 0.02,3)
c2 = GraduateAccount("C1001", 2000, 500,4)

# print(a1.deposit(500))
# print(a1.withdraw(300))
# print(s1.apply_interest())
# print(c2.withdraw(2500))  # Exceeds balance but within overdraft limit
# print(c2.withdraw(3000))
# print(s1.display_withdrawal_allowance())


try:
    print(a1.withdraw(1500))  # This should raise an exception
except InsufficientFundsException as e:
    print(f"Exception Caught: {e}")
except ValueError as e:
    # log the exception to a log file
    print("An error has occurred")
    print(e)
except Exception as ex:
    # catch all
    print("An unexpected error has occurred. Please contact tech support.")
    print(e)
finally:
    print("The FINALLY block always runs")