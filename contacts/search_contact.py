import logging
from start import path_csv
# from storage.logger import log_event
from contacts.new_contact import input_name
from storage.read_phonebook import read_line_file


def search_cont():
    search_name = input_name(input('Введите имя или фамилию для поиска контакта: ')).lower()
    logging.debug(f"Поиск контакта: {search_name}")  # Используем уровень DEBUG для отладочной информации

    try:
        contacts_list = read_line_file(path_csv)
    except Exception as e:
        logging.error(f"Ошибка при чтении файла: {e}")  # Используем уровень ERROR для ошибок
        return

    found_contacts = []  # Список для хранения найденных контактов

    for contact in contacts_list:
        fields = contact.lower().split(';')
        if fields[1].strip() == search_name or fields[2].strip() == search_name:
            found_contacts.append(contact)

    if found_contacts:
        logging.info(
            f"Найдено контактов: {len(found_contacts)}")  # Используем уровень INFO для информационных сообщений
        print('Найденные контакты:')
        for contact in found_contacts:
            print(contact)
    else:
        logging.warning(
            f"Контакт с именем или фамилией {search_name} не найден.")  # Используем уровень WARNING для предупреждений
        print('Контакт с таким именем или фамилией не найден.')
