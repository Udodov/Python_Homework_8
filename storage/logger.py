import logging
from start import log_path_str
# from datetime import datetime as dt
from pathlib import Path

# Определяем путь к файлу лога. Преобразуем строку в объект Path
log_path = Path(log_path_str)

# Создаем директорию, если она не существует
log_path.parent.mkdir(parents=True, exist_ok=True)

# Настраиваем логгер
logging.basicConfig(
    filename=str(log_path),
    level=logging.DEBUG,
    format='%(asctime)s | %(levelname)s | %(message)s',
    datefmt='%Y-%m-%d | %H:%M:%S'
)


def log_event(event_type: str, description: str) -> None:
    """Функция для записи событий в лог."""
    # Используем стандартный логгер для записи событий
    if event_type == 'ERROR':
        logging.error(description)
    elif event_type == 'WARNING':
        logging.warning(description)
    else:
        logging.info(description)  # Для остальных типов используем уровень INFO
