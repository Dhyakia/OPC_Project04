class Tournament:

    number_of_tournament_player = []

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
                # Same problem as other Execption -> it crash the program
                raise Exception('The elo must be positive')
        else:
            raise Exception('The elo must be a number')
