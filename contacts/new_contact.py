import time
from start import path_csv, path_txt, path_xml, path_json, path_html  # , path_sql
from storage.logger import log_event
from contacts.creating import creating_contact
from utils.formatting import convert_csv_to_txt, convert_csv_to_xml, convert_csv_to_json, convert_csv_to_html


# ,\ convert_csv_to_sql


def new():
    # Генерация уникального ID на основе текущего времени
    contact_id = str(int(time.time() * 1000))

    firstname = input_name(input('Введите имя: '))
    lastname = input_name(input('Введите фамилию: '))
    phone = input('Введите номер телефона: ')
    email = input('Введите E-mail: ')
    description = input('Добавьте описание к контакту: ')

    # Добавление ID в начало строки с деталями контакта
    contact_details = (
            contact_id + '; ' + firstname + ';  ' + lastname + ";  " + phone + ';  ' + email + '; ' + description + '\n')
    # Вызов функции для создания контакта в csv-файл
    creating_contact(path_csv, contact_details)

    # Вызов функции для конвертации в txt-файл
    convert_csv_to_txt(path_csv, path_txt)

    # Вызов функции для конвертации в xml-файл
    convert_csv_to_xml(path_csv, path_xml)

    # Вызов функции для конвертации в json-файл
    convert_csv_to_json(path_csv, path_json)

    # Вызов функции для конвертации в html-файл
    convert_csv_to_html(path_csv, path_html)

    # Вызов функции для конвертации в sql-файл
    # convert_csv_to_sql(path_csv, path_sql)

    log_event('INFO', f'Новая запись в телефонной книге: \n {contact_details} успешно создана!')
    print(f'Новая запись в телефонной книге: \n {contact_details} успешно создана!')


def input_name(name):
    # Удаляем пробелы в начале и конце строки
    name = name.strip()
    # Заменяем все пробелы между словами на '_'
    name = name.replace(" ", "_")
    # Делаем первую букву каждого слова заглавной, разделяя по '_'
    name = "_".join(word.capitalize() for word in name.split("_"))
    return name

# def input_name(name):
# Удаляем пробелы в начале и конце строки и приводим каждое слово к нужному формату
#    return name.strip().title()
