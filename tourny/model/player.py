from tourny.model.tinydb import players_table


class Player:
    """Player class, it's a player."""

    def __init__(self, last_name, first_name, date_of_birth, gender, elo):
        self.last_name = last_name
        self.first_name = first_name
        self.date_of_birth = date_of_birth
        self.gender = gender
        self.elo = elo
        self.score = float(0)
        self.last_played = ""

    @classmethod
    def database_to_players_list(cls, serialiazed_players):
        """Takes in serialized players, return a list of players object."""
        players_list = []
        all_serialized_player = list(serialiazed_players)
        for serialized_player in all_serialized_player:
            player = cls.player_deserializer(serialized_player)
            players_list.append(player)

        return players_list

    @classmethod
    def player_deserializer(cls, serialiazed_player):
        """Takes a serialized player and return a player object."""
        last_name = serialiazed_player['Last_name']
        first_name = serialiazed_player['First_name']
        date_of_birth = serialiazed_player['Birthdate']
        gender = serialiazed_player['Gender']
        elo = serialiazed_player['Elo']

        player = cls(last_name, first_name, date_of_birth, gender, elo)
        return player

    @classmethod
    def tourmanent_player_list_serializer(cls, tournament_player_list):
        """Takes a list of players inside a tournament, and return a serialized list of players."""
        players_data = []
        for player in tournament_player_list:
            player_data = player.player_serializer()
            players_data.append(player_data)

        return players_data

    def player_serializer(self):
        """Serialized a player object, return a list."""
        last_name = self.last_name
        first_name = self.first_name
        date_of_birth = self.date_of_birth
        gender = self.gender
        elo = self.elo

        player = [last_name, first_name, date_of_birth, gender, elo]

        return player

    def player_to_database(self):
        """Add a player object into the database."""
        serialiazed_player = {
            'Last_name': self.last_name,
            'First_name': self.first_name,
            'Birthdate': self.date_of_birth,
            'Gender': self.gender,
            'Elo': self.elo
        }

        players_table.insert(serialiazed_player)

    @classmethod
    def database_to_tournaments_list_players_list_format(cls, tournament_players_list):
        """De-serializer players inside a tournament and returns a list of player objects."""
        players_list = []
        for tournament_player in tournament_players_list:
            last_name = tournament_player[0]
            first_name = tournament_player[1]
            date_of_birth = tournament_player[2]
            gender = tournament_player[3]
            elo = tournament_player[4]

            player = cls(last_name, first_name, date_of_birth, gender, elo)
            players_list.append(player)

        return players_list

    @classmethod
    def database_to_tournaments_round_list_format(cls, tournament_player):
        """Takes in a player from the database, return a player object."""
        last_name = tournament_player[0]
        first_name = tournament_player[1]
        date_of_birth = tournament_player[2]
        gender = tournament_player[3]
        elo = tournament_player[4]

        player = cls(last_name, first_name, date_of_birth, gender, elo)

        return player

    @classmethod
    def tourmanent_player_list_serializer_save(cls, tournament_players_list):
        """Takes in a tournament's players list, and serialize each player."""
        player_data = []
        for player in tournament_players_list:
            last_name = player.last_name
            first_name = player.first_name
            date_of_birth = player.date_of_birth
            gender = player.gender
            elo = player.elo
            score = player.score
            last_played = player.last_played

            player = [last_name, first_name, date_of_birth, gender, elo, score, last_played]
            player_data.append(player)

        return player_data

    def tournament_rounds_list_players_serializer(self):
        """Serialize a player and return a tuple."""
        last_name = self.last_name
        first_name = self.first_name
        date_of_birth = self.date_of_birth
        gender = self.gender
        elo = self.elo

        player = (last_name, first_name, date_of_birth, gender, elo)
        return player
