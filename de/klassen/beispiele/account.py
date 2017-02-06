

# example for classes and inheritance

class Account:
    """
    Account for a bank client.
    """
    prefix = ''

    def __init__(self, newname, balance=0):
        self.name = newname
        self.balance = balance

    def deposit(self, amt):
        self.balance = self.balance + amt

    def withdraw(self, amt):
        self.balance = self.balance - amt

    def __str__(self):
        return "{}:{:10.2f}".format(self.name, self.balance)


if __name__ == '__main__':

    a = Account('Adam', 100)
    print(a)

    a.deposit(50)
    print(a)

    a.withdraw(10)
    print(a)
