from Classes.player import Player

def help():
    'Выводит текст с подсказкой'
    print("""Вот список доступных команд:
        /help - выводит список команд
        /add - добавляет игрока
        /delete - удалить игрока
        /search - найти игрока (проверить есть ли такой игрок)
        /show - вывести всех игроков
        /update - обновить данные пользователя
        /exit - выход из программы""")

def add() -> Player:
    'Запрашивает данные и создаёт на их основе игрока'
    player_name = input("Введите ник игрока: ")
    player_level = int(input("Введите уровень игрока: "))
    player_points = int(input("Введите очки пользователя: "))
    player = Player(player_name, player_level, player_points)
    return player

def search() -> str:
    return input("Ведите имя игрока: ")

def update_player_data() -> tuple[str, int, int]:
    name = input("Введите имя игрока: ")
    lv = int(input("Введите новый уровень: "))
    points = int(input("Введите новое число очков: "))
    return name, lv, points