from tinydb import TinyDB

database = TinyDB('data.json')
players_table = database.table('players')
tournaments_table = database.table('tournaments')


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
        # explicit
        self.last_name = last_name
        self.first_name = first_name
        self.date_of_birth = date_of_birth
        self.gender = gender
        self.elo = elo
        self.score = float(0)
        self.last_played = ""
