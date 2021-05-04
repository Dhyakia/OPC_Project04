from tabulate import tabulate


class View:

    def __init__(self):
        print("Welcome to torga\n")

    def goodbye(self):
        """Print goodbye"""
        print("Goodbye !")

    def ask_main_menu(self):
        """Show user possible input. Return input."""
        print("To create/resume a tourmament, enter [T]\nTo add a new player, enter [A]")
        print("To access the database, enter [D]\nTo quit, enter [X]")
        start = input("")
        return start

    def ask_resume_or_start(self):
        """Show user possible input. Return input."""
        user_input = input("To resume a tournament, enter [R]\nTo start a new tournament, enter [N]\n")
        return user_input

    def ask_player_or_tournament(self):
        """Show user possible input. Return input."""
        print('')
        print("[P] to see all the players\n[T] to see all the tournaments\n[M] to return to the main menu\n")
        print("To see information regarding a specific tournament, simply enter the tournament's name like so:")
        print("'exemple_tournament -r' to see the rounds")
        print("'exemple_tournament -m' to see the matchs")
        print("'exemple_tournament -p' to see the players")
        user_input = input("")
        return user_input

    def ask_alpha_or_rank(self):
        """Show user possible input. Return input."""
        user_input = input("In what order ? [A]lpha or [R]ank\n")
        return user_input

    def ask_tournament_name(self):
        """Show user possible input. Return input."""
        tournament_name_input = input("Enter the name: ")
        return tournament_name_input

    def ask_tournament_location(self):
        """Show user possible input. Return input."""
        tournament_location_input = input("Enter the location: ")
        return tournament_location_input

    def ask_tournament_date(self):
        """Show user possible input. Return input."""
        tournament_date_input = input("Enter the date in YYYY-MM-DD format: ")
        return tournament_date_input

    def ask_tournament_date_help(self):
        """Print an error message."""
        print("You must follow the YYYY-MM-DD format")

    def ask_tournament_duration(self):
        """Show user possible input. Return input."""
        tournament_duration_input = input("[Empty for default (1 day)] Enter the duration : ")
        return tournament_duration_input

    def ask_tournament_number_of_turns(self):
        """Show user possible input. Return input."""
        tournament_number_of_turns_input = input("[Empty for default (4 rounds)] Enter the number of rounds: ")
        return tournament_number_of_turns_input

    def ask_tournament_speed(self):
        """Show user possible input. Return input."""
        tournament_speed_input = input("[Blitz, Bullet or Rapid] Enter the speed format: ")
        return tournament_speed_input

    def ask_tournament_speed_help(self):
        """Print an error message."""
        print("Speed format must be 'bullet', blitz' or 'rapid'")

    def ask_tournament_info(self):
        """Show user possible input. Return input."""
        tournament_info_input = input("TO remark's: ")
        return tournament_info_input

    def ask_player_last_name(self):
        """Show user possible input. Return input."""
        player_last_name_input = input("Enter last name: ")
        return player_last_name_input

    def ask_player_first_name(self):
        """Show user possible input. Return input."""
        player_first_name_input = input("Enter first name: ")
        return player_first_name_input

    def ask_player_date_of_birth(self):
        """Show user possible input. Return input."""
        player_date_of_birth_input = input("Enter birthdate in YYYY-MM-DD format: ")
        return player_date_of_birth_input

    def ask_player_date_of_birth_help(self):
        """Print an error message."""
        print("You must follow the YYYY-MM-DD format")

    def ask_player_gender(self):
        """Show user possible input. Return input."""
        player_gender_input = input("Enter gender: ")
        return player_gender_input

    def ask_player_elo(self):
        """Show user possible input. Return input."""
        player_elo_input = input("Enter elo: ")
        print("")
        return player_elo_input

    def ask_player_elo_help(self):
        """Print an error message."""
        print("The value of the elo must be a float")

    def ask_player_full_name(self):
        """Show user possible input. Return input."""
        player_full_name = input("Enter the full name of the participant: ")
        return player_full_name

    def player_has_been_added(self, player_name):
        """Print a confirmation message."""
        print(f"{player_name} has succesfully been added into the tournament.")

    def player_has_been_added_help(self, player_name):
        """Print an error message."""
        print(f"{player_name} couldn't be found.")
        print("Either not in the database, or not in the right format (must be :'Lastname Firstname').")

    def tournament_can_start(self):
        """Print a confirmation message."""
        print("Sucessfully added 8 players, the tournament can now start")

    def generating_first_turn_matchs(self):
        """Print an informal message."""
        print('generating first turn matchs ...')

    def generating_matchs(self):
        """Print an informal message."""
        print('generating matchs ...')

    def show_user_matchup(self, matchs_list):
        """Takes a list of matchs and show each of them to the user."""
        print('')
        for index, match in enumerate(matchs_list):
            output = (
                f"""Match {index + 1}:
        {match.player1.last_name} {match.player1.first_name} VS {match.player2.last_name} {match.player2.first_name}"""
            )
            print(output)
        print('')

    def ask_user_match_result(self, match_count):
        """Takes user input and return said input"""
        print('')
        match_result = input(f"Match {match_count} resultat: ")
        return match_result

    def enter_score_instructions(self):
        """Print instruction for entering score."""
        print("Enter 0 for a draw, 1 if player1 won and 2 if player2 won")

    def enter_score_instructions_help(self):
        """Print additional instruction for entering score."""
        print('')
        print("Enter 0 for a draw, 1 if player1 won and 2 if player2 won.")
        print("Optionally, you can enter 'save' to save the tournament.")
        print('')

    def a_player_won(self, player_last_name, player_first_name):
        """Print the first and last name of the winner."""
        print(f"{player_last_name} {player_first_name} won")

    def draw(self, match):
        """Print a confirmation of the draw."""
        print(f"Match {match} was a draw")

    def round_1_annoucement(self, time):
        """Takes time and print to the user the round name and date."""
        print('')
        print('Round 1')
        print(f'Start time: {time}')

    def round_second_to_last_annoucement(self, rounds_count, time):
        """Takes the round counter and time, and print them to the user."""
        print('')
        print(f'Rounds {rounds_count}')
        print(f'Start time: {time}')

    def end_of_round_time(self, time):
        """Takes time at the end of a round and print it."""
        print('')
        print(f'End time: {time}')
        print('')

    def tournament_player_table(self, table):
        """
        Takes the table of players, and show :
        last name -- first name -- score.
        """
        print('')
        print(tabulate(table, headers=["Last name", "First name", "Score"]))
        print('')

    def all_tournaments_table(self, table):
        """
        Takes the table of tournaments, and show :
        name -- location -- date -- duration -- number of turns -- format -- info.
        """
        print('')
        print(tabulate(table, headers=["Name", "Location", "Date", "Duration", "Number of turns", "Format", "Info"]))
        print('')

    def all_player_table(self, table):
        """
        Takes the table of players, and show :
        last name -- first name -- date of birth -- gender -- elo.
        """
        print('')
        print(tabulate(table, headers=["Last name", "First name", "date of birth", "Gender", "Elo"]))
        print('')

    def round_info_table(self, name, start, end):
        """Takes a round and print its name, start and end."""
        print('')
        print(f'Name:{name}, start:{start}, end:{end}')
        print('')

    def show_all_matchs(self, round):
        """Takes a round and print all matchs in said round."""
        print('')
        print(f'{round.name}')
        for index, match in enumerate(round.matchs_list):
            output = (
                f"""Match {index + 1}:
        {match.player1.last_name} {match.player1.first_name} VS {match.player2.last_name} {match.player2.first_name}"""
            )
            print(output)
        print('')

    def tournament_is_saved(self, tournament_name):
        """Takes a tournament name and print it has a confirmation for save."""
        print('')
        print(f'{tournament_name} tourmament has been saved.')
        print('')

    def show_user_loading(self, tournament_name):
        """Takes a tournament name and print a loading message with said tournament name."""
        print('')
        print(f'{tournament_name} loading ...')
        print('')

    def show_user_loading_successful(self, tournament_name):
        """Takes a tournament name and print a message that confirm to the user the sucess of the loading."""
        print('')
        print(f'{tournament_name} successfully loaded, the tournament can now resume')
        print('')

    def show_user_right_name_input(self):
        """Show user the correct formating of a player."""
        print('')
        print("Incorrect input. Make sure you typed 'Lastname Firstname' correctly.")
        print('')
