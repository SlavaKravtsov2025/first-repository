# Разработай систему управления учетными записями пользователей для небольшой компании.
# Компания разделяет сотрудников на обычных работников и администраторов.
# У каждого сотрудника есть уникальный идентификатор (ID), имя и уровень доступа.
# Администраторы, помимо обычных данных пользователей, имеют дополнительный уровень доступа и могут добавлять или удалять пользователя из системы.
# Требования:
# 1.Класс `User*: Этот класс должен инкапсулировать данные о пользователе: ID, имя и уровень доступа ('user' для обычных сотрудников).
# 2.Класс Admin: Этот класс должен наследоваться от класса User. Добавь дополнительный атрибут уровня доступа, специфичный для администраторов ('admin').
# Класс должен также содержать методы add_user и remove_user, которые позволяют добавлять и удалять пользователей из списка (представь, что это просто список экземпляров User).

class User():
    def __init__(self, user_id, user_name):
        self.user_id = user_id
        self.user_name = user_name
        self.access_level = ["user"]

class Admin(User):
    def __init__(self, admin_name):
        new_id = len(user_list) + 1
        super().__init__(new_id, admin_name)
        self.access_level.append("admin")
        user_list.append(self)
        print(f"Администратор {self.user_name} с ID {self.user_id} создан, уровен доступа {self.access_level}")

    def add_user(self, new_name):
        new_id = len(user_list) + 1
        new_user = User(new_id, new_name)
        user_list.append(new_user)
        print(f"Пользователь {new_user.user_name} с ID {new_user.user_id} добавлен, уровен доступа {new_user.access_level}")

    def remove_user(self, user_id):
        if user_id < 1 or user_id > len(user_list):
            print(f"Пользователь с ID {user_id} не найден")
        else:
            user = user_list.pop(user_id - 1)
            print(f"Пользователь {user.user_name} с ID {user.user_id} удален")

    def user_info(self):
        print("Список всех пользователей")
        for user in user_list:
            print(f"ID: {user.user_id}, имя: {user.user_name}, уровень доступа: {user.access_level}")

user_list = []

admin1 = Admin("Александр")

admin1.add_user("Сергей")
admin1.add_user("Владимир")
admin1.add_user("Николай")

admin1.user_info()

admin1.remove_user(3)

admin1.user_info()

