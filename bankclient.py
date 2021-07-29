import account


class BankClient:

    def __init__(self, name):
        self.__name = name
        self.__account = account.Account(0)

    def get_name(self):
        return self.__name

    def get_balance(self):
        return self.__account.get_balance()

    def set_name(self, name):
        self.__name = name

    def set_balance(self, amount):
        self.__account.set_balance(amount)
