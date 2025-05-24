# Задание: Применение Принципа Открытости/Закрытости (Open/Closed Principle) в Разработке Простой Игры
# Цель: Цель этого домашнего задание - закрепить понимание и навыки применения принципа открытости/закрытости (Open/Closed Principle),
# одного из пяти SOLID принципов объектно-ориентированного программирования.
# Принцип гласит, что программные сущности (классы, модули, функции и т.д.) должны быть открыты для расширения, но закрыты для модификации.
# Задача: Разработать простую игру, где игрок может использовать различные типы оружия для борьбы с монстрами.
# Программа должна быть спроектирована таким образом, чтобы легко можно было добавлять новые типы оружия, не изменяя существующий код бойцов или механизм боя.

from abc import ABC, abstractmethod

class Fighter():
    def __init__(self):
        self.weapon = None

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
        print("Я атакую мечом")

class Bow(Weapon):
    def __init__(self):
        self.name = "лук"
    def attack(self):
        print("Я стреляю из лука")

class Spear(Weapon):
    def __init__(self):
        self.name = "копье"
    def attack(self):
        print("Я атакую копьем")

print("Борьба с монстрами (вер.0.1)")

fighter = Fighter()

while True:
    monster_type = input("Выбери монстра (1 - Дракон, 2 - Вампир, 3 - Зомби, 0 - Выход): ")
    if monster_type == "0":
        break
    elif monster_type == "1":
        monster = Monster("Дракон", "лук")
    elif monster_type == "2":
        monster = Monster("Вампир", "копье")
    elif monster_type == "3":
        monster = Monster("Зомби", "меч")
    else:
        print(f"Неправильный тип монстра {monster_type}")
        continue

    while True:
        weapon_type = input("Выбери оружие (1 - Меч, 2 - Лук, 3 - Копье, 0 - Выбор монстра): ")
        if weapon_type == "0":
            break
        elif weapon_type == "1":
            weapon = Sword()
        elif weapon_type == "2":
            weapon = Bow()
        elif weapon_type == "3":
            weapon = Spear()
        else:
            print(f"Неправильный тип оружия {monster_type}")
            continue

        fighter.change_weapon(weapon)
        fighter.weapon.attack()
        if weapon.name == monster.get_weapon_kill():
            print(f"Монстр {monster.name} убит")
            break


