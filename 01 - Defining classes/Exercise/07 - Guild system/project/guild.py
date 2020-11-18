from project.player import Player


class Guild:
    def __init__(self, name: str):
        self.name = name
        self.players = []

    def assign_player(self, player: Player):
        if player.guild == self.name:
            return f'Player {player.name} is already in the guild.'
        elif player.guild != 'Unaffiliated':
            return f'Player {player.name} is in another guild.'

        player.guild = self.name
        self.players.append(player)
        return f'Welcome player {player.name} to the guild {self.name}'

    def kick_player(self, player_name: str):
        players_in_guild = [player.name for player in self.players]

        if player_name in players_in_guild:
            player = self.players[players_in_guild.index(player_name)]
            self.players.remove(player)
            player.guild = 'Unaffiliated'
            return f'Player {player_name} has been removed from the guild.'

        return f'Player {player_name} is not in the guild.'

    def guild_info(self):
        guild_details = [
            f'Guild: {self.name}',
            ''.join([player.player_info() for player in self.players])
        ]
        return '\n'.join(guild_details)
