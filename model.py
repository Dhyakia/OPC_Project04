from tinydb import TinyDB

database = TinyDB('data.json')
save = TinyDB('save.json')
players_table = database.table('players')
tournaments_table = database.table('tournaments')
save_table = save.table('save')


class Tournament:

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
        tournaments_list = []
        all_serialized_tournament = list(serialiazed_tournaments)
        for tournament in all_serialized_tournament:
            tournament_data = cls.tournament_data_deserializer(Tournament, tournament)
            tournaments_list.append(tournament_data)

        return tournaments_list

    @classmethod
    def saved_tournament_to_memory(cls, serialiazed_tournaments):
        all_serialized_tournament = list(serialiazed_tournaments)
        for tournament in all_serialized_tournament:
            tournament_data = cls.tournament_data_deserializer(Tournament, tournament)

        try:
            return tournament
        except UnboundLocalError:
            pass

    def tournament_data_deserializer(self, serialized_tournament):
            name = serialized_tournament['Name']
            location = serialized_tournament['Location']
            date = serialized_tournament['Date']
            duration = serialized_tournament['Duration']
            number_of_turns = serialized_tournament['Number_of_turns']
            speed = serialized_tournament['Speed']
            tournament_info = serialized_tournament['Tournament_info']
            tournament_players = Player.database_to_tournaments_list_players_list_format(
                Player, serialized_tournament['Tournaments_players'])
            tournament_rounds = self.database_to_tournaments_list_rounds_list_format(
                Player, serialized_tournament['Tournaments_rounds'])   

            tournament = Tournament(name, location, date, duration, number_of_turns, speed, tournament_info,
                                    tournament_players, tournament_rounds)

            return tournament

    # TODO Will need to move once round has its own class
    def database_to_tournaments_list_rounds_list_format(self, tournament_rounds_list_serialized):
        rounds_data = []
        for rounds in tournament_rounds_list_serialized:
            match_1 = Player.database_to_tournaments_list_players_list_format(Player, rounds[0])
            match_2 = Player.database_to_tournaments_list_players_list_format(Player, rounds[1])
            match_3 = Player.database_to_tournaments_list_players_list_format(Player, rounds[2])
            match_4 = Player.database_to_tournaments_list_players_list_format(Player, rounds[3])
            round_name = rounds[4]
            round_start = rounds[5]
            round_end = rounds[6]

            round = [match_1, match_2, match_3, match_4, round_name, round_start, round_end]
            rounds_data.append(round)

        return rounds_data


class Player:

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
        players_list = []
        all_serialized_player = list(serialiazed_players)
        for player in all_serialized_player:
            player_data = cls.player_deserializer(Player, player)
            players_list.append(player_data)

        return players_list

    def player_deserializer(self, serialiazed_player):
            last_name = serialiazed_player['Last_name']
            first_name = serialiazed_player['First_name']
            date_of_birth = serialiazed_player['Birthdate']
            gender = serialiazed_player['Gender']
            elo = serialiazed_player['Elo']

            player = Player(last_name, first_name, date_of_birth, gender, elo)
            return player

    @classmethod
    def tourmanent_player_list_serializer(cls, tournament_player_list):
        players_data = []
        for player in tournament_player_list:
            player_data = player.player_serializer()
            players_data.append(player_data)

        return players_data

    def player_serializer(self):
        last_name = self.last_name
        first_name = self.first_name
        date_of_birth = self.date_of_birth
        gender = self.gender
        elo = self.elo

        player = [last_name, first_name, date_of_birth, gender, elo]

        return player

    def player_to_database(self, player_to_dabatase):
        serialiazed_player = {
            'Last_name': player_to_dabatase.last_name,
            'First_name': player_to_dabatase.first_name,
            'Birthdate': player_to_dabatase.date_of_birth,
            'Gender': player_to_dabatase.gender,
            'Elo': player_to_dabatase.elo
        }

        players_table.insert(serialiazed_player)

    def database_to_tournaments_list_players_list_format(self, tournaments_players_list_serialized):
        players_data = []
        for player in tournaments_players_list_serialized:
            last_name = player[0]
            first_name = player[1]
            date_of_birth = player[2]
            gender = player[3]
            elo = player[4]

            players_data.append(Player(last_name, first_name, date_of_birth, gender, elo))

        return players_data


class Match:

    def __init__(self, player1, player2):
        self.player1 = player1
        self.player2 = player2
