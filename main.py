#from Classes.player import Player
from Classes.manager import PlayerManager
import Scripts.commands as cmd
import Scripts.database as db

manager = PlayerManager()

db.init_db()

print("""Добро пожаловать в менеджер игроков!
    Вот список доступных команд:
    /help - выводит список команд
    /add - добавляет игрока
    /delete - удалить игрока
    /search - найти игрока (проверить есть ли такой игрок)
    /show - вывести всех игроков
    /update - обновить данные пользователя
    /exit - выход из программы""")

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
                print(f"Игрок найден. {res.get_info()}")
        case "/show":
            res = manager.show()
            print(f"Найдено записей: {len(res)}")
            for player in res:
                print(player.get_info())
        case "/update":
            try:
                name, level, points = cmd.update_player_data()
                res = manager.update_player(name, level, points)
                if res:
                    print("Данные обновлены")
                else:
                    print("Пользователь не найден!")
            except ValueError:
                print("Ошибка: Введены не корректные значения!")
        case "/exit":
            break
        case _:
            print("Неверная команда используйте /help чтобы увидеть список доступных команд")

print("Программа завершена")