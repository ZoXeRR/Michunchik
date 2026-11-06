from core.commands import CommandHandler


class Assistant:
    """Текстовое ядро помощника: принимает команды и передаёт их обработчику."""

    def __init__(self) -> None:
        self.handler = CommandHandler()

    def run(self) -> None:
        print("Привет! Я Михунчик — текстовый помощник.")
        print("Напиши «помощь», чтобы увидеть список команд.")

        while True:
            try:
                user_input = input("\nТы: ").strip()
            except (EOFError, KeyboardInterrupt):
                print("\nМихунчик: Завершаю работу.")
                break

            if not user_input:
                continue

            should_continue = self.handler.handle(user_input)
            if not should_continue:
                break
