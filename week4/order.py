from collections import defaultdict


class Dish:
    def __init__(self, name: str, price: float, mass: float):
        self.name = name
        self.price = price
        self.mass = mass


class Order:
    ''' Takes a dict of Dish instances with the amount of dishes
    and creates an order with its parameters'''
    def __init__(self, input_dishes: dict):
        self.dishes = defaultdict(int)
        self.total_price = 0.0
        self.to_pay = 0.0
        self.total_mass = 0.0
        self.add_dishes(input_dishes)

    def add_dishes(self, input_dishes: dict):
        for key in input_dishes.keys():
            amount = input_dishes[key]
            self.dishes[key.name] += amount
            self.total_price += key.price * amount
            self.to_pay += key.price * amount
            self.total_mass += key.mass * amount
        return None

    def pay(self, money: float):
        if self.to_pay < money:
            self.to_pay = 0.0
            tips = input('Would you like to leave tips?(y/n) - ')
            if tips == 'n':
                print('Please, take your change')
            print('Thank your for your visit. Goodbye')
        elif not (self.to_pay - money):
            self.to_pay = 0.0
            print('Thank your for your visit. Goodbye')
        else:
            self.to_pay -= money
            print(f'Thanks. There are {self.to_pay} dollars still to be paid.')
        return None

    def info(self):
        print('----------')
        print('order info:\n'
              f'price: {self.total_price};\n' 
              f'mass: {self.total_mass};\n'
              f'money still to pay: {self.to_pay}')
        for dish, amount in self.dishes.items():
            print(f'{dish} - {amount}')
        print('----------\n')
        return None


if __name__ == '__main__':
    coffee = Dish('coffee', 2.50, 100)
    okroshka = Dish('okroshka', 4.40, 300)
    my_order = Order({okroshka: 1, coffee: 2})
    my_order.info()
    my_order.add_dishes({okroshka: 1})
    my_order.info()
    my_order.pay(3.0)
    my_order.info()
    my_order.pay(12)

