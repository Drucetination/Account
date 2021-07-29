import logging


class Account:
    num_created = 0

    def __init__(self, amount):
        self.__balance = amount
        Account.num_created += 1

    def withdraw(self, amount):
        if 0 <= amount <= self.__balance:
            self.__balance -= amount
        else:
            print('You can\'t withdraw negative amount or more than current balance')

    def deposit(self, amount):
        if amount >= 0:
            self.__balance += amount
        else:
            print('You can\'t put negative amount of money into your account')

    @property
    def balance(self):
        return self.__balance

    @balance.setter
    def balance(self, amount):
        if amount >= 0:
            self.__balance = amount
        else:
            print('You can\'t put negative amount of money into your account')
