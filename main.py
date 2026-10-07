from Classes.player import Player
from Classes.manager import PlayerManager

manager = PlayerManager

while True:
    print("Добро пожаловать в менеджер игроков!\n" \
    "Вот список доступных команд:\n" \
    "/help - выводит список команд\n" \
    "/add - добавляет игрока")
    
    """Дальше должны быть команды
    /delete - удалить игрока
    /search - найти игрока (проверить есть ли такой игрок)
    /show - вывести всех игроков"""