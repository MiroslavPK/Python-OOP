from .player import Player

class Team:
    def __init__(self, name: str, rating: int) -> None:
        self.__name = name
        self.__rating = rating
        self.__players: list[Player] = []


    def add_player(self, player: Player) -> str:
        if player in self.__players:
            return f"Player {player.name} has already joined"
        self.__players.append(player)
        return f"Player {player.name} joined team {self.__name}"


    def remove_player(self, player_name: str) -> Player or str:
        players_names = [player.name for player in self.__players]
        if player_name not in players_names:
            return f"Player {player_name} not found"
        player = self.__players[players_names.index(player_name)]
        self.__players.remove(player)
        return player