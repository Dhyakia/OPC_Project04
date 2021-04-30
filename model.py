from tinydb import TinyDB

database = TinyDB('data.json')
save = TinyDB('save.json')
players_table = database.table('players')
tournaments_table = database.table('tournaments')
save_table = save.table('save')


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
            # TODO This can't be right
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

    def player_to_database(self):
        serialiazed_player = {
            'Last_name': self.last_name,
            'First_name': self.first_name,
            'Birthdate': self.date_of_birth,
            'Gender': self.gender,
            'Elo': self.elo
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

    def tourmanent_player_list_serializer_save(self, tournament_player_list):
        player_data = []
        for player in tournament_player_list:
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

    def tournament_rounds_list_players_serializer(self, match):
        players_data = []
        for player in match:
            last_name = player.last_name
            first_name = player.first_name
            date_of_birth = player.date_of_birth
            gender = player.gender
            elo = player.elo

            player = (last_name, first_name, date_of_birth, gender, elo)
            players_data.append(player)

        return players_data


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
            tournament_rounds = Round.database_to_tournaments_list_rounds_list_format(
                Player, serialized_tournament['Tournaments_rounds'])   

            tournament = Tournament(name, location, date, duration, number_of_turns, speed, tournament_info,
                                    tournament_players, tournament_rounds)

            return tournament

    def tournament_to_database(self, tournament_to_database):
        serialiazed_tournament = {
            'Name': tournament_to_database.name,
            'Location': tournament_to_database.location,
            'Date': tournament_to_database.date,
            'Duration': tournament_to_database.duration,
            'Number_of_turns': tournament_to_database.number_of_turns,
            'Speed': tournament_to_database.speed,
            'Tournament_info': tournament_to_database.tournament_info,
            'Tournaments_players': Player.tourmanent_player_list_serializer(
                tournament_to_database.tournament_players_list),
            'Tournaments_rounds': Round.tournament_rounds_list_serializer(
                tournament_to_database.rounds_list)
        }

        tournaments_table.insert(serialiazed_tournament)

    @classmethod
    def saved_tournament_to_memory(cls, serialiazed_tournaments):
        all_serialized_tournament = list(serialiazed_tournaments)
        for tournament in all_serialized_tournament:
            tournament_data = cls.tournament_data_deserializer(Tournament, tournament)

        try:
            return tournament_data
        except UnboundLocalError:
            pass

    def tournament_to_database_save(self, tournament_to_database):
        serialiazed_tournament = {
            'Name': tournament_to_database.name,
            'Location': tournament_to_database.location,
            'Date': tournament_to_database.date,
            'Duration': tournament_to_database.duration,
            'Number_of_turns': tournament_to_database.number_of_turns,
            'Speed': tournament_to_database.speed,
            'Tournament_info': tournament_to_database.tournament_info,
            'Tournaments_players': Player.tourmanent_player_list_serializer_save(
                tournament_to_database.tournament_players_list),
            'Tournaments_rounds': Round.tournament_rounds_list_serializer(
                tournament_to_database.rounds_list)
        }

        save_table.insert(serialiazed_tournament)


class Round:

    def __init__(self, match1, match2, match3, match4):
        self.match1 = match_list[0]
        self.match2 = match_list[1]
        self.match3 = match_list[2]
        self.match4 = match_list[3]

    def round_start_data(self, round_name, round_start_time):
        self.name = round_name
        self.start = round_start_time

    def round_end_data(self, round_end_time):
        self.end = round_end_time

    def database_to_tournaments_list_rounds_list_format(self, tournament_rounds_list_serialized):
        rounds_data = []
        for rounds in tournament_rounds_list_serialized:
            match1 = Player.database_to_tournaments_list_players_list_format(Player, rounds[0])
            match2 = Player.database_to_tournaments_list_players_list_format(Player, rounds[1])
            match3 = Player.database_to_tournaments_list_players_list_format(Player, rounds[2])
            match4 = Player.database_to_tournaments_list_players_list_format(Player, rounds[3])
            round_name = rounds[4]
            round_start = rounds[5]
            round_end = rounds[6]

            round = Round(match1, match2, match3, match4)
            round.round_start_data(round_name, round_start)
            round.round_end_data(round_end)
            rounds_data.append(round)

        return rounds_data

    def tournament_rounds_list_serializer(self, tournament_rounds_list):
        round_data = []
        for round in tournament_rounds_list:
            match_1 = Player.tournament_rounds_list_players_serializer(round[0])
            match_2 = Player.tournament_rounds_list_players_serializer(round[1])
            match_3 = Player.tournament_rounds_list_players_serializer(round[2])
            match_4 = Player.tournament_rounds_list_players_serializer(round[3])

            round_name = round[4]
            round_start = round[5]
            try:
                round_end = round[6]
            except IndexError:
                round_end = ''

            round = [match_1, match_2, match_3, match_4, round_name, round_start, round_end]
            round_data.append(round)

        return round_data

class Match:

    def __init__(self, player1, player2):
        self.player1 = player1
        self.player2 = player2
