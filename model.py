class Tournament:

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
            print("Speed must be 'bullet', 'blitz' or 'swift play'")

        self.tournament_infos = tournament_infos

        # Rounds - List that store the info at the end of the round

        # Tournament players - List that store the info of players in the tournament


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
                print('The elo must be positive')
        else:
            print('The elo must be a number')


class Tournament_player:

    def __init__(self, Player):
        self.name = (Player.first_name + ' ' + Player.last_name)
        self.score = float(0)

    def Win():
        #

    def Loose():
        #

    def Draw():
        #
