class Tournament:

    def __init__(self, name, location, date, duration=1, number_of_turns=4):
        self.name = name
        self.location = location
        # can go over 1 day, think about it
        self.date = date
        self.duration = duration
        self.number_of_turns = number_of_turns

    def tournament_rounds(self, t_round_info):
        # List that store the info of each round (1 round = 4 matchs)
        self.t_round_info = []

    def tournament_players(self, t_player_info):
        # List that store the info of all 8 players in the tournment; player tuple = (name + score)
        self.t_player_info = t_player_info

    def matchs_speed(self, speed):
        valid_speed = {"bullet", "blitz", "swift"}
        if speed not in valid_speed:
            raise ValueError("results: speed must be bullet, blitz or swift")

    def description(self, to_notes):
        if isinstance(to_notes, (str)):
            self.to_notes = to_notes
        # need an ELSE here


class Player:

    def __init__(self, last_name, first_name, date_of_birth, gender):
        self.last_name = last_name
        self.first_name = first_name
        self.date_of_birth = date_of_birth
        self.gender = gender

    def rank(self, rank):
        if isinstance(rank, int):
            self.rank = rank
        # need an ELSE here too
