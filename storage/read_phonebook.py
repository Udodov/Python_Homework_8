from storage.logger import log_event


def read_from_file(path: str) -> str:
    try:
        with open(path, 'r', encoding='utf-8') as file:
            data = file.read()
        log_event('INFO', 'Успешное чтение данных из файла')
        return data
    except FileNotFoundError:
        log_event('ERROR', 'Файл не найден')
        return ""  # Возвращаем пустую строку вместо None
    except Exception as e:
        log_event('ERROR', f'Произошла ошибка при чтении файла: {e}')
        return ""  # Возвращаем пустую строку вместо None


def read_line_file(path_file: str):
    try:
        with open(path_file, 'r+', encoding='utf-8') as file:
            return file.readlines()
    except FileNotFoundError:
        log_event('ERROR', f'Файл не найден: {path_file}')
    except Exception as e:
        log_event('ERROR', f'Произошла ошибка при чтении файла {path_file}: {e}')
    return None
