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
            last_name = player['Last_name']
            first_name = player['First_name']
            date_of_birth = player['Birthdate']
            gender = player['Gender']
            elo = player['Elo']

            player = cls(last_name, first_name, date_of_birth, gender, elo)
            players_list.append(player)

        return players_list

    def player_to_database(self, player_to_dabatase):
        serialiazed_player = {
            'Last_name': player_to_dabatase.last_name,
            'First_name': player_to_dabatase.first_name,
            'Birthdate': player_to_dabatase.date_of_birth,
            'Gender': player_to_dabatase.gender,
            'Elo': player_to_dabatase.elo
        }

        players_table.insert(serialiazed_player)

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

class Match:

    def __init__(self, player1, player2):
        self.player1 = player1
        self.player2 = player2
