from start import path_csv, path_txt, path_xml, path_json, path_html  # , path_sql
from storage.logger import log_event
from contacts.new_contact import input_name
from storage.read_phonebook import read_line_file
from utils.formatting import convert_csv_to_txt, convert_csv_to_xml, convert_csv_to_json, convert_csv_to_html


# , \convert_csv_to_sql


def delete_contact_record():
    del_name = input_name(input('Введите имя или фамилию для удаления контакта: '))
    my_file = read_line_file(path_csv)
    matching_contacts = []

    for index, line in enumerate(my_file):
        if del_name.lower() in line.lower():
            matching_contacts.append((index, line))

    if not matching_contacts:
        print(f'Контакт с именем или фамилией "{del_name}" не найден.')
        log_event('WARNING', f'Контакт "{del_name}" не найден для удаления.')
        return

    if len(matching_contacts) == 1:
        index_to_delete = matching_contacts[0][0]
    else:
        print("Найдены следующие контакты:")
        for idx, (index, contact) in enumerate(matching_contacts):
            print(f"{idx + 1}: {contact.strip()}")

        try:
            selected = int(input("Введите номер контакта для удаления: "))
            index_to_delete = matching_contacts[selected - 1][0]
        except (ValueError, IndexError):
            log_event('ERROR', 'Введен некорректный номер контакта для удаления.')
            print("Введен некорректный номер контакта.")
            return

    confirm = input(f'Вы уверены, что хотите удалить этот контакт? (y/n): ')
    if confirm.lower() == 'y':
        with open(path_csv, 'w', encoding='utf-8') as f:
            for index, line in enumerate(my_file):
                if index != index_to_delete:
                    f.write(line)
        convert_csv_to_txt(path_csv, path_txt)
        convert_csv_to_xml(path_csv, path_xml)
        convert_csv_to_json(path_csv, path_json)
        convert_csv_to_html(path_csv, path_html)
        #        convert_csv_to_sql(path_csv, path_sql)
        print("Контакт удален из телефонной книги.")
        log_event('INFO', f'Контакт "{del_name}" успешно удален.')
    else:
        print("Удаление отменено пользователем.")
        log_event('INFO', 'Пользователь отменил удаление контакта.')
