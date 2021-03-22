

class Tournament:

    TPLAYER_COUNTER = 0
    ROUND_COUNTER = 0
    TPLAYER_LIST = []
    ROUND_LIST = []

    def __init__(self, name="", location="", date="", duration=1, number_of_turns=4, speed="", tournament_info=""):
        self.name = name
        self.location = location
        self.date = date
        self.duration = duration
        self.number_of_turns = number_of_turns
        self.speed = speed
        self.tournament_info = tournament_info


class Player:

    def __init__(self, last_name, first_name, date_of_birth, gender, elo):
        self.last_name = last_name
        self.first_name = first_name
        self.date_of_birth = date_of_birth
        self.gender = gender
        self.elo = elo


class Round():

    def __init__(self, name, match_1, match_2, match_3, match_4, date_of_start):
        # A round a LIST composed of 4 matchs
        self.name = name
        self.match_1 = match_1
        self.match_2 = match_2
        self.match_3 = match_3
        self.match_4 = match_4


class Match():

    def __init__(self, tplayer_1, tplayer_score_1, tplayer_2, tplayer_score_2):
        # a match a TUPLE composed of 2 tournament_player
        self.tplayer_1 = tplayer_1
        self.tplayer_2 = tplayer_2
        self.tplayer_score_1 = tplayer_score_1
        self.tplayer_score_2 = tplayer_score_2


class Tournament_player():

    def __init__(self, player):
        # a tournament player is a LIST composed of a name + score
        self.name = (player.last_name + ' ' + player.first_name)
        self.score = float(0)
        Tournament.TPLAYER_ENTRY_COUNTER + 1
