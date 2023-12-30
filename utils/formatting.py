# Здесь функции для форматирования вывода контактов
# Модуль csv для чтения данных из CSV-файла и модуль xml.etree.ElementTree для создания XML-структуры.
import csv
import json
import xml.etree.ElementTree as ET


# import sqlite3


def convert_csv_to_txt(csv_filename: str, txt_filename: str):
    """
    Конвертирует CSV-файл в текстовый файл.
    :param csv_filename: Имя CSV-файла для чтения.
    :param txt_filename: Имя текстового файла для записи.
    """
    with open(csv_filename, 'r', newline='', encoding='utf-8') as csvfile:
        reader = csv.reader(csvfile)
        contacts = list(reader)

    with open(txt_filename, 'w', encoding='utf-8') as txtfile:
        for contact in contacts:
            txtfile.write(', '.join(contact) + '\n')


def convert_csv_to_xml(csv_file_path, xml_file_path):
    root = ET.Element('Phonebook')

    with open(csv_file_path, newline='', encoding='utf-8') as csvfile:  # Указываем кодировку UTF-8
        reader = csv.reader(csvfile)
        headers = next(reader)  # Пропускаем заголовки

        for row in reader:
            contact = ET.SubElement(root, 'Contact')
            for i, header in enumerate(headers):
                child = ET.SubElement(contact, header)
                child.text = row[i]

    tree = ET.ElementTree(root)
    tree.write(xml_file_path, encoding='utf-8', xml_declaration=True)


def convert_csv_to_json(csv_filename: str, json_filename: str):
    with open(csv_filename, 'r', newline='', encoding='utf-8') as csvfile:
        reader = csv.DictReader(csvfile)
        data = list(reader)

    with open(json_filename, 'w', encoding='utf-8') as jsonfile:
        json.dump(data, jsonfile, ensure_ascii=False, indent=4)


def convert_csv_to_html(csv_filename: str, html_filename: str):
    with open(csv_filename, 'r', newline='', encoding='utf-8') as csvfile:
        reader = csv.reader(csvfile)
        headers = next(reader)

        with open(html_filename, 'w', encoding='utf-8') as htmlfile:
            htmlfile.write('<!DOCTYPE html>\n<html>\n<head>\n<title>Phonebook</title>\n</head>\n<body>\n')
            htmlfile.write('<table border="1">\n<tr>\n')

            for header in headers:
                htmlfile.write(f'<th>{header}</th>\n')

            htmlfile.write('</tr>\n')

            for row in reader:
                htmlfile.write('<tr>\n')
                for cell in row:
                    htmlfile.write(f'<td>{cell}</td>\n')
                htmlfile.write('</tr>\n')

            htmlfile.write('</table>\n</body>\n</html>')

# def convert_csv_to_sql(csv_filename: str, sql_db_path: str):
#    conn = sqlite3.connect(sql_db_path)
#    cursor = conn.cursor()

#    with open(csv_filename, 'r', newline='', encoding='utf-8') as csvfile:
#        reader = csv.reader(csvfile)
#        headers = next(reader)

# Создаем таблицу с использованием имен столбцов из CSV
#        cursor.execute(f"CREATE TABLE IF NOT EXISTS phonebook ({', '.join(headers)});")

# Вставляем данные
#        for row in reader:
#            placeholders = ', '.join('?' * len(row))
#            sql = f"INSERT INTO phonebook VALUES ({placeholders})"
#            cursor.execute(sql, row)

#    conn.commit()
#    conn.close()
