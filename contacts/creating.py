def creating_csv(path_file: str):
    with open(path_file, 'a+', encoding='utf-8') as file:
        file.write(f'ID Контакта;  Имя;  Фамилия;  Номер телефона;  e-mail; Описание\n')


def creating_contact(path_file: str, contact_details: str):
    with open(path_file, 'a', encoding='utf-8') as file:
        file.write(contact_details)
