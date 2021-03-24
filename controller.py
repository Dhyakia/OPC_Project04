import model
import view as vv
import datetime


class Controller:

    def __init__(self):
        print("Welcome to torga")
        Controller.main_menu()

    def main_menu():
        # TODO low-prio; start tournament / add player / show multiples lists / save+load?
        start_logic = vv.View.ask_main_menu()
        if start_logic.lower() == "t":
            Controller.new_tournament()
        elif start_logic.lower() == "a":
            Controller.add_player()
        else:
            print("Goodbye !")

    def new_tournament():

        Controller.get_new_tournament_data()    # TEST ; skip for testing
        # Controller.get_8_player()             # TODO ; on it
        # Generate first matchs                 # TODO
        # Enter score                           # TODO
        # Generate next to last matchs          # TODO
        # Tournament over, show end-results     # TODO

    def get_new_tournament_data():
        tournament_name = vv.View.ask_tournament_name()
        tournament_location = vv.View.ask_tournament_location()

        tournament_date = vv.View.ask_tournament_date()
        day, month, year = map(int, tournament_date.split('.'))
        tournament_date = datetime.date(year, month, day)

        tournament_duration = vv.View.ask_tournament_duration()
        tournament_number_of_turns = vv.View.ask_tournament_number_of_turns()

        possible_speed = ["bullet", "blitz", "swift play"]
        tournament_speed = vv.View.ask_tournament_speed()
        while tournament_speed not in possible_speed:
            vv.View.speed_help()
            tournament_speed = vv.View.ask_tournament_speed()

        tournament_info = vv.View.ask_tournament_info()

        new_tournament_data = model.Tournament(tournament_name, tournament_location,
                                               tournament_date, tournament_duration,
                                               tournament_number_of_turns, tournament_speed,
                                               tournament_info)

        return print(new_tournament_data)

    def get_8_player():
        # first i need to change how i get player
        pass

    def add_player():
        player_last_name = vv.View.ask_player_last_name()
        player_first_name = vv.View.ask_player_first_name()

        player_date_of_birth_data = vv.View.ask_player_date_of_birth()
        day, month, year = map(int, player_date_of_birth_data.split('.'))
        player_date_of_birth = datetime.date(year, month, day)

        player_gender = vv.View.ask_player_gender()

        player_elo = vv.View.ask_player_elo()
        while type(player_elo) is not float:  # TODO low-prio; loop never activate, crash if not float
            player_elo = vv.View.ask_player_elo()

        # new_player name varible should be = 3first letter of last name + 3first letter of first name
        new_player = model.Player(player_last_name, player_first_name, player_date_of_birth,
                                  player_gender, player_elo)

        # TODO high-prio; i think i need to use a dictionnary to get a key of the newly created player

        return new_player, Controller.main_menu()  # TODO ask-mentor; if that's the right way

    def get_time():
        now = datetime.now()
        return now
