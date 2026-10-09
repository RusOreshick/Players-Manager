from Classes.player import Player

class PlayerManager:
    players_list = []

    def add_player(player: Player) -> None:
        PlayerManager.players_list.append(player)

    def delete_player(player: Player) -> bool:
        #Проверяем наличие игрока в списке а после удаляем возвращая true
        #Иначе возвращаем false
        for pl in PlayerManager.players_list:
            if player.name == pl.name:
                PlayerManager.players_list.remove(pl)
                return True
            else:
                return False

    def search_player(player: Player) -> bool:
        #Тот же принцип что и с удалением только не трогаем игрока
        if player in PlayerManager.players_list:
            return True
        else:
            return False

    def show():
        pl_list = PlayerManager.players_list
        if len(pl_list) > 0:
            for i in pl_list:
                print(i.get_info())
        else:
            print("Список пуст.")