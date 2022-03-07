from random import randint
from typing import *


class Attribute:
    def __set_name__(self, owner, name):
        self.name = name

    def __get__(self, instance: ClassVar, owner):
        print(f'Getting ready to use {self.name} in a fight.')
        success_chance = randint(4, 10)
        if success_chance >= 9:
            print('Critical strike!')
        res = instance.__dict__[self.name]*success_chance
        print(f'The total power of your attack is {res}.')
        return res

    def __set__(self, instance: ClassVar, value: int):
        print(f'Your {self.name} is now {value}.')
        instance.__dict__[self.name] = value
        return value


class Avatar:
    strength = Attribute()
    stamina = Attribute()
    dexterity = Attribute()

    def __init__(self, name: str):
        self.name = name
        self.strength = randint(1, 10)
        self.stamina = randint(1, 10)
        self.dexterity = randint(1, 10)
        self.talent_tree = {'constitution', 'wisdom', 'technology', 'charisma', 'force_powers'}

    def __getitem__(self, item: str):
        try:
            return self.__dict__[item]
        except KeyError:
            raise AttributeError

    def __getattribute__(self, item):
        attr = object.__getattribute__(self, item)
        if not attr:
            raise AttributeError
        return attr

    def __getattr__(self, item: str):
        if item in self.talent_tree:
            print(f"You don't have {item} upgraded now. Later "
                  "you will be able to gain it in the talent tree.")
        else:
            print(f"There is no such talent as {item}. ")
        return 0

    def show_attr(self, name: str):
        res = self.__getitem__(name)
        if res:
            print(f'Your {name} talent is {res}')
        if res != 10:
            print('Can be upgraded. ')
        return None


if __name__ == '__main__':
    hunn = Avatar('Attila')
    print(hunn['stamina'])  # - getitem
    print(hunn.strength)  # - getattribute and get
    print(hunn.magic)  # - getattr
    hunn.show_attr('dexterity')  # - getitem inside another func
