from account import Account


class SavingsAccount(Account):

    prefix = 'SAVINGS:'

    def interest(self, rate):
        self.balance *= rate

    def withdraw(self, amount):
        print('**signature for withdrawal given**')
        super(SavingsAccount, self).withdraw(amount)


if __name__ == '__main__':
    b = SavingsAccount('Betty', 100)
    print(b)

    b.deposit(100)
    print(b)

    b.withdraw(10)
    print(b)

    b.interest(1.03)
    print(b)
