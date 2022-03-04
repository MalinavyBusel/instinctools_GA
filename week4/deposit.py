class BankAccount:
    def __init__(self, acc_number: int, name: str, balance: float = 0.0):
        self.__account_number = acc_number
        self.__name = name
        self.__balance = balance

    def deposit(self, dep_money: float):
        self.__balance += dep_money
        print(f'The sum of {dep_money} added to your account.\n'
              f'The current balance is {self.__balance}.')

    def withdrawal(self, withdraw_money: float):
        if self.__balance - withdraw_money < 0:
            print(f'Not enough money. Your balance is {self.__balance}')
        else:
            self.__balance -= withdraw_money
            print(f'The sum of {withdraw_money} was successfully'
                  'withdrew from your account.\n'
                  f'The current balance is {self.__balance}.')

    def apply_fees(self, fee: int = 5):
        self.__balance -= self.__balance*fee/100

    def display(self):
        print(f'Owner: {self.__name.title()};\n'
              f'balance: {round(self.__balance, 2)}')


if __name__ == '__main__':
    ignat = BankAccount(48294, 'Ignat', 2000.42)
    ignat.apply_fees()
    ignat.display()
