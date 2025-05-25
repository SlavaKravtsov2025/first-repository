# Задание: Применение Принципа Открытости/Закрытости (Open/Closed Principle) в Разработке Простой Игры
# Цель: Цель этого домашнего задание - закрепить понимание и навыки применения принципа открытости/закрытости (Open/Closed Principle),
# одного из пяти SOLID принципов объектно-ориентированного программирования.
# Принцип гласит, что программные сущности (классы, модули, функции и т.д.) должны быть открыты для расширения, но закрыты для модификации.
# Задача: Разработать простую игру, где игрок может использовать различные типы оружия для борьбы с монстрами.
# Программа должна быть спроектирована таким образом, чтобы легко можно было добавлять новые типы оружия, не изменяя существующий код бойцов или механизм боя.

from abc import ABC, abstractmethod

class Fighter():
    def __init__(self, new_weapon = None):
        self.weapon = new_weapon

    def change_weapon(self, new_weapon):
        self.weapon = new_weapon

class Monster():
    def __init__(self, name, weapon_kill):
        self.name = name
        self.__weapon_kill = weapon_kill
    def set_weapon_kill(self, weapon_kill):
        self.__weapon_kill = weapon_kill
    def get_weapon_kill(self):
        return self.__weapon_kill

class Weapon(ABC):
    @abstractmethod
    def attack(self):
        pass

class Sword(Weapon):
    def __init__(self):
        self.name = "меч"
    def attack(self):
        print("Ты атакуешь мечом")

class Bow(Weapon):
    def __init__(self):
        self.name = "лук"
    def attack(self):
        print("Ты стреляешь из лука")

class Spear(Weapon):
    def __init__(self):
        self.name = "копье"
    def attack(self):
        print("Ты атакуешь копьем")

class Sling(Weapon):
    def __init__(self):
        self.name = "праща"
    def attack(self):
        print("Ты атакуешь из пращи")

class Baton(Weapon):
    def __init__(self):
        self.name = "дубинка"
    def attack(self):
        print("Ты атакуешь дубинкой")

print("Борьба с монстрами (вер.1.0)")

fighter = Fighter()

weapon_list = [Sword(), Bow(), Spear(), Sling(), Baton()]

weapon_cnt = len(weapon_list)

while True:
    monster_type = input("Выбери монстра (1 - Дракон, 2 - Вампир, 3 - Зомби, 0 - Выход): ")
    if monster_type == "0":
        break
    elif monster_type == "1":
        monster = Monster("Дракон", "лук")
    elif monster_type == "2":
        monster = Monster("Вампир", "копье")
    elif monster_type == "3":
        monster = Monster("Зомби", "дубинка")
    else:
        print(f"Неправильный тип монстра {monster_type}")
        continue

    nn = 0
    while True:
        weapon_type = input(f"Выбери правильное оружие - 3 попытки (цифры от 1 до {weapon_cnt}, 0-Возврат к выбору монстра): ")
        wt = int(weapon_type)
        if wt == 0:
            break
        elif 1 <= wt <= weapon_cnt:
            weapon = weapon_list[wt-1]
        else:
            print(f"Неправильный тип оружия {weapon_type}")
            continue

        fighter.change_weapon(weapon)
        fighter.weapon.attack()
        if weapon.name == monster.get_weapon_kill():
            print(f"Монстр {monster.name} побежден")
            break
        else:
            print(f"Монстр {monster.name} отбил атаку")

        nn += 1
        if nn >= 3:
            print("Вы проиграли, 3 попытки исчерпано, монстр убил Вас")
            break

