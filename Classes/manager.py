from Classes.player import Player

class PlayerManager:
    def __init__(self):
        self.players_list = []

    def add_player(self, player: Player) -> None:
        self.players_list.append(player)

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