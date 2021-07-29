import account


class AccountWithBonus(account.Account):
    statuses = ['Newcomer', 'Regular', 'Expert']

    def __init__(self, status, bonus_balance, amount):
        super().__init__(amount)
        self.__status = 'Newcomer'
        self.__bonus_balance = bonus_balance

    def get_status(self):
        return self.__status

    def get_bonus_balance(self):
        return self.__bonus_balance

    def set_status(self, status):
        if status in AccountWithBonus.statuses:
            self.__status = status
        else:
            print('The status must be Newcomer, Regular or Expert')

    def set_bonus_balance(self, amount):
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


