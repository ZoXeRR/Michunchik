from datetime import datetime
import webbrowser
from urllib.parse import urlparse


def get_current_time() -> str:
    """Возвращает текущие дату и время в локальном часовом поясе."""
    return datetime.now().strftime("%d.%m.%Y, %H:%M:%S")

def open_browser():
    try:
        webbrowser.open("https://google.com")
        print("Михунчик: открываю браузер")
    except Exception as error:
        print(f"Михунчик: Не удалось открыть браузер: {error}")

def open_website(address: str) -> None:
    """Открывает сайт в браузере после базовой проверки адреса."""
    if not address:
        print("Михунчик: Укажи адрес сайта. Например: сайт wikipedia.org")
        return

    url = address.strip()
    if "://" not in url:
        url = "https://" + url

    parsed = urlparse(url)
    if parsed.scheme not in {"http", "https"} or not parsed.netloc:
        print("Михунчик: Похоже, адрес сайта некорректен.")
        return

    try:
        opened = webbrowser.open(url)
        if opened:
            print(f"Михунчик: Открываю {url}")
        else:
            print("Михунчик: Не удалось передать адрес браузеру.")
    except Exception as error:
        print(f"Михунчик: Ошибка при открытии сайта: {error}")


def show_help() -> None:
    """Показывает список поддерживаемых команд."""
    print(
        """
Доступные команды:
  привет                         — поздороваться
  браузер                        — открыть браузер
  время                          — показать дату и время
  сайт wikipedia.org             — открыть сайт в браузере
  открой сайт github.com         — открыть сайт в браузере
  открой приложение калькулятор  — открыть разрешённое приложение
  помощь                         — показать эту справку
  выход                          — завершить работу

Названия приложений задаются в файле config/apps.json.
"""
    )
