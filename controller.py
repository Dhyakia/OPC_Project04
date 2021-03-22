import model
import view as vv
from datetime import datetime


class Controller:

    def __init__(self):
        print("Welcome to torga")
        Controller.main_menu()

    def main_menu():
        start_logic = vv.View.ask_main_menu()
        # start tournament / add player / show multiples lists / save+load?
        if start_logic.lower() == "t":
            Controller.create_tournament()
        elif start_logic.lower() == "a":
            Controller.add_player()
        else:
            print("Goodbye !")

    def create_tournament():
        tournament_name = vv.View.ask_tournament_name()
        tournament_location = vv.View.ask_tournament_location()
        tournament_date = vv.View.ask_tournament_date()
        tournament_duration = vv.View.ask_tournament_duration()
        tournament_number_of_turns = vv.View.ask_tournament_number_of_turns()

        possible_speed = ["bullet", "blitz", "swift play"]
        tournament_speed = vv.View.ask_tournament_speed()
        while tournament_speed not in possible_speed:
            vv.View.speed_help()
            tournament_speed = vv.View.ask_tournament_speed()

        tournament_info = vv.View.ask_tournament_info()

        new_tournament = model.Tournament(tournament_name, tournament_location,
                                          tournament_date, tournament_duration,
                                          tournament_number_of_turns, tournament_speed,
                                          tournament_info)

        return new_tournament

        # TODO need to add 8 tournament players.
        # TODO first i need to add at least 8 player into the memory

    def add_player():
        player_last_name = vv.View.ask_player_first_name()
        player_first_name = vv.View.ask_player_last_name()
        player_date_of_birth = vv.View.ask_player_date_of_birth()
        player_gender = vv.View.ask_player_gender()
        player_elo = vv.View.ask_player_elo()
        # TODO check if elo is a float
        """
        while
            vv.View.elo_help
            player_elo = vv.View.ask_player_elo()
        """
        new_player = model.Player(player_last_name, player_first_name, player_date_of_birth,
                                  player_gender, player_elo)
        
        return print(new_player.last_name, new_player.first_name, new_player.date_of_birth,
                     new_player.gender, new_player.elo)

    def get_time():
        # get current time, used at round creation & end
        now = datetime.now()
        return now

    # Generator were done before i got it - it might be all wrong - keeping it for now
    def first_round_match_generator(tournament_player_list):
        # Because it takes elo and not score, i might need to modify the list parameter
        tplayer_list_ordered = tournament_player_list.sort(model.Player.elo, reversed=True)
        middle = len(tplayer_list_ordered)//2
        tplayer_top_players = tplayer_list_ordered[middle:]
        tplayer_bottom_players = tplayer_list_ordered[:middle]

        match_1 = tplayer_top_players[0] + tplayer_bottom_players[0]
        match_2 = tplayer_top_players[1] + tplayer_bottom_players[1]
        match_3 = tplayer_top_players[2] + tplayer_bottom_players[2]
        match_4 = tplayer_top_players[3] + tplayer_bottom_players[3]
        # add 1 to the round counter
        model.Tournament.TURN_COUNTER + 1
        return match_1, match_2, match_3, match_4

    def second_to_last_round_generator(tournament_player_list):
        list_ordered_by_score = tournament_player_list(model.Tournament_player.score, reversed=True)
        # Also need to check if players played vs each other last round
        # comparing with last round list maybe ?

        match_1 = list_ordered_by_score[0] + list_ordered_by_score[1]
        match_2 = list_ordered_by_score[2] + list_ordered_by_score[3]
        match_3 = list_ordered_by_score[4] + list_ordered_by_score[5]
        match_4 = list_ordered_by_score[6] + list_ordered_by_score[7]
        # add 1 to the round counter
        model.Tournament.ROUND_COUNTER + 1
        return match_1, match_2, match_3, match_4
