class Tournament:

    NUMBER_OF_TOURNAMENT_PLAYER = []

    def __init__(self, name, location, date, duration=1, number_of_turns=4, speed='', tournament_infos=''):
        self.name = name
        self.location = location
        self.date = date
        self.duration = duration
        self.number_of_turns = number_of_turns

        possible_speed = ["bullet", "blitz", "swift play"]
        if speed.lower() in possible_speed:
            self.speed = speed
        else:
            # It works but CRASH the program if input is incorrect
            raise Exception("Speed param must be 'bullet', 'blitz' or 'swift play'")

    # List of all the rounds

    # List of players in the tournament


class Player:

    def __init__(self, last_name, first_name, date_of_birth, gender, elo):
        self.last_name = last_name
        self.first_name = first_name
        self.date_of_birth = date_of_birth
        self.gender = gender

        if type(elo) == float:
            if elo > 0:
                self.elo = elo
            else:
                # Same problem as other Execption -> it crash the program incase of error
                raise Exception('The elo must be positive')
        else:
            raise Exception('The elo must be a number')


class Tournament_player():

    def __init__(self, player):
        self.name = (player.last_name + ' ' + player.first_name)
        self.score = float(0)


class Rounds():

    def __init__():
        pass


# "database" for testing until TinyDB is setup
"""
player_01 = Player("Rimonteil", "Antoine", "01.08.1889", "Male", 1200.0)
player_02 = Player("Rakkas", "Thomas", "06.12.1983", "Male", 1500.0)
player_03 = Player("Martin", "Isabelle", "21.08.1783", "Female", 800.5)
player_04 = Player("Nguyen", "Denis", "11.10.1990", "Male", 800.0)
player_05 = Player("Bontet", "Capucine", "07.07.1907", "Female", 2250.0)
player_06 = Player("Lacroix", "Camille", "14.02.1405", "Female", 3300.5)
player_07 = Player("Kapela", "Kevin", "05.08.2001", "Male", 720.5)
player_08 = Player("Mark", "Marky", "28.03.2010", "Male", 440.5)

tplayer_01 = Tournament_player(player_08)
tplayer_02 = Tournament_player(player_08)
tplayer_03 = Tournament_player(player_08)
tplayer_04 = Tournament_player(player_08)
tplayer_05 = Tournament_player(player_08)
tplayer_06 = Tournament_player(player_08)
tplayer_07 = Tournament_player(player_08)
tplayer_08 = Tournament_player(player_08)

test_tournament = Tournament(name="Tiny Chess Tournament", location="City's chess club", date="24.06.2022",
                             duration=1, number_of_turns=4, speed="blitz",
                             tournament_infos="Veteran & new player are welcome")
"""
