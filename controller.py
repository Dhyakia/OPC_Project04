import model
import view as vv
import datetime


class Controller:

    def __init__(self):
        vv.View()
        self.main()

    def main(self):
        start_logic = vv.View.ask_main_menu()
        if start_logic.lower() == "x":
            vv.View.goodbye()

        elif start_logic.lower() == "a":
            self.add_player()

        elif start_logic.lower() == "t":
            self.get_new_tournament_data()
            self.get_8_players()
            self.first_round_generator()
            self.enter_score()

            # if left empty (default), SOMETIMES (~half the time) i get this error
            # "ValueError invalid literal for int with base 10 error in Python"

            number_of_rounds = model.tournaments_list[-1].number_of_turns
            number_of_loop = (int(number_of_rounds) - 1)
            for rounds in range(int(number_of_loop)):
                self.second_to_last_round_generator(rounds)
                self.enter_score()
            self.end_of_tournament_table()

    def get_new_tournament_data(self):
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

        possible_speed = ["bullet", "blitz", "rapid"]
        tournament_speed = vv.View.ask_tournament_speed()
        while tournament_speed.lower() not in possible_speed:
            vv.View.ask_tournament_speed_help()
            tournament_speed = vv.View.ask_tournament_speed()

        tournament_info = vv.View.ask_tournament_info()

        new_tournament_data = model.Tournament(tournament_name, tournament_location, tournament_date,
                                               tournament_duration, tournament_number_of_turns, tournament_speed,
                                               tournament_info)

        model.tournaments_list.append(new_tournament_data)

    def get_8_players(self):
        while len(model.tournaments_list[-1].players_list) < model.Tournament.CONSTANT_NUMBER_OF_TOURNAMENT_PLAYER:
            player_entering_tournament = vv.View.ask_player_full_name()
            player_last_name, player_first_name = player_entering_tournament.split(" ")
            error_message_counter = []
            for index, name in enumerate(model.players_list):
                if name.last_name == player_last_name and name.first_name == player_first_name:
                    model.tournaments_list[-1].players_list.append(model.players_list[index])
                    vv.View.player_has_been_added(player_entering_tournament)
                else:
                    error_message_counter.append("x")
                    if len(error_message_counter) == len(model.players_list):
                        vv.View.player_has_been_added_help(player_entering_tournament)
                    else:
                        pass

        vv.View.tournament_can_start()

    def first_round_generator(self):
        vv.View.generating_first_turn_matchs()
        players_list_by_elo = sorted(model.tournaments_list[-1].players_list, key=lambda x: x.elo, reverse=True)

        middle = len(players_list_by_elo)//2
        top_half_players = players_list_by_elo[:middle]
        bottom_half_players = players_list_by_elo[middle:]

        match_01 = top_half_players[0], bottom_half_players[0]
        match_02 = top_half_players[1], bottom_half_players[1]
        match_03 = top_half_players[2], bottom_half_players[2]
        match_04 = top_half_players[3], bottom_half_players[3]
        round_name = 'Round 1'
        start_time = self.get_time()

        round = [match_01, match_02, match_03, match_04, round_name, start_time]
        model.tournaments_list[-1].rounds_list.append(round)

        vv.View.round_1_annoucement(start_time)
        vv.View.show_user_matchup(match_01, match_02, match_03, match_04)

    def second_to_last_round_generator(self, rounds):
        vv.View.generating_matchs()
        rounds_count = (rounds + 2)

        players_list_by_score = sorted(model.tournaments_list[-1].players_list, key=lambda x: x.score, reverse=True)

        match_01 = players_list_by_score[0], players_list_by_score[1]
        match_02 = players_list_by_score[2], players_list_by_score[3]
        match_03 = players_list_by_score[4], players_list_by_score[5]
        match_04 = players_list_by_score[6], players_list_by_score[7]
        round_name = str(f'Round {rounds_count}')
        start_time = self.get_time()

        # TODO; if the player n°1 already played vs the n°2, then play vs n°3

        round = [match_01, match_02, match_03, match_04, round_name, start_time]
        model.tournaments_list[-1].rounds_list.append(round)

        vv.View.round_second_to_last_annoucement(rounds_count, start_time)
        vv.View.show_user_matchup(match_01, match_02, match_03, match_04)

    def enter_score(self):
        vv.View.enter_score_instructions()
        match_count = 0

        while match_count < 4:
            match_result = vv.View.ask_user_match_result((match_count + 1))
            if match_result == "0":
                player_1_last_name = model.tournaments_list[-1].rounds_list[-1][match_count][0].last_name
                player_1_first_name = model.tournaments_list[-1].rounds_list[-1][match_count][0].first_name
                player_2_last_name = model.tournaments_list[-1].rounds_list[-1][match_count][1].last_name
                player_2_first_name = model.tournaments_list[-1].rounds_list[-1][match_count][1].first_name
                for index, name in enumerate(model.tournaments_list[-1].players_list):
                    if name.last_name == player_1_last_name and name.first_name == player_1_first_name:
                        model.tournaments_list[-1].players_list[index].score += 0.5
                    elif name.last_name == player_2_last_name and name.first_name == player_2_first_name:
                        model.tournaments_list[-1].players_list[index].score += 0.5
                        match_count += 1
                        vv.View.draw(match_count)

            elif match_result == "1":
                last_name = model.tournaments_list[-1].rounds_list[-1][match_count][0].last_name
                first_name = model.tournaments_list[-1].rounds_list[-1][match_count][0].first_name
                for index, name in enumerate(model.tournaments_list[-1].players_list):
                    if name.last_name == last_name and name.first_name == first_name:
                        model.tournaments_list[-1].players_list[index].score += 1
                        match_count += 1
                        vv.View.a_player_won(model.tournaments_list[-1].players_list[index].first_name,
                                             model.tournaments_list[-1].players_list[index].last_name)

            elif match_result == "2":
                last_name = model.tournaments_list[-1].rounds_list[-1][match_count][1].last_name
                first_name = model.tournaments_list[-1].rounds_list[-1][match_count][1].first_name
                for index, name in enumerate(model.tournaments_list[-1].players_list):
                    if name.last_name == last_name and name.first_name == first_name:
                        model.tournaments_list[-1].players_list[index].score += 1
                        match_count += 1
                        vv.View.a_player_won(model.tournaments_list[-1].players_list[index].first_name,
                                             model.tournaments_list[-1].players_list[index].last_name)
            else:
                vv.View.enter_score_instructions_help()

        end_time = self.get_time()
        model.tournaments_list[-1].rounds_list[-1].append(end_time)
        vv.View.end_of_round_time(end_time)

    def end_of_tournament_table(self):
        tplayer_1 = [model.tournaments_list[-1].players_list[0].first_name,
                     model.tournaments_list[-1].players_list[0].last_name,
                     model.tournaments_list[-1].players_list[0].score]

        tplayer_2 = [model.tournaments_list[-1].players_list[1].first_name,
                     model.tournaments_list[-1].players_list[1].last_name,
                     model.tournaments_list[-1].players_list[1].score]

        tplayer_3 = [model.tournaments_list[-1].players_list[2].first_name,
                     model.tournaments_list[-1].players_list[2].last_name,
                     model.tournaments_list[-1].players_list[2].score]

        tplayer_4 = [model.tournaments_list[-1].players_list[3].first_name,
                     model.tournaments_list[-1].players_list[3].last_name,
                     model.tournaments_list[-1].players_list[3].score]

        tplayer_5 = [model.tournaments_list[-1].players_list[4].first_name,
                     model.tournaments_list[-1].players_list[4].last_name,
                     model.tournaments_list[-1].players_list[4].score]

        tplayer_6 = [model.tournaments_list[-1].players_list[5].first_name,
                     model.tournaments_list[-1].players_list[5].last_name,
                     model.tournaments_list[-1].players_list[5].score]

        tplayer_7 = [model.tournaments_list[-1].players_list[6].first_name,
                     model.tournaments_list[-1].players_list[6].last_name,
                     model.tournaments_list[-1].players_list[6].score]

        tplayer_8 = [model.tournaments_list[-1].players_list[7].first_name,
                     model.tournaments_list[-1].players_list[7].last_name,
                     model.tournaments_list[-1].players_list[7].score]

        table = [tplayer_1, tplayer_2, tplayer_3, tplayer_4, tplayer_5, tplayer_6, tplayer_7, tplayer_8]

        vv.View.tournament_player_table(table)

    def add_player(self):
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

        model.players_list.append(new_player)
        self.main()

    @staticmethod
    def get_time():
        now = datetime.datetime.now()
        full_now = now.strftime("%d/%m/%Y %H:%M:%S")
        return full_now
