from start import check
from menu_phonebook import menu
from storage.logger import log_event


# Основная функция для запуска программы
def main():
    try:
        menu()
    except KeyboardInterrupt:
        print("\nПрограмма была прервана пользователем.")


# Точка входа в программу
if __name__ == "__main__":
    check()  # Проверка перед началом работы программы
    log_event('CHECK', 'Проверка существования файла Phonebook.csv')
    log_event('INFO', 'Телефонная книга запущена')
    main()  # Запуск основной функции программы
