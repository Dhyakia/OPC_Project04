from tinydb import TinyDB

database = TinyDB('data.json')
save = TinyDB('save.json')
players_table = database.table('players')
tournaments_table = database.table('tournaments')
save_table = save.table('save')


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


class Tournament:
    """Tournament class. It's a tournament."""

    NUMBER_OF_TOURNAMENT_PLAYER = 8

    def __init__(self, name, location, date, duration=int(1), number_of_turns=4, speed='',
                 tournament_info='', players_list=[], rounds_list=[]):
        self.name = name
        self.location = location
        self.date = date
        self.duration = duration
        self.number_of_turns = number_of_turns
        self.speed = speed
        self.tournament_info = tournament_info
        self.tournament_players_list = players_list
        self.rounds_list = rounds_list

    @classmethod
    def database_to_tournaments_list(cls, serialiazed_tournaments):
        """Takes in the tournaments from the database and return a list of tournaments object."""
        tournaments_list = []
        all_serialized_tournament = list(serialiazed_tournaments)
        for tournament in all_serialized_tournament:
            tournament_data = cls.tournament_data_deserializer(tournament)
            tournaments_list.append(tournament_data)

        return tournaments_list

    @classmethod
    def tournament_data_deserializer(cls, serialized_tournament):
        """De-serialize a tournament and return a tournament object."""
        name = serialized_tournament['Name']
        location = serialized_tournament['Location']
        date = serialized_tournament['Date']
        duration = serialized_tournament['Duration']
        number_of_turns = serialized_tournament['Number_of_turns']
        speed = serialized_tournament['Speed']
        tournament_info = serialized_tournament['Tournament_info']
        tournament_players = Player.database_to_tournaments_list_players_list_format(
            serialized_tournament['Tournaments_players'])
        tournament_rounds = Round.database_to_tournaments_list_rounds_list_format(
            serialized_tournament['Tournaments_rounds'])

        tournament = cls(name, location, date, duration, number_of_turns, speed, tournament_info,
                         tournament_players, tournament_rounds)

        return tournament

    def tournament_to_database(self):
        """Serialize a tournament, then add it to the tournament table."""
        serialiazed_tournament = {
            'Name': self.name,
            'Location': self.location,
            'Date': self.date,
            'Duration': self.duration,
            'Number_of_turns': self.number_of_turns,
            'Speed': self.speed,
            'Tournament_info': self.tournament_info,
            'Tournaments_players': Player.tourmanent_player_list_serializer(self.tournament_players_list),
            'Tournaments_rounds': Round.tournament_rounds_list_serializer(self.rounds_list)
        }

        tournaments_table.insert(serialiazed_tournament)

    @classmethod
    def saved_tournament_to_memory(cls, serialiazed_tournaments):
        """De-serialize a tournament, return it as an saved tournament if possible."""
        all_serialized_tournament = list(serialiazed_tournaments)
        for tournament in all_serialized_tournament:
            tournament_data = cls.tournament_data_deserializer(tournament)

        try:
            return tournament_data
        except UnboundLocalError:
            pass

    def tournament_to_database_save(self):
        """Serialize a tournament, then add it to the save table."""
        serialiazed_tournament = {
            'Name': self.name,
            'Location': self.location,
            'Date': self.date,
            'Duration': self.duration,
            'Number_of_turns': self.number_of_turns,
            'Speed': self.speed,
            'Tournament_info': self.tournament_info,
            'Tournaments_players': Player.tourmanent_player_list_serializer_save(
                self.tournament_players_list),
            'Tournaments_rounds': Round.tournament_rounds_list_serializer(
                self.rounds_list)
        }

        save_table.insert(serialiazed_tournament)


class Round:
    """Class round. It's a round."""

    def __init__(self, matchs_list):
        self.matchs_list = matchs_list

    def round_start_data(self, round_name, round_start_time):
        self.name = round_name
        self.start = round_start_time

    def round_end_data(self, round_end_time):
        self.end = round_end_time

    @classmethod
    def database_to_tournaments_list_rounds_list_format(cls, tournament_rounds_list_serialized):
        """De-serialize round data inside a tournament, returns a rounds object."""
        rounds_data = []
        for rounds in tournament_rounds_list_serialized:
            match1 = Match.match_player_deserializer(rounds[0])
            match2 = Match.match_player_deserializer(rounds[1])
            match3 = Match.match_player_deserializer(rounds[2])
            match4 = Match.match_player_deserializer(rounds[3])
            round_name = rounds[4]
            round_start = rounds[5]

            try:
                round_end = rounds[6]
            except IndexError:
                round_end = ""

            round = cls([match1, match2, match3, match4])
            round.round_start_data(round_name, round_start)
            round.round_end_data(round_end)
            rounds_data.append(round)

        return rounds_data

    def tournament_rounds_list_serializer(tournament_rounds_list):
        """Serialize a round object."""
        rounds_data = []
        for a_round in tournament_rounds_list:
            a_round_list = []
            for a_match in a_round.matchs_list:
                match = Match.match_player_serializer(a_match)
                a_round_list.append(match)

            round_name = a_round.name
            a_round_list.append(round_name)

            round_start = a_round.start
            a_round_list.append(round_start)
            try:
                round_end = a_round.end
                a_round_list.append(round_end)
            except AttributeError:
                round_end = ''

            rounds_data.append(a_round_list)

        return rounds_data


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

    def match_player_deserializer(self, matchs_list):
        """De-serialize a match, return a match object."""
        player1 = Player.database_to_tournaments_round_list_format(matchs_list[0])
        player2 = Player.database_to_tournaments_round_list_format(matchs_list[1])

        match = self(player1, player2)
        return match
