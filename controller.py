import model
import view
import datetime


class Controller:

    def __init__(self):
        self.view = view.View()
        self.main()

    def main(self):
        flow = True
        while flow is True:
            start_logic = self.view.ask_main_menu()

            players_list = model.Player.database_to_players_list(model.players_table.all())
            tournaments_list = model.Tournament.database_to_tournaments_list(model.tournaments_table.all())
            saved_game = model.Tournament.saved_tournament_to_memory(model.save_table)

            if start_logic.lower() == "t":
                resume_or_start = self.view.ask_resume_or_start()
                self.tournament_logic(resume_or_start, players_list, tournaments_list, saved_game)

            elif start_logic.lower() == "a":
                self.add_player(players_list)

            elif start_logic.lower() == "d":
                user_view = self.view.ask_player_or_tournament()
                self.show_data_list(user_view, players_list, tournaments_list)

            elif start_logic.lower() == "x":
                self.view.goodbye()
                flow = False

    def tournament_logic(self, user_input, players_list, tournaments_list, saved_game):
        # TODO A chauque fin de round, le tournois doit effectuer une sauvegarde automatiquement
        if user_input.lower() == "r":
            self.view.show_user_loading(saved_game.name)

            # TODO Set ici le self.tournament = saved_game (???)
            tournaments_list.append(saved_game)
            self.view.show_user_loading_successful(tournaments_list[-1].name)

            self.view.show_all_matchs(
                tournaments_list[-1].rounds_list[-1][4], tournaments_list[-1].rounds_list[-1][0],
                tournaments_list[-1].rounds_list[-1][1], tournaments_list[-1].rounds_list[-1][2],
                tournaments_list[-1].rounds_list[-1][3])
            self.enter_score(tournaments_list)

            loop = len(tournaments_list[-1].rounds_list)
            number_of_rounds = tournaments_list[-1].number_of_turns
            for rounds in range(number_of_rounds):
                if rounds <= loop:
                    pass
                else:
                    self.second_to_last_round_generator_resumed_games(rounds, tournaments_list)
                    self.enter_score(tournaments_list)
            self.end_of_tournament_table(tournaments_list)
            self.tournament_to_database(tournaments_list[-1])

        elif user_input.lower() == "n":
            # TODO get_new_tournament_data ne prend plus un liste en argument (pas sur)
            new_tournament_data = self.get_new_tournament_data()
            tournaments_list.append(new_tournament_data)
            self.get_8_players(players_list, tournaments_list)
            self.first_round_generator(tournaments_list)
            self.enter_score(tournaments_list)

            number_of_rounds = int(tournaments_list[-1].number_of_turns)
            number_of_loop = number_of_rounds - 1
            for rounds in range(number_of_loop):
                self.second_to_last_round_generator(rounds, tournaments_list)
                self.enter_score(tournaments_list)
            self.end_of_tournament_table(tournaments_list)
            self.tournament_to_database(tournaments_list[-1])

        else:
            return None

    def get_new_tournament_data(self):
        tournament_name = self.view.ask_tournament_name()
        tournament_location = self.view.ask_tournament_location()

        tournament_date = None
        while tournament_date is None:
            try:
                tournament_date_output = self.view.ask_tournament_date()
                year, month, day = map(int, tournament_date_output.split('-'))
                tournament_date_date_format = datetime.date(year, month, day)
                tournament_date = str(tournament_date_date_format)
            except ValueError:
                self.view.ask_tournament_date_help()
                tournament_date = None

        tournament_duration = self.view.ask_tournament_duration()
        if tournament_duration == '':
            tournament_duration = 1

        tournament_number_of_turns = self.view.ask_tournament_number_of_turns()
        if tournament_number_of_turns == '':
            tournament_number_of_turns = 4

        possible_speed = ["bullet", "blitz", "rapid"]
        tournament_speed = self.view.ask_tournament_speed()
        while tournament_speed.lower() not in possible_speed:
            self.view.ask_tournament_speed_help()
            tournament_speed = self.view.ask_tournament_speed()
        tournament_info = self.view.ask_tournament_info()

        new_tournamment = model.Tournament(tournament_name, tournament_location, tournament_date,
                                           tournament_duration, tournament_number_of_turns, tournament_speed,
                                           tournament_info, [], [])
        return new_tournamment

    def get_8_players(self, players_list, tournaments_list):
        while len(tournaments_list[-1].tournament_players_list) < model.Tournament.NUMBER_OF_TOURNAMENT_PLAYER:
            try:
                player_entering_tournament = self.view.ask_player_full_name()
                player_last_name, player_first_name = player_entering_tournament.split(" ")
                error_message_counter = []
                for index, name in enumerate(players_list):
                    if name.last_name == player_last_name and name.first_name == player_first_name:
                        players_list[index].score = float(0)
                        players_list[index].last_played = str('')
                        tournaments_list[-1].tournament_players_list.append(players_list[index])
                        self.view.player_has_been_added(player_entering_tournament)
                    else:
                        error_message_counter.append("x")
                        if len(error_message_counter) == len(players_list):
                            self.view.player_has_been_added_help(player_entering_tournament)
                        else:
                            pass
            except ValueError:
                self.view.show_user_right_name_input()

        self.view.tournament_can_start()

    def first_round_generator(self, tournaments_list):
        self.view.generating_first_turn_matchs()
        players_list_by_elo = sorted(tournaments_list[-1].tournament_players_list,
                                     key=lambda x: x.elo, reverse=True)

        middle = len(players_list_by_elo) // 2
        top_half_players = players_list_by_elo[:middle]
        bottom_half_players = players_list_by_elo[middle:]

        match_01 = model.Match(top_half_players[0], bottom_half_players[0])
        match_02 = model.Match(top_half_players[1], bottom_half_players[1])
        match_03 = model.Match(top_half_players[2], bottom_half_players[2])
        match_04 = model.Match(top_half_players[3], bottom_half_players[3])

        top_half_players[0].last_played = bottom_half_players[0].last_name + ' ' + bottom_half_players[0].first_name
        top_half_players[1].last_played = bottom_half_players[1].last_name + ' ' + bottom_half_players[1].first_name
        top_half_players[2].last_played = bottom_half_players[2].last_name + ' ' + bottom_half_players[2].first_name
        top_half_players[3].last_played = bottom_half_players[3].last_name + ' ' + bottom_half_players[3].first_name
        bottom_half_players[0].last_played = top_half_players[0].last_name + ' ' + top_half_players[0].first_name
        bottom_half_players[1].last_played = top_half_players[1].last_name + ' ' + top_half_players[1].first_name
        bottom_half_players[2].last_played = top_half_players[2].last_name + ' ' + top_half_players[2].first_name
        bottom_half_players[3].last_played = top_half_players[3].last_name + ' ' + top_half_players[3].first_name

        round_name = 'Round 1'
        start_time = self.get_time()
        round = [match_01, match_02, match_03, match_04, round_name, start_time]
        tournaments_list[-1].rounds_list.append(round)

        self.view.round_1_annoucement(start_time)
        self.view.show_user_matchup(match_01, match_02, match_03, match_04)

    def second_to_last_round_generator(self, rounds, tournaments_list):
        self.view.generating_matchs()
        rounds_count = (rounds + 2)

        players_list_by_score = sorted(tournaments_list[-1].tournament_players_list,
                                       key=lambda x: x.score, reverse=True)
        round = []
        index = 1
        while len(players_list_by_score) != 0:
            last_name = players_list_by_score[index].last_name
            first_name = players_list_by_score[index].first_name
            full_name = (last_name + ' ' + first_name)

            if players_list_by_score[0].last_played == full_name:
                match = (players_list_by_score[0], players_list_by_score[index + 1])

                del players_list_by_score[index + 1]
                del players_list_by_score[0]
                round.append(match)

            if players_list_by_score[0].last_played != full_name:
                match = (players_list_by_score[0], players_list_by_score[index])

                del players_list_by_score[index]
                del players_list_by_score[0]
                round.append(match)

        round_name = str(f'Round {rounds_count}')
        start_time = self.get_time()
        round.append(round_name)
        round.append(start_time)

        tournaments_list[-1].rounds_list.append(round)

        self.view.round_second_to_last_annoucement(rounds_count, start_time)
        self.view.show_user_matchup(round[0], round[1], round[2], round[3])

    def second_to_last_round_generator_resumed_games(self, rounds, tournaments_list):
        self.view.generating_matchs()
        rounds_count = int(rounds)

        players_list_by_score = sorted(tournaments_list[-1].tournament_players_list,
                                       key=lambda x: x.score, reverse=True)
        round = []
        index = 1
        while len(players_list_by_score) != 0:
            last_name = players_list_by_score[index].last_name
            first_name = players_list_by_score[index].first_name
            full_name = (last_name + ' ' + first_name)

            if players_list_by_score[0].last_played == full_name:
                match = (players_list_by_score[0], players_list_by_score[index + 1])

                del players_list_by_score[index + 1]
                del players_list_by_score[0]
                round.append(match)

            if players_list_by_score[0].last_played != full_name:
                match = (players_list_by_score[0], players_list_by_score[index])

                del players_list_by_score[index]
                del players_list_by_score[0]
                round.append(match)

        round_name = str(f'Round {rounds_count}')
        start_time = self.get_time()
        round.append(round_name)
        round.append(start_time)

        tournaments_list[-1].rounds_list.append(round)

        self.view.round_second_to_last_annoucement(rounds_count, start_time)
        self.view.show_user_matchup(round[0], round[1], round[2], round[3])

    def enter_score(self, tournaments_list):
        self.view.enter_score_instructions()
        match_count = 0

        while match_count < 4:
            match_result = self.view.ask_user_match_result((match_count + 1))
            if match_result == "0":
                player_1_last_name = tournaments_list[-1].rounds_list[-1][match_count][0].last_name
                player_1_first_name = tournaments_list[-1].rounds_list[-1][match_count][0].first_name
                player_2_last_name = tournaments_list[-1].rounds_list[-1][match_count][1].last_name
                player_2_first_name = tournaments_list[-1].rounds_list[-1][match_count][1].first_name
                for index, name in enumerate(tournaments_list[-1].tournament_players_list):
                    if name.last_name == player_1_last_name and name.first_name == player_1_first_name:
                        tournaments_list[-1].tournament_players_list[index].score += 0.5
                    elif name.last_name == player_2_last_name and name.first_name == player_2_first_name:
                        tournaments_list[-1].tournament_players_list[index].score += 0.5
                        match_count += 1
                        self.view.draw(match_count)

            elif match_result == "1":
                last_name = tournaments_list[-1].rounds_list[-1][match_count][0].last_name
                first_name = tournaments_list[-1].rounds_list[-1][match_count][0].first_name
                for index, name in enumerate(tournaments_list[-1].tournament_players_list):
                    if name.last_name == last_name and name.first_name == first_name:
                        tournaments_list[-1].tournament_players_list[index].score += 1
                        match_count += 1
                        self.view.a_player_won(tournaments_list[-1].tournament_players_list[index].first_name,
                                               tournaments_list[-1].tournament_players_list[index].last_name)

            elif match_result == "2":
                last_name = tournaments_list[-1].rounds_list[-1][match_count][1].last_name
                first_name = tournaments_list[-1].rounds_list[-1][match_count][1].first_name
                for index, name in enumerate(tournaments_list[-1].tournament_players_list):
                    if name.last_name == last_name and name.first_name == first_name:
                        tournaments_list[-1].tournament_players_list[index].score += 1
                        match_count += 1
                        self.view.a_player_won(tournaments_list[-1].tournament_players_list[index].first_name,
                                               tournaments_list[-1].tournament_players_list[index].last_name)

            elif match_result.lower() == "save":
                model.save_table.truncate()
                self.tournament_to_database_save(tournaments_list[-1])
                self.view.tournament_is_saved(tournaments_list[-1].name)
                self.view.goodbye()
                exit()

            else:
                self.view.enter_score_instructions_help()

        end_time = self.get_time()
        tournaments_list[-1].rounds_list[-1].append(end_time)
        self.view.end_of_round_time(end_time)

    def end_of_tournament_table(self, tournaments_list):
        tplayer_1 = [tournaments_list[-1].tournament_players_list[0].first_name,
                     tournaments_list[-1].tournament_players_list[0].last_name,
                     tournaments_list[-1].tournament_players_list[0].score]

        tplayer_2 = [tournaments_list[-1].tournament_players_list[1].first_name,
                     tournaments_list[-1].tournament_players_list[1].last_name,
                     tournaments_list[-1].tournament_players_list[1].score]

        tplayer_3 = [tournaments_list[-1].tournament_players_list[2].first_name,
                     tournaments_list[-1].tournament_players_list[2].last_name,
                     tournaments_list[-1].tournament_players_list[2].score]

        tplayer_4 = [tournaments_list[-1].tournament_players_list[3].first_name,
                     tournaments_list[-1].tournament_players_list[3].last_name,
                     tournaments_list[-1].tournament_players_list[3].score]

        tplayer_5 = [tournaments_list[-1].tournament_players_list[4].first_name,
                     tournaments_list[-1].tournament_players_list[4].last_name,
                     tournaments_list[-1].tournament_players_list[4].score]

        tplayer_6 = [tournaments_list[-1].tournament_players_list[5].first_name,
                     tournaments_list[-1].tournament_players_list[5].last_name,
                     tournaments_list[-1].tournament_players_list[5].score]

        tplayer_7 = [tournaments_list[-1].tournament_players_list[6].first_name,
                     tournaments_list[-1].tournament_players_list[6].last_name,
                     tournaments_list[-1].tournament_players_list[6].score]

        tplayer_8 = [tournaments_list[-1].tournament_players_list[7].first_name,
                     tournaments_list[-1].tournament_players_list[7].last_name,
                     tournaments_list[-1].tournament_players_list[7].score]

        table = [tplayer_1, tplayer_2, tplayer_3, tplayer_4, tplayer_5, tplayer_6, tplayer_7, tplayer_8]

        self.view.tournament_player_table(table)
        return None

    def add_player(self, players_list):
        player_last_name = self.view.ask_player_last_name()
        player_first_name = self.view.ask_player_first_name()

        player_date_of_birth = None
        while player_date_of_birth is None:
            try:
                player_date_of_birth_output = self.view.ask_player_date_of_birth()
                year, month, day = map(int, player_date_of_birth_output.split('-'))
                player_date_of_birth_date_format = datetime.date(year, month, day)
                player_date_of_birth = str(player_date_of_birth_date_format)
            except ValueError:
                self.view.ask_player_date_of_birth_help()
                player_date_of_birth = None

        player_gender = self.view.ask_player_gender()

        player_elo = None
        while player_elo is None:
            try:
                player_elo_output = self.view.ask_player_elo()
                player_elo = float(player_elo_output)
            except (ValueError, TypeError):
                self.view.ask_player_elo_help()
                player_elo = None

        new_player = model.Player(player_last_name, player_first_name, player_date_of_birth,
                                  player_gender, player_elo)

        players_list.append(new_player)
        new_player.player_to_database()
        return None

    def show_data_list(self, user_view, players_list, tournaments_list):

        if user_view.lower() == "p":
            alpha_or_rank = self.view.ask_alpha_or_rank()
            self.show_all_players(alpha_or_rank, players_list)

        elif user_view.lower() == "t":
            self.show_all_tournaments_table(tournaments_list)

        elif len(user_view) > 2:
            self.show_data_inside_tournament(user_view, tournaments_list)

        elif user_view.lower() == "m":
            pass

    def show_all_tournaments_table(self, tournaments_list):
        table = []
        for tournament in tournaments_list:
            name = tournament.name
            location = tournament.location
            date = tournament.date
            duration = tournament.duration
            number_of_turns = tournament.number_of_turns
            speed = tournament.speed
            info = tournament.tournament_info

            tournament_data = [name, location, date, duration, number_of_turns, speed, info]
            table.append(tournament_data)

        tournament_data_sorted = sorted(table, key=lambda x: x[2])
        self.view.all_tournaments_table(tournament_data_sorted)

    def show_all_players(self, alpha_or_rank, players_list):
        user_input = alpha_or_rank
        table = []

        for player in players_list:
            last_name = player.last_name
            first_name = player.first_name
            date_of_birth = player.date_of_birth
            gender = player.gender
            elo = player.elo

            player_data = [last_name, first_name, date_of_birth, gender, elo]
            table.append(player_data)

        if user_input.lower() == 'a':
            all_player_sorted_by_alpha = sorted(table, key=lambda x: x[0])
            self.view.all_player_table(all_player_sorted_by_alpha)

        elif user_input.lower() == 'r':
            all_player_sorted_by_rank = sorted(table, key=lambda x: x[4], reverse=True)
            self.view.all_player_table(all_player_sorted_by_rank)

    def show_all_players_in_tournament(self, alpha_or_rank, players_list):
        user_input = alpha_or_rank
        table = []

        for player in players_list:
            last_name = player.last_name
            first_name = player.first_name
            date_of_birth = player.date_of_birth
            gender = player.gender
            elo = player.elo

            player_data = [last_name, first_name, date_of_birth, gender, elo]
            table.append(player_data)

        if user_input.lower() == 'a':
            all_player_sorted_by_alpha = sorted(table, key=lambda x: x[0])
            self.view.all_player_table(all_player_sorted_by_alpha)

        elif user_input.lower() == 'r':
            all_player_sorted_by_rank = sorted(table, key=lambda x: x[4], reverse=True)
            self.view.all_player_table(all_player_sorted_by_rank)

    def show_data_inside_tournament(self, user_view, tournaments_list):
        data = user_view
        rounds = data.find(" -r")
        matchs = data.find(" -m")
        players = data.find(" -p")

        if rounds >= 0:
            tournament_target = data.replace(' -r', '')
            for index, name in enumerate(tournaments_list):
                if name.name == tournament_target:
                    for round_data in tournaments_list[index].rounds_list:
                        round_name = round_data[4]
                        round_start = round_data[5]
                        round_end = round_data[6]
                        self.view.round_info_table(round_name, round_start, round_end)

        elif matchs >= 0:
            tournament_target = data.replace(' -m', '')
            for index, name in enumerate(tournaments_list):
                if name.name == tournament_target:
                    for rounds in tournaments_list[index].rounds_list:
                        match1 = rounds[0]
                        match2 = rounds[1]
                        match3 = rounds[2]
                        match4 = rounds[3]
                        round_name = rounds[4]
                        self.view.show_all_matchs(round_name, match1, match2, match3, match4)

        elif players >= 0:
            tournament_target = data.replace(' -p', '')
            for index, name in enumerate(tournaments_list):
                if name.name == tournament_target:
                    user_input = self.view.ask_alpha_or_rank()
                    self.show_all_players(user_input, tournaments_list[index].tournament_players_list)

    def tournament_to_database(self, tournament_to_database):
        serialiazed_tournament = {
            'Name': tournament_to_database.name,
            'Location': tournament_to_database.location,
            'Date': tournament_to_database.date,
            'Duration': tournament_to_database.duration,
            'Number_of_turns': tournament_to_database.number_of_turns,
            'Speed': tournament_to_database.speed,
            'Tournament_info': tournament_to_database.tournament_info,
            'Tournaments_players': model.Player.tourmanent_player_list_serializer(
                tournament_to_database.tournament_players_list),
            'Tournaments_rounds': self.tournament_rounds_list_serializer(
                tournament_to_database.rounds_list)
        }

        model.tournaments_table.insert(serialiazed_tournament)

    def tournament_to_database_save(self, tournament_to_database):
        serialiazed_tournament = {
            'Name': tournament_to_database.name,
            'Location': tournament_to_database.location,
            'Date': tournament_to_database.date,
            'Duration': tournament_to_database.duration,
            'Number_of_turns': tournament_to_database.number_of_turns,
            'Speed': tournament_to_database.speed,
            'Tournament_info': tournament_to_database.tournament_info,
            'Tournaments_players': self.tourmanent_player_list_serializer_save(
                tournament_to_database.tournament_players_list),
            'Tournaments_rounds': self.tournament_rounds_list_serializer(
                tournament_to_database.rounds_list)
        }

        model.save_table.insert(serialiazed_tournament)

    def tourmanent_player_list_serializer_save(self, tournament_player_list):
        player_data = []
        for player in tournament_player_list:
            last_name = player.last_name
            first_name = player.first_name
            date_of_birth = player.date_of_birth
            gender = player.gender
            elo = player.elo
            score = player.score
            last_played = player.last_played

            player = [last_name, first_name, date_of_birth, gender, elo, score, last_played]
            player_data.append(player)

        return player_data

    def tournament_rounds_list_serializer(self, tournament_rounds_list):
        round_data = []
        for round in tournament_rounds_list:
            match_1 = self.tournament_rounds_list_players_serializer(round[0])
            match_2 = self.tournament_rounds_list_players_serializer(round[1])
            match_3 = self.tournament_rounds_list_players_serializer(round[2])
            match_4 = self.tournament_rounds_list_players_serializer(round[3])

            round_name = round[4]
            round_start = round[5]
            try:
                round_end = round[6]
            except IndexError:
                round_end = ''

            round = [match_1, match_2, match_3, match_4, round_name, round_start, round_end]
            round_data.append(round)

        return round_data

    def tournament_rounds_list_players_serializer(self, match):
        players_data = []
        for player in match:
            last_name = player.last_name
            first_name = player.first_name
            date_of_birth = player.date_of_birth
            gender = player.gender
            elo = player.elo

            player = (last_name, first_name, date_of_birth, gender, elo)
            players_data.append(player)

        return players_data

    @staticmethod
    def get_time():
        now = datetime.datetime.now()
        full_now = now.strftime("%d/%m/%Y %H:%M:%S")
        return full_now
 