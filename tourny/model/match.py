from tourny.model.player import Player


class Match:
    """Match class. Its's a match."""

    def __init__(self, player1, player2):
        self.player1 = player1
        self.player2 = player2

    @classmethod
    def match_player_serializer(cls, match):
        """Serialized a match, return said match."""
        player1 = Player.tournament_rounds_list_players_serializer(match.player1)
        player2 = Player.tournament_rounds_list_players_serializer(match.player2)

        match = [player1, player2]
        return match

    @classmethod
    def match_player_deserializer(cls, matchs_list):
        """De-serialize a match, return a match object."""
        player1 = Player.database_to_tournaments_round_list_format(matchs_list[0])
        player2 = Player.database_to_tournaments_round_list_format(matchs_list[1])

        match = cls(player1, player2)
        return match
