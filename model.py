class Tournament:

    CONSTANT_NUMBER_OF_TOURNAMENT_PLAYER = 8

    def __init__(self, name, location, date, duration=int(1), number_of_turns=4, speed="", tournament_info=""):
        # explicit
        self.name = name
        self.location = location
        self.date = date
        self.duration = duration
        self.number_of_turns = int(number_of_turns)
        if not number_of_turns:
            number_of_turns = 4
        self.speed = speed
        self.tournament_info = tournament_info
        # implicit
        self.players_list = []
        self.rounds_list = []


class Player:

    def __init__(self, last_name, first_name, date_of_birth, gender, elo):
        # explicit
        self.last_name = last_name
        self.first_name = first_name
        self.date_of_birth = date_of_birth
        self.gender = gender
        self.elo = elo
        # implicit
        self.score = float(0)
        self.last_played = ""


# "DATEBASE" until TinyDB is setup
player_01 = Player('Rimonteil', 'Antoine', '1689-06-08', 'male', 1200.0)
player_02 = Player('Rimonteil', 'Thomas', '1990-06-01', 'male', 1500.0)
player_03 = Player('Bontet', 'Capucine', '2020-04-11', 'female', 800.0)
player_04 = Player('Mark', 'Marky', '1960-01-21', 'male', 2200.5)
player_05 = Player('Nguyen', 'Denis', '1993-06-18', 'male', 2500.0)
player_06 = Player('Martin', 'Isabelle', '1950.07-14', 'female', 3300.0)
player_07 = Player('Laforet', 'Jessica', '2021-02-01', 'female', 100.0)
player_08 = Player('Goyal', 'Anshul', '1970-08-15', 'male', 1800.5)

players_list = [player_01, player_02, player_03, player_04,
                player_05, player_06, player_07, player_08]

tournament_01 = Tournament("First tournament", "City's chess club", "2020-12-25", 1, 4, "blitz", "Merry Xmass")
tournament_02 = Tournament("New year opening", "City's chess club", "2021-01-08", 2, 6, "bullet", "Happy new year")
tournament_03 = Tournament("Easter special", "City's chess club", "2021-04-01", 1, 4, "blitz", "Free pizza")

tournaments_list = [tournament_01, tournament_02, tournament_03]

tournament_03.players_list = [player_01, player_02, player_03, player_04, player_05, player_06, player_07, player_08]

tournament_03.players_list[0].score = 4
tournament_03.players_list[1].score = 3.5
tournament_03.players_list[2].score = 2
tournament_03.players_list[3].score = 0
tournament_03.players_list[4].score = 0.5
tournament_03.players_list[5].score = 2.5
tournament_03.players_list[6].score = 2.5
tournament_03.players_list[7].score = 1
