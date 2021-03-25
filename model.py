class Player:

    def __init__(self, last_name, first_name, date_of_birth, gender, elo):
        self.last_name = last_name
        self.first_name = first_name
        self.date_of_birth = date_of_birth
        self.gender = gender
        self.elo = elo
        self.score = float(0)


class Tournament:

    CONSTANT_NUMBER_OF_TOURNAMENT_PLAYER = 8

    def __init__(self, name, location, date, duration=1, number_of_turns=4, speed="", tournament_info=""):
        self.name = name
        self.location = location
        self.date = date
        self.duration = duration
        self.number_of_turns = number_of_turns
        self.speed = speed
        self.tournament_info = tournament_info


class Round():

    def __init__(self, name, match_1, match_2, match_3, match_4, date_of_start):
        self.name = name
        self.match_1 = match_1
        self.match_2 = match_2
        self.match_3 = match_3
        self.match_4 = match_4


class Match():

    def __init__(self, tplayer_1, tplayer_score_1, tplayer_2, tplayer_score_2):
        self.tplayer_1 = tplayer_1
        self.tplayer_2 = tplayer_2
        self.tplayer_score_1 = tplayer_score_1
        self.tplayer_score_2 = tplayer_score_2


# "DATEBASE"
player_01 = Player('Rimonteil', 'Antoine', '1689-06-08', 'male', 1200.0)
player_02 = Player('Rimonteil', 'Thomas', '1990-06-01', 'male', 1500.0)
player_03 = Player('Bontet', 'Capucine', '2020-04-11', 'female', 800.0)
player_04 = Player('Mark', 'Marky', '1960-01-21', 'male', 2200.5)
player_05 = Player('Nguyen', 'Denis', '1993-06-18', 'male', 2500.0)
player_06 = Player('Martin', 'Isabelle', '1950.07-14', 'female', 3300.0)
player_07 = Player('Jessica', 'Laforet', '2021-02-01', 'female', 100.0)
player_08 = Player('Goyal', 'Anshul', '1970-08-15', 'male', 1800.5)

player_list = [player_01, player_02, player_03, player_04,
               player_05, player_06, player_07, player_08]

tournament_01 = Tournament("First tournament", "City's chess club", "2020-12-25", 1, 4, "blitz", "Merry Xmass")
tournament_02 = Tournament("New year opening", "City's chess club", "2021-01-08", 2, 6, "bullet", "Happy new year")

tournament_list = [tournament_01, tournament_02]
