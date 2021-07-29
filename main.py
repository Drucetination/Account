# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

import account
import bankclient


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    acc = account.Account(1000)

    print(acc.balance)
    acc.balance = 2000
    print(acc.balance)
    acc.balance = -2000
    print(acc.balance)


# See PyCharm help at https://www.jetbrains.com/help/pycharm/
