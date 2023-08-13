# Вывод меню и выборт пункта
def show_menu():
    print("\nВыберите необходимое действие:\n"
          "1. Отобразить все заметки\n"
          "2. Найти заметку по идентификатору\n"
          "3. Найти заметку по заголовку\n"
          "4. Найти заметку по дате\n"
          "5. Добавить заметку в список\n"
          "6. Удалить заметку из списка\n"
          "7. Изменить данные заметки\n"
          "8. Сохранить заметки в новом файле\n"
          "9. Закончить работу")
    choice = int(input())
    return choice

# Трансформируем данные из файла в список из словарей
def parse_csv(filename):
    results = []
    fields = ["Идентификатор", "Заголовок", "Тело", "Дата"]
    with open(filename, 'r', encoding='utf-8') as data:
        for line in data:
            record = dict(zip(fields, line.strip().split(';')))
            results.append(record)
    return results

# Выполняем функции работы с заметками в зависимости от выбранного пункта меню
def work_with_notes():
    choice = show_menu()
    notes = parse_csv('notes.csv')

    while (choice != 9):
        if choice == 1:
            show_noteslist(notes)
        elif choice == 2:
            show_noteslist(find_by_id(notes))
        elif choice == 3:
            show_noteslist(find_by_title(notes))
        elif choice == 4:
            show_noteslist(find_by_date(notes))
        elif choice == 5:
            add_new_note(notes)
            write_csv('notes.csv', notes)
        elif choice == 6:
            delete_note(notes)
            rewrite_csv('notes.csv', notes)
        elif choice == 7:
            change_notedata(notes)
            rewrite_csv('notes.csv', notes)
        elif choice == 8:
            make_csv()
        choice = show_menu()

# 1 - Отобразить все заметки
def show_noteslist(notes):
    for elem in notes:
        for key in elem:
            print(f'{key} : {elem[key]}')
        print()

# 2 - Найти заметку по идентификатору
def find_by_id(notes):
    id = input('Введите id заметки для поиска: ')
    results = []
    for elem in notes:
        if elem['Идентификатор'] == id:
            results.append(elem)
    return results

# 3 - Найти заметку по заголовку
def find_by_title(notes):
    title = input('Введите заголовок заметки для поиска: ')
    results = []
    for elem in notes:
        if elem['Заголовок'] == title:
            results.append(elem)
    return results

# 4 - Найти заметку по дате
def find_by_date(notes):
    date = input('Введите дату заметки для поиска (в формате дд.мм.гг): ')
    results = []
    for elem in notes:
        if elem['Дата'] == date:
            results.append(elem)
    return results

# 5 - Добавить заметку в список
def add_new_note(notes):
    record = dict()
    for k in notes[0].keys():
        record[k] = input(f'Введите {k}: ')
    notes.append(record)

def write_csv(filename, notes):
    with open(filename, 'a', encoding='utf-8') as data:
        line = ''
        for v in notes[-1].values():
            line += v + ';'
        data.write(f'{line[:-1]}\n')

# 6 - Удалить заметку из списка
def delete_note(notes):
    note = input('Введите идентификатор, заголовок или дату заметки, которую необходимо удалить: ')
    for elem in notes:
        for v in elem.values():
            if v == note:
                notes.remove(elem)

def rewrite_csv(filename, notes):
    with open(filename, 'w', encoding='utf-8') as data:
        for i in range(len(notes)):
            line = ''
            for v in notes[i].values():
                line += v + ';'
            data.write(f'{line[:-1]}\n')

# 7 - Изменить данные заметки
def change_notedata(notes):
    note = input('Введите идентификатор, заголовок или дату заметки, данные которой необходимо изменить: ')
    changed_atr = input('Введите наименование атрибута, который необходимо изменить: ')
    new_atr = input('Введите новое значение атрибута: ')
    for elem in notes:
        for v in elem.values():
            if v == note:
                elem[changed_atr] = elem[changed_atr].replace(elem[changed_atr],new_atr)

# 8 - Сохранить заметки в новом файле
def make_csv():
    filename = input('Введите имя файла для сохранения: ')
    shutil.copyfile('notes.csv',f'{filename}.csv')

# 9 - Закончить работу - программа просто выйдет из цикла while и закончит работу

import shutil
work_with_notes()