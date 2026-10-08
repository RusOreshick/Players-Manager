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