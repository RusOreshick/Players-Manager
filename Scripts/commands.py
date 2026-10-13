from Classes.player import Player

def help():
    'Выводит текст с подсказкой'
    print("Вот список доступных команд:\n" \
        "/help - выводит список команд\n" \
        "/add - добавляет игрока\n" \
        "/delete - удалить игрока\n" \
        "/search - найти игрока (проверить есть ли такой игрок)\n" \
        "/show - вывести всех игроков\n" \
        "/exit - выход из программы\n")

def add() -> Player:
    'Запрашивает данные и создаёт на их основе игрока'
    player_name = input("Введите ник игрока: ")
    player_level = int(input("Введите уровень игрока: "))
    player_points = int(input("Введите очки пользователя: "))
    player = Player(player_name, player_level, player_points)
    return player

def search():
    return input("Ведите имя игрока: ")