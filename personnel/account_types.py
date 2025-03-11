class FundsUnavailableException(Exception):
    # inherits from the Exception class
    def __init__(self, message="You do not have enough funds for this transaction"):
        self._message = message
        # Custom error message
        super().__init__(self._message)
        # super() calling parent class
        # Exception - common base class

class Account:
    # base class
    def __init__(self, account_number, balance):
        self._account_number = account_number
        self._balance = balance

    def deposit(self, amount):
        self._balance += amount
        return f"Deposited {amount}. New balance: {self._balance}"

    def withdraw(self, amount):
        if amount > self._balance:
            raise ValueError ("Insufficient funds")
        self._balance -= amount
        return f"Withdrew {amount}. New balance: {self._balance}"
    # conditional statement - if the amount entered to withdraw is higher than the balance - a string is returned

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
            raise FundsUnavailableException(f"Exceeded overdraft limit! Cannot withdraw {amount}. Available balance: {self._balance}, Overdraft limit: {self._overdraft_limit}")
        self._balance -= amount
        return f"Withdrew {amount}. New balance: {self._balance}"
    # polymorphism - child class overrides method from parents class
    # withdraw method has different behaviour depending on the object type (follows a different logic)

    def __str__(self):
        return f"Graduate Account Details:\nAccount Number: {self._account_number}\nBalance: £{self._balance}\nOverdraft Limit: £{self._overdraft_limit}\nCourse Length: {self._course_length} years"