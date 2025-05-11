# Задача: Создай класс `Task`, который позволяет управлять задачами (делами).
# У задачи должны быть атрибуты: описание задачи, срок выполнения и статус (выполнено/не выполнено).
# Реализуй функцию для добавления задач, отметки выполненных задач и вывода списка текущих (не выполненных) задач.

import datetime

class Task:
    def __init__(self, task_id, task_name, task_start, task_time, task_status = False, task_del = False):
        self.task_id = task_id
        self.task_name = task_name
        self.task_start = task_start
        self.task_time = task_time
        self.task_status = task_status
        self.task_del = task_del
        print(f"Создана задача {self.task_name} с id = {self.task_id} время {self.task_time.strftime("%d.%m.%y %H:%M")}")

    def add_task(self, task_time):
        self.task_time = task_time
        self.task_status = True
        task_list.append(self)
        print(f"Задача с id {self.task_id} добавлена в список активных задач, срок {self.task_time.strftime("%d.%m.%y %H:%M")}")

    def final_task(self):
        self.task_status = False

def active_task_list():
    print("Список активных задач:")
    for task in task_list:
        if task.task_status:
            task_t = task.task_time.strftime("%d.%m.%y %H:%M")
            print(f"ID: {task.task_id} Задача: {task.task_name} Срок: {task_t}")

def final_task_list():
    print("Список завершенных задач:")
    for task in task_list:
        if not task.task_status and not task.task_del:
            task_t = task.task_time.strftime("%d.%m.%y %H:%M")
            print(f"ID: {task.task_id} Задача: {task.task_name} Срок: {task_t}")

def del_final_task():
    for task in task_list:
        if not task.task_status and not task.task_del:
            task.task_del = True
    print("Завершенные задачи удалены")

def del_all_task():
    task_list.clear()
    print("Список задач очищен")

task_list = []
print("Менеджер задач, Вер.1.0")
while True:
    print("Меню действий: 1-добавить, 2-завершить, 3-список активных, 4-список завершенных, 5-удалить завершенные, 6-удалить все\n"
                   "0 - выход")
    action = input("Введите действие с задачами: ")
    if action == "0":
        break
    elif action == "1":
        new_name = input("Введите наименование новой задачи: ")
        new_time_str = input("Введите срок выполнения новой задачи (в формате DD.MM.YY HH:MM): ")
        id_t = len(task_list) + 1
        cur_time = datetime.datetime.now()
        new_task = Task(id_t, new_name, cur_time, cur_time)
        new_time = datetime.datetime.strptime(new_time_str, "%d.%m.%y %H:%M")
        new_task.add_task(new_time)
    elif action == "2":
        id_t = int(input("Введите ID задачи для завершения: "))
        if id_t < 1 or id_t > len(task_list):
            print(f"Ошибка: задачи с ID {id_t} не существует")
        elif not task_list[id_t-1].task_status :
            print(f"Задача с ID {id_t} уже завершена")
        else:
            task_list[id_t-1].final_task()
            print(f"Задача с ID {id_t} завершена")
    elif action == "3":
        active_task_list()
    elif action == "4":
        final_task_list()
    elif action == "5":
        del_final_task()
    elif action == "6":
        del_all_task()
    else :
        print("Введена неверная опция, повторите ввод")

print("Конец работы")


