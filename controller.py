import model
import view
import datetime


class Controller:

    def __init__(self):
        self.view = view.View()
        self.main()

    def main(self):
        # Main program loop - 4 way menu directed by user input
        flow = True
        while flow is True:
            start_logic = self.view.ask_main_menu()

            # un-serialize data (all players, all tournaments and the previously saved game)
            players_list = self.database_to_players_list(model.players_table.all())
            tournaments_list = self.database_to_tournaments_list(model.tournaments_table.all())
            saved_game = self.saved_tournament_to_memory(model.save_table)

            # "t" for tournament related
            if start_logic.lower() == "t":
                resume_or_start = self.view.ask_resume_or_start()
                self.tournament_logic(resume_or_start, players_list, tournaments_list, saved_game)

            # "a" for adding a new player
            elif start_logic.lower() == "a":
                self.add_player(players_list)

            # "d" for database - this is where the user can see the data
            elif start_logic.lower() == "d":
                user_view = self.view.ask_player_or_tournament()
                self.show_data_list(user_view, players_list, tournaments_list)

            # "x" to exit main loop -> exit program
            elif start_logic.lower() == "x":
                self.view.goodbye()
                flow = False

    def tournament_logic(self, user_input, players_list, tournaments_list, saved_game):
        # Once inside the tournamenent logic, 3 choices for the user

        # 1. "r" to resume and finish the previously saved tournament
        if user_input.lower() == "r":
            self.view.show_user_loading(saved_game.name)
            tournaments_list.append(saved_game)
            self.view.show_user_loading_successful(tournaments_list[-1].name)

            self.view.show_all_matchs(
                tournaments_list[-1].rounds_list[-1][4], tournaments_list[-1].rounds_list[-1][0],
                tournaments_list[-1].rounds_list[-1][1], tournaments_list[-1].rounds_list[-1][2],
                tournaments_list[-1].rounds_list[-1][3])
            self.enter_score(tournaments_list)

            # TODO doesnt loop properly, night need a specific twist of the generator method to properly
            # show the right round number
            number_of_rounds = tournaments_list[-1].number_of_turns
            number_of_loop = number_of_rounds + 1
            for rounds in range(number_of_rounds):
                if rounds >= number_of_loop:
                    self.second_to_last_round_generator(rounds, tournaments_list)
                    self.enter_score(tournaments_list)
                else:
                    pass
            self.end_of_tournament_table(tournaments_list)
            self.tournament_to_database(tournaments_list[-1])

        # 2. "n" to create and start a new tournament
        elif user_input.lower() == "n":
            self.get_new_tournament_data(tournaments_list)
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

        # 3. Any other will send back to the main menu
        else:
            return None

    def get_new_tournament_data(self, tournaments_list):
        # Take user input when the "create new tournament" option is selected
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

        # Once all the data collected, transform into a tournament object
        new_tournament_data = model.Tournament(tournament_name, tournament_location, tournament_date,
                                               tournament_duration, tournament_number_of_turns, tournament_speed,
                                               tournament_info, [], [])

        # Finaly, add the tournament object into the tournament list
        tournaments_list.append(new_tournament_data)

    def get_8_players(self, players_list, tournaments_list):
        # Take user input, search if input is equal to an existing player
        # if the both part of the name match, the player gets added in the player_list inside the tournament
        # loop until said list has 8 players
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
        # Generate the first round of matchs following the Swiss rules
        self.view.generating_first_turn_matchs()
        # Order player per elo
        players_list_by_elo = sorted(tournaments_list[-1].tournament_players_list,
                                     key=lambda x: x.elo, reverse=True)

        # Divide the list in 2 ( 4 top and 4 bottom )
        middle = len(players_list_by_elo) // 2
        top_half_players = players_list_by_elo[:middle]
        bottom_half_players = players_list_by_elo[middle:]

        # First batch of matchs
        match_01 = (top_half_players[0], bottom_half_players[0])
        match_02 = (top_half_players[1], bottom_half_players[1])
        match_03 = (top_half_players[2], bottom_half_players[2])
        match_04 = (top_half_players[3], bottom_half_players[3])

        # add the last_played paremeter for each player, for latter round (avoid rematch)
        top_half_players[0].last_played = bottom_half_players[0].last_name + ' ' + bottom_half_players[0].first_name
        top_half_players[1].last_played = bottom_half_players[1].last_name + ' ' + bottom_half_players[1].first_name
        top_half_players[2].last_played = bottom_half_players[2].last_name + ' ' + bottom_half_players[2].first_name
        top_half_players[3].last_played = bottom_half_players[3].last_name + ' ' + bottom_half_players[3].first_name
        bottom_half_players[0].last_played = top_half_players[0].last_name + ' ' + top_half_players[0].first_name
        bottom_half_players[1].last_played = top_half_players[1].last_name + ' ' + top_half_players[1].first_name
        bottom_half_players[2].last_played = top_half_players[2].last_name + ' ' + top_half_players[2].first_name
        bottom_half_players[3].last_played = top_half_players[3].last_name + ' ' + top_half_players[3].first_name

        # finalize the list round, add it to the tournament round_list and show user the matchups
        round_name = 'Round 1'
        start_time = self.get_time()
        round = [match_01, match_02, match_03, match_04, round_name, start_time]
        tournaments_list[-1].rounds_list.append(round)

        self.view.round_1_annoucement(start_time)
        self.view.show_user_matchup(match_01, match_02, match_03, match_04)

    def second_to_last_round_generator(self, rounds, tournaments_list):
        # Generate matchs by ordering players by score
        self.view.generating_matchs()
        rounds_count = (rounds + 2)

        players_list_by_score = sorted(tournaments_list[-1].tournament_players_list,
                                       key=lambda x: x.score, reverse=True)
        round = []
        index = 1
        # check for last_played == current; yes = take next in list by score, no = match is set
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

        # finalize the list round, add it to the tournament round_list and show user the matchups
        round_name = str(f'Round {rounds_count}')
        start_time = self.get_time()
        round.append(round_name)
        round.append(start_time)

        tournaments_list[-1].rounds_list.append(round)

        self.view.round_second_to_last_annoucement(rounds_count, start_time)
        self.view.show_user_matchup(round[0], round[1], round[2], round[3])

    def enter_score(self, tournaments_list):
        # Take user input to establish score
        self.view.enter_score_instructions()
        match_count = 0

        # "0" = draw        (0.5 point for each player)
        # "1" = player1 win (1point for player1)
        # "2" = player2 win (1point for player2)
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

            # Save current tournament; clean save table, add current tournament data into the save.json
            # Then exit the program
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
        # Tournament is over, show the user a table with the players and their results
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
        # Get data from user input, use it as parameter to create a player object
        # Most parameter require a certain format
        # Once the object created, it gets added into the player_list and the database
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
        self.player_to_database(new_player)
        return None

    def show_data_list(self, user_view, players_list, tournaments_list):
        # sub menu of the "database"

        # "p" to show players
        if user_view.lower() == "p":
            alpha_or_rank = self.view.ask_alpha_or_rank()
            self.show_all_players(alpha_or_rank, players_list)

        # "t" to show tournaments
        elif user_view.lower() == "t":
            self.show_all_tournaments_table(tournaments_list)

        # advanced option -> data inside a specific tournament
        elif len(user_view) > 2:
            self.show_data_inside_tournament(user_view, tournaments_list)

        # "m" to exit to the main menu
        elif user_view.lower() == "m":
            pass

    def show_all_tournaments_table(self, tournaments_list):
        # Format data from each tournament to be readable, add them into a list
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

        # Sort list by name then send it to the view, wich will show the user all the past tournaments
        tournament_data_sorted = sorted(table, key=lambda x: x[2])
        self.view.all_tournaments_table(tournament_data_sorted)

    def show_all_players(self, alpha_or_rank, players_list):
        # sub menu of the show all player, inside "database"
        # will ask the user for input, use to define wich parameter will sort them
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

        # "a" will sort them by alphabetical order
        if user_input.lower() == 'a':
            all_player_sorted_by_alpha = sorted(table, key=lambda x: x[0])
            self.view.all_player_table(all_player_sorted_by_alpha)

        # "r" will sort them by rankings
        elif user_input.lower() == 'r':
            all_player_sorted_by_rank = sorted(table, key=lambda x: x[4], reverse=True)
            self.view.all_player_table(all_player_sorted_by_rank)

    def show_all_players_in_tournament(self, alpha_or_rank, players_list):
        # Format each players data & put then into a list
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

        # Ask user for input, wich will determine what way the list is sorted
        # Sorted list get then pass to the view to show data to the user
        if user_input.lower() == 'a':
            all_player_sorted_by_alpha = sorted(table, key=lambda x: x[0])
            self.view.all_player_table(all_player_sorted_by_alpha)

        elif user_input.lower() == 'r':
            all_player_sorted_by_rank = sorted(table, key=lambda x: x[4], reverse=True)
            self.view.all_player_table(all_player_sorted_by_rank)

    def show_data_inside_tournament(self, user_view, tournaments_list):
        # Method that use a tournament name + suffix to show data inside said tournament
        data = user_view
        rounds = data.find(" -r")
        matchs = data.find(" -m")
        players = data.find(" -p")

        # ("tournament_name" -r) will show all the rounds inside a tournament
        if rounds >= 0:
            tournament_target = data.replace(' -r', '')
            for index, name in enumerate(tournaments_list):
                if name.name == tournament_target:
                    for round_data in tournaments_list[index].rounds_list:
                        round_name = round_data[4]
                        round_start = round_data[5]
                        round_end = round_data[6]
                        self.view.round_info_table(round_name, round_start, round_end)

        # ("tournament_name" -m) will show all the matchs inside a tournament
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

        # ("tournament_name" -p) will show all the players inside a tournament
        elif players >= 0:
            tournament_target = data.replace(' -p', '')
            for index, name in enumerate(tournaments_list):
                if name.name == tournament_target:
                    user_input = self.view.ask_alpha_or_rank()
                    self.show_all_players(user_input, tournaments_list[index].tournament_players_list)

    def player_to_database(self, player_to_dabatase):
        # Serialization method to turn a player object into conform json data
        serialiazed_player = {
            'Last_name': player_to_dabatase.last_name,
            'First_name': player_to_dabatase.first_name,
            'Birthdate': player_to_dabatase.date_of_birth,
            'Gender': player_to_dabatase.gender,
            'Elo': player_to_dabatase.elo
        }

        model.players_table.insert(serialiazed_player)

    def database_to_players_list(self, serialiazed_players):
        # Un-serialization of a player from the data.json
        players_list = []
        all_serialized_player = list(serialiazed_players)
        for player in all_serialized_player:
            last_name = player['Last_name']
            first_name = player['First_name']
            date_of_birth = player['Birthdate']
            gender = player['Gender']
            elo = player['Elo']

            player = model.Player(last_name, first_name, date_of_birth, gender, elo)
            players_list.append(player)

        return players_list

    def tournament_to_database(self, tournament_to_database):
        # Serialization of a tournament object into readable .json data
        serialiazed_tournament = {
            'Name': tournament_to_database.name,
            'Location': tournament_to_database.location,
            'Date': tournament_to_database.date,
            'Duration': tournament_to_database.duration,
            'Number_of_turns': tournament_to_database.number_of_turns,
            'Speed': tournament_to_database.speed,
            'Tournament_info': tournament_to_database.tournament_info,
            'Tournaments_players': self.tourmanent_player_list_serializer(
                tournament_to_database.tournament_players_list),
            'Tournaments_rounds': self.tournament_rounds_list_serializer(
                tournament_to_database.rounds_list)
        }

        model.tournaments_table.insert(serialiazed_tournament)

    def tournament_to_database_save(self, tournament_to_database):
        # Serialization of a tournament being played into readable .json data
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

    def tourmanent_player_list_serializer(self, tournament_player_list):
        # Serialization of the player object for the players in the player_list in a tournament
        player_data = []
        for player in tournament_player_list:
            last_name = player.last_name
            first_name = player.first_name
            date_of_birth = player.date_of_birth
            gender = player.gender
            elo = player.elo

            player = [last_name, first_name, date_of_birth, gender, elo]
            player_data.append(player)

        return player_data

    def tourmanent_player_list_serializer_save(self, tournament_player_list):
        # Serialization of the player object for the players in the player_list in a tournament currently being played
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
        # Serialization of the data inside a round (list), inside a tournament
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
        # Serialization of the players, for each math
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

    def database_to_tournaments_list(self, serialiazed_tournaments):
        # Un-serialization of a tournament from data.json into the memory
        tournaments_list = []
        all_serialized_tournament = list(serialiazed_tournaments)
        for tournament in all_serialized_tournament:
            name = tournament['Name']
            location = tournament['Location']
            date = tournament['Date']
            duration = tournament['Duration']
            number_of_turns = tournament['Number_of_turns']
            speed = tournament['Speed']
            tournament_info = tournament['Tournament_info']
            tournament_players = self.database_to_tournaments_list_players_list_format(
                tournament['Tournaments_players'])
            tournament_rounds = self.database_to_tournaments_list_rounds_list_format(
                tournament['Tournaments_rounds'])

            tournament = model.Tournament(name, location, date, duration, number_of_turns, speed, tournament_info,
                                          tournament_players, tournament_rounds)
            tournaments_list.append(tournament)

        return tournaments_list

    def database_to_tournaments_list_players_list_format(self, tournaments_players_list_serialized):
        # Un-serialization of the players inside a tournament, from data.json into the memory
        players_data = []
        for player in tournaments_players_list_serialized:
            last_name = player[0]
            first_name = player[1]
            date_of_birth = player[2]
            gender = player[3]
            elo = player[4]

            player = model.Player(last_name, first_name, date_of_birth, gender, elo)
            players_data.append(player)

        return players_data

    def database_to_tournaments_list_rounds_list_format(self, tournament_rounds_list_serialized):
        # Un-serialization of the round, in the round_list, inside a tournament, from data.json to the memory
        rounds_data = []
        for rounds in tournament_rounds_list_serialized:
            match_1 = self.database_to_tournaments_list_players_list_format(rounds[0])
            match_2 = self.database_to_tournaments_list_players_list_format(rounds[1])
            match_3 = self.database_to_tournaments_list_players_list_format(rounds[2])
            match_4 = self.database_to_tournaments_list_players_list_format(rounds[3])
            round_name = rounds[4]
            round_start = rounds[5]
            round_end = rounds[6]

            round = [match_1, match_2, match_3, match_4, round_name, round_start, round_end]
            rounds_data.append(round)

        return rounds_data

    def saved_tournament_to_memory(self, serialiazed_tournaments):
        # Un-serialization of the saved tournament, from save.json into the memory
        all_serialized_tournament = list(serialiazed_tournaments)
        for tournament in all_serialized_tournament:
            name = tournament['Name']
            location = tournament['Location']
            date = tournament['Date']
            duration = tournament['Duration']
            number_of_turns = tournament['Number_of_turns']
            speed = tournament['Speed']
            tournament_info = tournament['Tournament_info']
            tournament_players = self.database_to_tournaments_list_players_list_format(
                tournament['Tournaments_players'])
            tournament_rounds = self.database_to_tournaments_list_rounds_list_format(
                tournament['Tournaments_rounds'])

            tournament = model.Tournament(name, location, date, duration, number_of_turns, speed, tournament_info,
                                          tournament_players, tournament_rounds)

        try:
            return tournament
        except UnboundLocalError:
            pass

    def saved_tournament_to_memory_player_list_format(self, tournaments_players_list_serialized):
        # Un-serialization of the players from the player_list inside the tournament in save.json (into memory)
        players_data = []
        for player in tournaments_players_list_serialized:
            last_name = player[0]
            first_name = player[1]
            date_of_birth = player[2]
            gender = player[3]
            elo = player[4]
            score = player[5]
            last_played = player[6]

            player = model.Player(last_name, first_name, date_of_birth, gender, elo, score, last_played)
            players_data.append(player)

        return players_data

    @staticmethod
    def get_time():
        # Static method that return a full date (from year to second) in .datetime format
        now = datetime.datetime.now()
        full_now = now.strftime("%d/%m/%Y %H:%M:%S")
        return full_now
