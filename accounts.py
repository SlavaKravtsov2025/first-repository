# Разработай систему управления учетными записями пользователей для небольшой компании.
# Компания разделяет сотрудников на обычных работников и администраторов.
# У каждого сотрудника есть уникальный идентификатор (ID), имя и уровень доступа.
# Администраторы, помимо обычных данных пользователей, имеют дополнительный уровень доступа и могут добавлять или удалять пользователя из системы.
# Требования:
# 1.Класс `User*: Этот класс должен инкапсулировать данные о пользователе: ID, имя и уровень доступа ('user' для обычных сотрудников).
# 2.Класс Admin: Этот класс должен наследоваться от класса User. Добавь дополнительный атрибут уровня доступа, специфичный для администраторов ('admin').
# Класс должен также содержать методы add_user и remove_user, которые позволяют добавлять и удалять пользователей из списка (представь, что это просто список экземпляров User).

class User():
    # конструктор, по умолчанию уровень доступа "user"
    def __init__(self, user_idf, user_name):
        self.user_idf = user_idf
        self.user_name = user_name
        self.__access_level = "user"

    # Доступ к private __access_level
    def get_access_level(self):
        return self.__access_level

    # Установка нового __access_level
    def set_access_level(self, new_level):
        self.__access_level = new_level

class Admin(User):
    def __init__(self, name):
        # Счетчик идентификатора пользователей, admin имеет идентификатор 1
        self.id_count = 1
        # Список объектоа пользователей
        self.user_list = []
        super().__init__(self.id_count, name)
        self.id_count += 1
        self.set_access_level("admin")
        print(f"Администратор {self.user_name} с ID {self.user_idf} создан, уровень доступа {self.get_access_level()}")

    # Добавляет нового пользователя
    def add_user(self, new_name):
        # Проверяем, что пользователя с таким именем нет в списке
        ok_add = True
        for user in self.user_list:
            if user.user_name == new_name:
                print(f"Пользователь {new_name} уже есть в списке пользователей")
                ok_add = False
                break
        if ok_add:
            new_user = User(self.id_count, new_name)
            # Добавляем объект нового пользователя в список, увеличив предварительно счетчик
            self.id_count += 1
            self.user_list.append(new_user)
            print(f"Пользователь {new_user.user_name} с ID {new_user.user_idf} добавлен, уровень доступа {new_user.get_access_level()}")

    # Удаляет пользователя
    def remove_user(self, user_idf):
        ok_remove = False
        # Поиск идентификатора в списке объектов
        for i in range(0, len(self.user_list)):
            if self.user_list[i].user_idf == user_idf:
                user = self.user_list.pop(i)
                print(f"Пользователь {user.user_name} с ID {user.user_idf} удален")
                ok_remove = True
                break
        if not ok_remove:
            print(f"Пользователь с ID {user_idf} не найден")

    # Выводит список пользователей
    def users_list(self):
        print("Список всех пользователей")
        for user in self.user_list:
            print(f"ID: {user.user_idf}, имя: {user.user_name}, уровень доступа: {user.get_access_level()}")

    # Получить идентификатор по имени
    def get_user_idf(self, user_name):
        user_idf = 0
        for user in self.user_list:
            if user.user_name == user_name:
                user_idf = user.user_idf
        if user_idf == 0:
            print(f"Пользователь с именем {user_name} не найден")
        return user_idf


admin1 = Admin("Александр")

admin1.add_user("Сергей")
admin1.add_user("Сергей")

admin1.add_user("Владимир")
admin1.add_user("Николай")

admin1.users_list()

user_id = admin1.get_user_idf("Григорий")
admin1.remove_user(user_id)

user_id = admin1.get_user_idf("Николай")
admin1.remove_user(user_id)

admin1.users_list()

