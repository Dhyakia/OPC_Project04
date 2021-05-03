from tabulate import tabulate


class View:

    def __init__(self):
        print("Welcome to torga\n")

    def goodbye(self):
        print("Goodbye !")

    def ask_main_menu(self):
        print("To create/resume a tourmament, enter [T]\nTo add a new player, enter [A]")
        print("To access the database, enter [D]\nTo quit, enter [X]")
        start = input("")
        return start

    def ask_resume_or_start(self):
        user_input = input("To resume a tournament, enter [R]\nTo start a new tournament, enter [N]\n")
        return user_input

    def ask_player_or_tournament(self):
        print('')
        print("[P] to see all the players\n[T] to see all the tournaments\n[M] to return to the main menu\n")
        print("To see information regarding a specific tournament, simply enter the tournament's name like so:")
        print("'exemple_tournament -r' to see the rounds")
        print("'exemple_tournament -m' to see the matchs")
        print("'exemple_tournament -p' to see the players")
        user_input = input("")
        return user_input

    def ask_alpha_or_rank(self):
        user_input = input("In what order ? [A]lpha or [R]ank\n")
        return user_input

    def ask_tournament_name(self):
        tournament_name_input = input("Enter the name: ")
        return tournament_name_input

    def ask_tournament_location(self):
        tournament_location_input = input("Enter the location: ")
        return tournament_location_input

    def ask_tournament_date(self):
        tournament_date_input = input("Enter the date in YYYY-MM-DD format: ")
        return tournament_date_input

    def ask_tournament_date_help(self):
        print("You must follow the YYYY-MM-DD format")

    def ask_tournament_duration(self):
        tournament_duration_input = input("[Empty for default (1 day)] Enter the duration : ")
        return tournament_duration_input

    def ask_tournament_number_of_turns(self):
        tournament_number_of_turns_input = input("[Empty for default (4 rounds)] Enter the number of rounds: ")
        return tournament_number_of_turns_input

    def ask_tournament_speed(self):
        tournament_speed_input = input("[Blitz, Bullet or Rapid] Enter the speed format: ")
        return tournament_speed_input

    def ask_tournament_speed_help(self):
        print("Speed format must be 'bullet', blitz' or 'rapid'")

    def ask_tournament_info(self):
        tournament_info_input = input("TO remark's: ")
        return tournament_info_input

    def ask_player_last_name(self):
        player_last_name_input = input("Enter last name: ")
        return player_last_name_input

    def ask_player_first_name(self):
        player_first_name_input = input("Enter first name: ")
        return player_first_name_input

    def ask_player_date_of_birth(self):
        player_date_of_birth_input = input("Enter birthdate in YYYY-MM-DD format: ")
        return player_date_of_birth_input

    def ask_player_date_of_birth_help(self):
        print("You must follow the YYYY-MM-DD format")

    def ask_player_gender(self):
        player_gender_input = input("Enter gender: ")
        return player_gender_input

    def ask_player_elo(self):
        player_elo_input = input("Enter elo: ")
        print("")
        return player_elo_input

    def ask_player_elo_help(self):
        print("The value of the elo must be a float")

    def ask_player_full_name(self):
        player_full_name = input("Enter the full name of the participant: ")
        return player_full_name

    def player_has_been_added(self, player_name):
        print(f"{player_name} has succesfully been added into the tournament.")

    def player_has_been_added_help(self, player_name):
        print(f"{player_name} couldn't be found.")
        print("Either not in the database, or not in the right format (must be :'Lastname Firstname').")

    def tournament_can_start(self):
        print("Sucessfully added 8 players, the tournament can now start")

    def generating_first_turn_matchs(self):
        print('generating first turn matchs ...')

    def generating_matchs(self):
        print('generating matchs ...')

    def show_user_matchup(self, matchs_list):
        print('')
        for index, match in enumerate(matchs_list):
            print(f'Match {index + 1}: {match.player1.last_name} {match.player1.first_name} VS {match.player2.last_name} {match.player2.first_name}')
        print('')

    def ask_user_match_result(self, match_count):
        print('')
        match_result = input(f"Match {match_count} resultat: ")
        return match_result

    def enter_score_instructions(self):
        print("Enter 0 for a draw, 1 if player1 won and 2 if player2 won")

    def enter_score_instructions_help(self):
        print("Enter 0 for a draw, 1 if player_01 won and 2 if player_2 won")
        print("Exemple :")
        print("Match 1: X vs Y")
        print("Match 1 resultat: 1")
        print("X won")

    def a_player_won(self, player_last_name, player_first_name):
        print(f"{player_last_name} {player_first_name} won")

    def draw(self, match):
        print(f"Match {match} was a draw")

    def round_1_annoucement(self, time):
        print('')
        print('Round 1')
        print(f'Start time: {time}')

    def round_second_to_last_annoucement(self, rounds_count, time):
        print('')
        print(f'Rounds {rounds_count}')
        print(f'Start time: {time}')

    def end_of_round_time(self, time):
        print('')
        print(f'End time: {time}')
        print('')

    def tournament_player_table(self, table):
        print('')
        print(tabulate(table, headers=["Last name", "First name", "Score"]))
        print('')

    def all_tournaments_table(self, table):
        print('')
        print(tabulate(table, headers=["Name", "Location", "Date", "Duration", "Number of turns", "Format", "Info"]))
        print('')

    def all_player_table(self, table):
        print('')
        print(tabulate(table, headers=["Last name", "First name", "date of birth", "Gender", "Elo"]))
        print('')

    def round_info_table(self, name, start, end):
        print('')
        print(f'Name:{name}, start:{start}, end:{end}')
        print('')

    def show_all_matchs(self, round):
        print('')
        print(f'{round.name}')
        for index, match in enumerate(round.matchs_list):
            print(f'Match{index + 1}: {match.player1.last_name} {match.player1.first_name} VS {match.player2.last_name} {match.player2.first_name}')
        print('')

    def tournament_is_saved(self, tournament_name):
        print('')
        print(f'{tournament_name} tourmament has been saved.')
        print('')

    def show_user_loading(self, tournament_name):
        print('')
        print(f'{tournament_name} loading ...')
        print('')

    def show_user_loading_successful(self, tournament_name):
        print('')
        print(f'{tournament_name} successfully loaded, the tournament can now resume')
        print('')

    def show_user_right_name_input(self):
        print('')
        print("Incorrect input. Make sure you typed 'Lastname Firstname' correctly.")
        print('')
