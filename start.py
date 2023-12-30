import os
from contacts.creating import creating_csv

path_csv = os.path.join('storage/data_phonebook', 'Phonebook.csv')
path_txt = os.path.join('storage/data_phonebook', 'Phonebook.txt')
path_xml = os.path.join('storage/data_phonebook', 'Phonebook.xml')
log_path_str = os.path.join('storage/data_phonebook', 'Phonebook_log.csv')
path_json = os.path.join('storage/data_phonebook', 'Phonebook.json')
path_html = os.path.join('storage/data_phonebook', 'Phonebook.html')


# path_sql = os.path.join('storage/data_phonebook', 'Phonebook.sql')


def check():
    valid_csv = os.path.exists(path_csv)

    if not valid_csv:
        print('*.cvs файла нет')
        creating_csv(path_csv)
