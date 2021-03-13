class Tournament:

    def __init__(self, name, location, date, duration=1, number_of_turns=4, speed='', tournament_infos=''):
        self.name = name
        print(f"Tournament's name is : {self.name}")

        self.location = location
        print(f"Tournament's location is : {self.location}")

        self.date = date
        print(f"Tournament's take place the : {self.date}")

        self.duration = duration
        print(f"Tournament will take place over {self.duration} days")

        self.number_of_turns = number_of_turns
        print(f"Their will be : {self.number_of_turns} rounds")

        self.speed = speed
        possible_speed = ["bullet", "blitz", "swift play"]
        if speed.lower() in possible_speed:
            print(f"The format is {self.speed}")
        else:
            print("Speed must be 'bullet', 'blitz' or 'swift play'")

        self.tournament_infos = tournament_infos
        print(f"Tournament's info : {self.tournament_infos}")

    def turns_list(self):
        # store turns info into a list
        pass

    def players_list(self):
        # store players info into a list
        pass


class Player:

    def __init__(self, last_name, first_name, date_of_birth, gender, elo):
        self.last_name = last_name
        self.first_name = first_name
        self.date_of_birth = date_of_birth
        self.gender = gender

        if type(elo) == int:
            if elo > 0:
                self.elo = elo
                print(self.elo)
            else:
                print('The elo must be positive')
        else:
            print('The elo must be a integer')
