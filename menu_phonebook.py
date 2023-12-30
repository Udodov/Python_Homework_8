from start import path_csv
from storage.logger import log_event
from storage.read_phonebook import read_from_file
from contacts.new_contact import new
from contacts.search_contact import search_cont
from contacts.deleting_contact import delete_contact_record


def menu():
    while True:
        print('\nМЕНЮ Телефонной книги\n'
              '1. Просмотреть все существующие контакты\n'
              '2. Добавить новый контакт\n'
              '3. Найти существующий контакт\n'
              '4. Удалить существующий контакт\n'
              '5. Выход\n')
        choice = input('Выберите пункт меню: ')

        match choice:
            case '1':
                my_file = read_from_file(path_csv)
                print(my_file)
                log_event('VIEW', 'Просмотр всех контактов')
                input('Вернуться в меню? Нажмите Enter')
                continue
            case '2':
                new()
                log_event('ADD', 'Добавление нового контакта')
                input('Вернуться в меню? Нажмите Enter')
                continue
            case '3':
                search_cont()
                log_event('SEARCH', 'Поиск контакта')
                input('Вернуться в меню? Нажмите Enter')
                continue
            case '4':
                delete_contact_record()
                log_event('DELETE', 'Удаление контакта')
                input('Вернуться в меню? Нажмите Enter')
                continue
            case '5':
                print('Спасибо, что используете эту телефонную книгу!')
                log_event('EXIT', 'Выход из программы')
                break
            case _:
                log_event('WARNING', f'Неверный выбор в меню: {choice}')
                input('Нет такого пункта...\nДля продолжения нажмите Enter и повторите ввод\n')
                continue
