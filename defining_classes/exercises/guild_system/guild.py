class Guild:
    def __init__(self, name: str):
        self.name = name
        self.players = []

    def assign_player(self, player):
        if player in self.players:
            return f"Player {player.name} is already in the guild."
        elif player not in self.players and player.guild != "Unaffiliated":
            return f"Player {player.name} is in another guild."
        else:
            player.guild = self.name
            self.players.append(player)
            return f"Welcome player {player.name} to the guild {self.name}"

    def kick_player(self, player_name):
        filtered_players = [p for p in self.players if p.name == player_name]
        if not filtered_players:
            return f"Player {player_name} is not in the guild."
        player = filtered_players[0]
        self.players.remove(player)
        player.guild = "Unaffiliated"
        return f"Player {player_name} has been removed from the guild."

    def guild_info(self):
        result = f"Guild: {self.name}\n"
        for player in self.players:
            result += player.player_info()
        return result
