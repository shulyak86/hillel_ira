import uuid as uuid
import datetime


class BankAccount:
    '''
    this class is a bank account. When creating an instance - you need to fill arguments as - user's Name(str)
    and starting sum of money on this account(float)
    '''
    def __init__(self, account_name: str, balance: float) -> True:
        self.account_name = account_name
        self.account_uuid = uuid.uuid4()
        self.balance = balance
        self.transactions = []


    def deposit(self, sum_increase):
        '''is a method created to add money to user's account, with each transaction it adds a string of
        (datetime, 'deposit', sum) to the transactions list'''
        self.balance += sum_increase
        trans_datetime = datetime.datetime.now()
        self.transactions.append((trans_datetime.isoformat(sep=' '), 'deposit', str(sum_increase)))


    def withdrawal(self, sum_withdrawal):
        '''is a method created to get money from user's account, with each transaction it adds a string of
        (datetime, 'withdrawal', sum) to the transactions list'''
        bank_comission = 0.01
        '''here we add 1% of a bank comission for money withdrawal only'''
        self.balance -= sum_withdrawal*(1 + bank_comission)
        trans_datetime = datetime.datetime.now()
        self.transactions.append((trans_datetime.isoformat(sep=' '), 'withdrawal', str(sum_withdrawal)))

    def balance_show(self):
        return self.balance

    def info_about(self):
        info = (self.account_name, self.account_uuid, self.balance)
        return info


shuliak = BankAccount('Shuliak Iryna', 10000.00)

shuliak.deposit(100000)
shuliak.withdrawal(500)
shuliak.deposit(100000)

print(shuliak.balance_show())
print(shuliak.transactions)
print(shuliak.info_about())

