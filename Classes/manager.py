from Classes.player import Player
import Scripts.database as db
import sqlite3

class PlayerManager:
    def add_player(self, player: Player) -> bool:
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
        with db.get_connection() as conn:
            cursor = conn.cursor()
            cursor.execute(
                "delete from players where name = ?", (player,)
            )
            return cursor.rowcount != 0

    def search_player(self, player: str) -> Player:
        with db.get_connection() as conn:
            cursor = conn.cursor()
            row = cursor.execute(
                "select * from players where name = ?", (player,)
            ).fetchone()
            if row is None:
                return None
            return Player(row["name"], row["level"], row["points"])

    def show(self) -> list[Player]:
        with db.get_connection() as conn:
            cursor = conn.cursor()
            players = cursor.execute(
                "select * from players order by points desc"
                ).fetchall()
            list_players = []
            for player in players:
                list_players.append(Player(player["name"], player["level"], player["points"]))
            return list_players