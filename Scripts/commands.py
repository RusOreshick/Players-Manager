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
    player_level = int(input("Введите уровень игрока: "))
    player_points = int(input("Введите очки пользователя: "))
    player = Player(player_name, player_level, player_points)
    return player

def search():
    return input("Ведите имя игрока: ")

def save_players(path: str, players_list: list) -> None:
    data = {"players": {}}
    for pl in players_list:
        data["players"][pl.name] = {
            "name": pl.name,
            "level": pl.level,
            "points": pl.points,
        }
    with open(path, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=4, ensure_ascii=False)

def download_players(path, players_list: list):
    with open(path, "r", encoding="utf-8") as fl:
        data = json.load(fl)

    for player in data["players"]:
        address = data["players"][player]
        pl = Player(address["name"], address["level"], address["points"])
        players_list.append(pl)