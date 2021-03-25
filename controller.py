import model
import view as vv
import datetime


class Controller:

    def __init__(self):
        vv.View()
        self.main()

    @classmethod
    def main(cls):
        start_logic = vv.View.ask_main_menu()
        if start_logic.lower() == "t":
            cls.get_new_tournament_data()
            # cls.get_8_players()
            # Generate fist match
            # Enter score
            # Generate next to last matchs
            # Tournament over, show end results
        elif start_logic.lower() == "a":
            cls.add_player()
        else:
            vv.View.goodbye()

    @classmethod
    def get_new_tournament_data(cls):
        tournament_name = vv.View.ask_tournament_name()
        tournament_location = vv.View.ask_tournament_location()

        tournament_date = None
        while tournament_date is None:
            try:
                tournament_date_output = vv.View.ask_tournament_date()
                year, month, day = map(int, tournament_date_output.split('-'))
                tournament_date_date_format = datetime.date(year, month, day)
                tournament_date = str(tournament_date_date_format)
            except ValueError:
                vv.View.ask_tournament_date_help()
                tournament_date = None

        tournament_duration = vv.View.ask_tournament_duration()
        tournament_number_of_turns = vv.View.ask_tournament_number_of_turns()

        possible_speed = ["bullet", "blitz", "swift play"]
        tournament_speed = vv.View.ask_tournament_speed()
        while tournament_speed not in possible_speed:
            vv.View.ask_tournament_speed_help()
            tournament_speed = vv.View.ask_tournament_speed()

        tournament_info = vv.View.ask_tournament_info()

        new_tournament_data = model.Tournament(tournament_name, tournament_location, tournament_date,
                                               tournament_duration, tournament_number_of_turns, tournament_speed,
                                               tournament_info)

        model.tournament_list.append(new_tournament_data)

    @classmethod
    def get_8_players(cls):
        # ask user wich player to enter into the tournament [last_name + " " + first_name]
        # search the list for the player in question
        # in a while loop, using the constant in tournament(8) to loop:
        # if player exist = add him into the list and continue until 8 player
        # else, either the player doesn't exist or typo, warn user
        pass

    @classmethod
    def add_player(cls):
        player_last_name = vv.View.ask_player_last_name()
        player_first_name = vv.View.ask_player_first_name()

        player_date_of_birth = None
        while player_date_of_birth is None:
            try:
                player_date_of_birth_output = vv.View.ask_player_date_of_birth()
                year, month, day = map(int, player_date_of_birth_output.split('-'))
                player_date_of_birth_date_format = datetime.date(year, month, day)
                player_date_of_birth = str(player_date_of_birth_date_format)
            except ValueError:
                vv.View.ask_player_date_of_birth_help()
                player_date_of_birth = None

        player_gender = vv.View.ask_player_gender()

        player_elo = None
        while player_elo is None:
            try:
                player_elo_output = vv.View.ask_player_elo()
                player_elo = float(player_elo_output)
            except (ValueError, TypeError):
                vv.View.ask_player_elo_help()
                player_elo = None

        new_player = model.Player(player_last_name, player_first_name, player_date_of_birth,
                                  player_gender, player_elo)

        model.player_list.append(new_player)
        cls.main()

    @staticmethod
    def get_time():
        # TODO; will have to check if that's the right way
        now = datetime.now()
        return now
