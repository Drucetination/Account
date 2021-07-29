# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

import account
import account_with_bonus as awb


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    acc = account.Account(1000)

    print(acc.balance)
    acc.balance = 2000
    print(acc.balance)
    acc.balance = -2000
    print(acc.balance)

    bonus_acc = awb.AccountWithBonus('Newcomer', 200, 0)

    print(bonus_acc.balance, bonus_acc.bonus_balance, bonus_acc.status)


# See PyCharm help at https://www.jetbrains.com/help/pycharm/
