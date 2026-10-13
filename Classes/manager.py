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
            conn.commit()
            return True
        except sqlite3.IntegrityError:
            return False

    def delete_player(self, player: str) -> bool:
        with db.get_connection() as conn:
            conn.execute(
                "delete from players where name = ?", (player,)
            )
            conn.commit()
            cursor = conn.cursor()
            if cursor.rowcount == 0:
                return False
            else:
                return True

    def search_player(self, player: str):
        with db.get_connection() as conn:
            cursor = conn.cursor()
            cursor.execute(
                "select * from players where name = ?", (player,)
            )
            return cursor.fetchone()

    def show(self):
        with db.get_connection() as conn:
            cursor = conn.cursor()
            cursor.execute(
                "select * from players order by points desc"
                )
            return cursor.fetchall()