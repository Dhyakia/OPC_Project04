import model
import view as vv
import datetime


class Controller:

    def __init__(self):
        vv.View()
        self.main()

    def main(self):
        start_logic = vv.View.ask_main_menu()
        flow = True
        while flow is True:

            if start_logic.lower() == "t":
                resume_or_start = vv.View.ask_resume_or_start()

                if resume_or_start.lower() == "r":
                    # TODO resume a saved tournament
                    # ask for player or tournament info
                    pass

                elif resume_or_start.lower() == "n":
                    self.get_new_tournament_data()
                    print(type(model.tournaments_list[-1].number_of_turns))
                    self.get_8_players()
                    self.first_round_generator()
                    self.enter_score()                    
                    # if left empty (default), SOMETIMES (~half the time) i get this error
                    # "ValueError invalid literal for int with base 10 error in Python"
                    # TODO rematch are still not done
                    # TODO save the program at any time

                    number_of_rounds = model.tournaments_list[-1].number_of_turns
                    number_of_loop = number_of_rounds - 1
                    for rounds in range(number_of_loop):
                        self.second_to_last_round_generator(rounds)
                        self.enter_score()
                    self.end_of_tournament_table()

            elif start_logic.lower() == "a":
                self.add_player()

            elif start_logic.lower() == "d":
                user_view = vv.View.ask_player_or_tournament()
                self.show_data_list(user_view)

            elif start_logic.lower() == "x":
                vv.View.goodbye()
                flow = False

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
        # TODO string vide donc None et pas vide !
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
                    model.players_list[index].score = float(0)
                    model.players_list[index].last_played = str('')
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

    def show_data_list(self, user_view):

        if user_view.lower() == "p":
            alpha_or_rank = vv.View.ask_alpha_or_rank()
            self.show_all_players(alpha_or_rank)

        elif user_view.lower() == "t":
            self.show_all_tournaments_table()

        elif len(user_view) > 2:
            self.show_data_inside_tournament(user_view)

        else:
            return

    def show_all_tournaments_table(self):
        table = []
        for tournament in model.tournaments_list:
            name = tournament.name
            location = tournament.location
            date = tournament.date
            duration = tournament.duration
            number_of_turns = tournament.number_of_turns
            speed = tournament.speed
            info = tournament.tournament_info

            tournament_data = [name, location, date, duration, number_of_turns, speed, info]
            table.append(tournament_data)

        vv.View.all_tournaments_table(table)

    def show_all_players(self, alpha_or_rank):
        user_input = alpha_or_rank
        table = []

        for player in model.players_list:
            last_name = player.last_name
            first_name = player.first_name
            date_of_birth = player.date_of_birth
            gender = player.gender
            elo = player.elo

            player_data = [last_name, first_name, date_of_birth, gender, elo]
            table.append(player_data)

        if user_input.lower() == 'a':
            all_player_sorted_by_alpha = sorted(table, key=lambda x: x[0])
            vv.View.all_player_table(all_player_sorted_by_alpha)

        elif user_input.lower() == 'r':
            all_player_sorted_by_rank = sorted(table, key=lambda x: x[4], reverse=True)
            vv.View.all_player_table(all_player_sorted_by_rank)

    def show_data_inside_tournament(self, user_view):
        data = user_view
        rounds = data.find(" -r")
        matchs = data.find(" -m")
        players = data.find(" -p")

        # if any of them are equal or more than 0, that mean it's in there
        if rounds >= 0:
            tournament_target = data.replace(' -r', '')
            for index, name in enumerate(model.tournaments_list):
                if name.name == tournament_target:
                    model.tournaments_list[index].rounds_list
                    # TODO; Show all rounds with name, start date & end date

        elif matchs >= 0:
            tournament_target = data.replace(' -m', '')
            for index, name in enumerate(model.tournaments_list):
                if name.name == tournament_target:
                    model.tournaments_list[index]
                    # TODO; Target ALL 4 match for EVERY round, then print the match-up (X vs Y)

        elif players >= 0:
            tournament_target = data.replace(' -p', '')
            for index, name in enumerate(model.tournaments_list):
                if name.name == tournament_target:
                    model.tournaments_list[index]
                    # TODO; fetch the players list + ask for alpha or rank + show

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
