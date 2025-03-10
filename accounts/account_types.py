# class InsufficientFundsException():
#     # exception class - inherits from the Exception Class in Python
#     """
#     Exception Class
#
#     """
#     def __init__(self, message="Insufficient funds for this transaction"):
#         # dunder __init__ constructor takes message as a parameter
#         super().__init__(self.message)
#         # calling argument
#         # super() calls parent class

class InsufficientFundsException(Exception):
    def __init__(self, message="Insufficient funds for this transaction"):
        self.message = message  # Custom error message
        super().__init__(self.message)

class Account:
    def __init__(self, account_number, balance):
        self._account_number = account_number
        self._balance = balance

    def deposit(self, amount):
        self._balance += amount
        return f"Deposited {amount}. New balance: {self._balance}"

    def withdraw(self, amount):
        if amount > self._balance:
            return "Insufficient funds"
        self._balance -= amount
        return f"Withdrew {amount}. New balance: {self._balance}"

    def display_info(self):
        return f"Account Number: {self._account_number}, Balance: {self._balance}"

class SavingsAccount(Account):
    def __init__(self, account_number, balance, interest_rate,withdrawal_allowance):
        super().__init__(account_number, balance)
        # super() is calling the PARENT (Account)
        self._interest_rate = interest_rate
        self._withdrawal_allowance = withdrawal_allowance
    # adding two more attributes alongside base class

    def add_interest(self):
        self._balance += self._balance * self._interest_rate
        return f"Interest applied. New balance: {self._balance}"
    # use * as the overload operator to multiply both attributes

    def display_withdrawal_allowance(self):
        return f"The max withdrawal allowance for this customer is {self._withdrawal_allowance}."

class GraduateAccount(Account):
    def __init__(self, account_number, balance, overdraft_limit,course_length):
        super().__init__(account_number, balance)
        self._overdraft_limit = overdraft_limit
        self._course_length = course_length

    def withdraw(self, amount):
        if amount > self._balance + self._overdraft_limit:
            raise InsufficientFundsException(f"Exceeded overdraft limit! Cannot withdraw {amount}. Available balance: {self._balance}, Overdraft limit: {self._overdraft_limit}")
        self._balance -= amount
        return f"Withdrew {amount}. New balance: {self._balance}"

