class Tournament:

    def __init__(self, name, location, date, duration=1, number_of_turns=4):
        self.name = name
        self.location = location
        self.date = date
        # can go over 1 day, think about it
        self.duration = duration
        self.number_of_turns = number_of_turns

    def tournament_rounds(self, t_round_info):
        # List that store the info of each round (1 round = 4 matchs)
        self.t_round_info = []

    def tournament_players(self, t_player_info):
        # List that store the info of all 8 players in the tournament
        self.t_player_info = []

    def matchs_speed(self, speed):
        valid_speed = {"bullet", "blitz", "swift"}
        if speed not in valid_speed:
            raise ValueError("results: speed must be bullet, blitz or swift")

    def description(self, to_notes):
        self.to_notes = to_notes


class Player:

    def __init__(self, last_name, first_name, date_of_birth, gender):
        self.last_name = last_name
        self.first_name = first_name
        self.date_of_birth = date_of_birth
        self.gender = gender

    def rank(self, rank):
        if isinstance(rank, int):
            self.rank = rank
        else:
            print("A rank must be an integer")


class Round:

    def __init__(self, match_list):
        # a round is a list of matchs
        self.match_list = []


class Match:

    def __init__(self, tplayer1, tplayer2, tscore1, tscore2):
        match_results = ([self.tplayer1, self.score1], [self.tplayer2, self.tscore2])
        return match_results
