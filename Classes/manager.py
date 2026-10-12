from Classes.player import Player
import Scripts.database as db
import sqlite3

class PlayerManager:
    def __init__(self):
        self.players_list = []

    def add_player(self, player: Player) -> None:
        try:
            with db.get_connection() as conn:
                conn.execute(
                    "insert into players(name, level, points) values (?, ?, ?)",
                    (player.name, player.level, player.points)
                )
            return True
        except sqlite3.IntegrityError:
            return False

    def delete_player(self, player: str) -> bool:
        #Проверяем наличие игрока в списке а после удаляем возвращая true
        #Иначе возвращаем false
        for pl in self.players_list:
            if player == pl.name:
                self.players_list.remove(pl)
                return True
        return False

    def search_player(self, player: str):
        #Тот же принцип что и с удалением только не трогаем игрока
        for pl in self.players_list:
            if player == pl.name:
                return pl
        return False

    def show(self):
        pl_list = self.players_list
        if len(pl_list) > 0:
            for i in pl_list:
                print(i.get_info())
        else:
            print("Список пуст.")