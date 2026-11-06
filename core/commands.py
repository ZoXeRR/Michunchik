from core.apps import open_app
from core.utils import get_current_time, open_website, show_help, open_browser


class CommandHandler:
    """Распознаёт текстовые команды и вызывает соответствующие функции."""

    def handle(self, raw_command: str) -> bool:
        command = raw_command.strip()
        normalized = command.lower()

        if normalized in {"привет", "здравствуй", "здравствуйте"}:
            print("Михунчик: Привет! Чем могу помочь?")
        elif normalized in {"время", "сколько времени", "который час"}:
            print(f"Михунчик: Сейчас {get_current_time()}.")
        elif normalized in {"помощь", "команды", "help"}:
            show_help()
        elif normalized in {"выход", "выйти", "стоп", "exit", "quit"}:
            print("Михунчик: До встречи!")
            return False
        elif normalized.startswith("сайт "):
            address = command[5:].strip()
            open_website(address)
        elif normalized.startswith("открой сайт "):
            address = command[len("открой сайт "):].strip()
            open_website(address)
        elif normalized.startswith("открой приложение "):
            app_name = command[len("открой приложение "):].strip()
            open_app(app_name)
        elif normalized.startswith("приложение "):
            app_name = command[len("приложение "):].strip()
            open_app(app_name)
        elif normalized in "браузер":
            open_browser()
        else:
            print(
                "Михунчик: Неизвестная команда. Напиши «помощь», "
                "чтобы посмотреть доступные команды."
            )

        return True
