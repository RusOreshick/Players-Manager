class Player:
    def __init__(self, name: str, level: int, points: int):
        self.name = name
        self.level = level
        self.points = points

    def get_info(self) -> str:
        return f"Имя игрока {self.name}, Уровень {self.level}, Число очков {self.points}"