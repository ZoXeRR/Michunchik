import json
import platform
import subprocess
from pathlib import Path
from typing import Any


PROJECT_ROOT = Path(__file__).resolve().parent.parent
APPS_CONFIG = PROJECT_ROOT / "config" / "apps.json"


def _load_app_config() -> dict[str, Any]:
    """Загружает белый список приложений из JSON-файла."""
    try:
        with APPS_CONFIG.open("r", encoding="utf-8") as file:
            data = json.load(file)
        return data if isinstance(data, dict) else {}
    except FileNotFoundError:
        print(f"Михунчик: Не найден файл настроек: {APPS_CONFIG}")
    except json.JSONDecodeError:
        print("Михунчик: В config/apps.json допущена ошибка формата JSON.")
    except OSError as error:
        print(f"Михунчик: Не удалось прочитать настройки: {error}")
    return {}


def open_app(app_name: str) -> None:
    """
    Запускает только приложение из белого списка.
    Команда запуска задаётся массивом аргументов; shell=True не используется.
    """
    if not app_name:
        print("Михунчик: Укажи название приложения.")
        return

    config = _load_app_config()
    system_name = platform.system().lower()
    system_apps = config.get(system_name, {})
    if not isinstance(system_apps, dict):
        system_apps = {}

    app_command = system_apps.get(app_name.lower())

    if not app_command:
        available = ", ".join(sorted(system_apps)) or "нет настроенных приложений"
        print(
            f"Михунчик: Приложение «{app_name}» не находится в белом списке.\n"
            f"Доступно для этой ОС: {available}"
        )
        return

    if not isinstance(app_command, list) or not all(
        isinstance(part, str) for part in app_command
    ):
        print("Михунчик: Некорректная команда запуска в config/apps.json.")
        return

    try:
        subprocess.Popen(app_command)
        print(f"Михунчик: Запускаю приложение «{app_name}».")
    except FileNotFoundError:
        print(
            "Михунчик: Команда запуска не найдена. Проверь путь или название "
            "приложения в config/apps.json."
        )
    except OSError as error:
        print(f"Михунчик: Не удалось запустить приложение: {error}")
