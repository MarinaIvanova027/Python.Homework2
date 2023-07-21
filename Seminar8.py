# Задача 38: Дополнить телефонный справочник возможностью изменения и удаления данных. 
# Пользователь также может ввести имя или фамилию, и Вы должны реализовать функционал для изменения 
# и удаления данных.

# Иванов Иван;89876543210
# Петров Петр;88795462130
# Сидоров Федор;81230456789


from pathlib import Path
FILE_PATH = Path('phonebook.txt')
print(FILE_PATH)

# Создает (добавляет) контакты
def add_contact():
    with open(FILE_PATH, 'a', encoding='utf8') as file:
        info = input('Введите данные: ')
        file.write(f'{info}\n')
add_contact()

# Показывает контакты
def show_contact():
    with open(FILE_PATH, 'r', encoding='utf8') as file:
        # print([lines for lines in file])
        print(*[line for line in file])
        # print(file.readlines())

# Находит нужный контакт
def find_contact():
    list_1 = []
    serch = input('Введите искомое: ').strip()
    with open(FILE_PATH, 'r', encoding='utf8') as file:
        for contact in file:
            if serch in contact:
                list_1.append(contact)
        print(*[line for line in list_1])

# Изменяет контакт   ?????????????????????????????????????????????????????
# def edit_contact():
#     list_1 = []
#     with open(FILE_PATH, 'r', encoding='utf8') as file:
#         name = input("Введите контакт: ")
#         for contact in file:
#             if contact == name:
#                 new_name = input("Введите изменения в контакт:  ")
#                 name = new_name
#                 break
#             # with open(FILE_PATH, "w", encoding='utf-8') as file:  
#             #     file.write('{name}\n')        
#         print(*[line for line in list_1])
# edit_contact()        

# Удаляет контакт  ??????????????????????????????????????????
# def delete_contact():
#     with open(FILE_PATH, 'r', encoding='utf8') as file:
#         name = input('Введите контакт: ')
#         for contact in file:
#             if contact == name:
#                 name_del = input('Вы хотите удалить этот контакт (yes/no)?: ')
#                 if name_del == 'yes':
#                     file.remove(name)
#                 print('Вы удалили контакт')
#         # print(*[line for line in list_1])
# delete_contact()


def choose():
    flag = True
    while flag:
        n = input('Введите действие: ')
        match n:
            case '1':
                add_contact()
            case '2':
                show_contact()
            case '3':
                find_contact()
            case '4':
                edit_contact()
            case '5':
                delete_contact()
            case '6':
                flag = False

choose()