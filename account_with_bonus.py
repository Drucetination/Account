import account


class AccountWithBonus(account.Account):
    statuses = ['Newcomer', 'Regular', 'Expert']

    def __init__(self, status, bonus_balance, amount):
        super().__init__(amount)
        self.__status = 'Newcomer'
        self.__bonus_balance = 200

    @property
    def status(self):
        return self.__status

    @property
    def bonus_balance(self):
        return self.__bonus_balance

    @status.setter
    def status(self, status):
        if status in AccountWithBonus.statuses:
            self.__status = status
        else:
            print('The status must be Newcomer, Regular or Expert')

    @bonus_balance.setter
    def bonus_balance(self, amount):
        if amount >= 0:
            self.__bonus_balance = amount
        else:
            print('Bonus balance can\'t be a negative number')

    def increase_balance(self, amount):
        if amount >= 0:
            self.__bonus_balance += amount
        else:
            print('You can\'t put a negative amount to your bonus balance')

    def decrease_balance(self, amount):
        if 0 <= amount <= self.__bonus_balance:
            self.__bonus_balance -= amount
        else:
            print('You can\'t put a negative amount to your bonus balance and your bonus balance can\'t'
                  ' be a negative number')


