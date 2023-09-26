'''implement a class called bankaccont that reresents a bank account. the class should have private
attributes for account number,account holder name,and account balance.include methods to
deposites money,withdraw money,and display he account balance.ensure that the account balance
cannot be accessed directly from outside the class.write a program to create an instance of the 
bankaccount class and test he deposit and withdrawa functionality.'''


class bankaccount:

  def __init__(self,account_number,account_holder_name,initial_balance=0.0):
    self.__account_number=account_number
    self.__account_holder_name=account_holder_name
    self.__account_balance=initial_balance

def deposit(self,amount):
  if amount > 0:
    self.__account_balance += amount
    print("deposited ₹{}.new balance: ₹
                             {}".format(amount,self.__account_balance))
else:
    print("nvalid deposit amount.please deposit a positive amount.")

def withdraw(self,amount):
  if amount > 0 and amount <= self.__account_balance:
    self.__account_balance -= amount
    print("withdraw ₹{}.new balance: ₹ 
                                 {}".format(amount,self.__account_balance))
  else:
    print("invalid withdrawal amount or insufficient balance.")

def display_balance(self):
  print("account balance for {} (account #{}): ₹{}".format(
    self.__account_holder_name,self.__account_number,
    self.__account_balance))


account = 
bankaccount(account_number="123456789",
account_holder_name="hari prabu",
initial_balance=5000.0)

account.display_balance()
account.deposit(500.0)
account.wihdraw(200.0)
account.display_balance()



  
