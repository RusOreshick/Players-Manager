#from Classes.player import Player
from Classes.manager import PlayerManager
import Scripts.commands as cmd
import Scripts.database as db

manager = PlayerManager()

db.init_db()

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
            result = manager.add_player(player)
            if result:
                print(f"Игрок добавлен ({player.get_info()})")
            else:
                print("Игрок с таким именем уже есть!")
        case "/delete":
            result_search = cmd.search()
            res = manager.delete_player(result_search)
            if res:
                print(f"Игрок {result_search} успешно удалён")
            else:
                print(f"Игрок с именем {result_search} не найден!")
        case "/search":
            result_search = cmd.search()
            res = manager.search_player(result_search)
            if res is None:
                print(f"Игрок с именем {result_search} не найден!")
            else:
                player = dict(res)
                print(f"Игрок найден. Имя: {player['name']}; Уровень: {player['level']}; Очки: {player['points']}")
        case "/show":
            manager.show()
        case "/exit":
            break
        case _:
            print("Неверная команда используйте /help чтобы увидеть список доступных команд")

print("Программа завершена")