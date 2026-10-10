from Classes.player import Player
import json

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
    player_level = input("Введите уровень игрока: ")
    player_points = input("Введите очки пользователя: ")
    player = Player(player_name, player_level, player_points)
    return player

def search() -> Player:
    player_name = input("Ведите имя игрока: ")
    player = Player(player_name, 0, 0)
    return player

def save_players(path, manager):
    with open(path, "r", encoding="utf-8") as fl:
        data = json.load(fl)

    if len(manager.players_list) != 0:
        for i in manager.players_list:
            data["players"][i.name] = {"name": i.name, "level": i.level, "points": i.points}

    with open(path, "w", encoding="utf-8") as fl:
        json.dump(data, fl, indent=4)

def download_players(path, players_list: list):
    with open(path, "r", encoding="utf-8") as fl:
        data = json.load(fl)

    for player in data["players"]:
        address = data["players"][player]
        pl = Player(address["name"], address["level"], address["points"])
        players_list.append(pl)