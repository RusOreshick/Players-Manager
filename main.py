#from Classes.player import Player
from Classes.manager import PlayerManager
import Scripts.commands as cmd

manager = PlayerManager

print("Добро пожаловать в менеджер игроков!\n" \
    "Вот список доступных команд:\n" \
    "/help - выводит список команд\n" \
    "/add - добавляет игрока\n" \
    "/delete - удалить игрока\n" \
    "/search - найти игрока (проверить есть ли такой игрок)\n" \
    "/show - вывести всех игроков\n" \
    "/exit - выход из программы\n")

while True:
    user_command = input("\nВведите команду >>> ")

    match user_command:
        case "/help":
            cmd.help()
        case "/add":
            player = cmd.add()
            manager.add_player(player)
            print(f"Игрок добавлен ({player.get_info()})")
        case "/delete":
            result_search = cmd.search()
            res = manager.delete_player(result_search)
            if res:
                print(f"Игрок {result_search.name} успешно удалён")
            else:
                print(f"Игрок с именем {result_search.name} не найден!")
        case "/search":
            result_search = cmd.search()
            res = manager.search_player(result_search)
            if res:
                print(f"Игрок найден {res.get_info()}")
            else:
                print(f"Игрок с именем {result_search.name} не найден!")
        case "/show":
            manager.show()
        case "/exit":
            break
        case _:
            print("Неверная команда используйте /help чтобы увидеть список доступных команд")

print("Программа завершена")