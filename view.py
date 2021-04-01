# Because all methods ( as of 25.03.2021 ) are statics, it might not be needed to create a class


class View:

    def __init__(self):
        print("Welcome to torga")

    def goodbye():
        print("Goodbye !")

    def ask_main_menu():
        logic_start = input("Do you want to create a [T]ournament or [A]dd a new player ?\n")
        return logic_start

    def ask_tournament_name():
        tournament_name_input = input("Enter the name: ")
        return tournament_name_input

    def ask_tournament_location():
        tournament_location_input = input("Enter the location: ")
        return tournament_location_input

    def ask_tournament_date():
        tournament_date_input = input("Enter the date in YYYY-MM-DD format: ")
        return tournament_date_input

    def ask_tournament_date_help():
        print("You must follow the YYYY-MM-DD format")

    def ask_tournament_duration():
        tournament_duration_input = input("[Empty for default (1 day)] Enter the duration : ")
        return tournament_duration_input

    def ask_tournament_number_of_turns():
        tournament_number_of_turns_input = input("[Empty for default (4 rounds)] Enter the number of rounds: ")
        return tournament_number_of_turns_input

    def ask_tournament_speed():
        tournament_speed_input = input("Enter the speed format: ")
        return tournament_speed_input

    def ask_tournament_speed_help():
        print("Speed format must be 'bullet', blitz' or 'swift play'")

    def ask_tournament_info():
        tournament_info_input = input("TO remark's: ")
        return tournament_info_input

    def ask_player_last_name():
        player_last_name_input = input("Enter last name: ")
        return player_last_name_input

    def ask_player_first_name():
        player_first_name_input = input("Enter first name: ")
        return player_first_name_input

    def ask_player_date_of_birth():
        player_date_of_birth_input = input("Enter birthdate in YYYY-MM-DD format: ")
        return player_date_of_birth_input

    def ask_player_date_of_birth_help():
        print("You must follow the YYYY-MM-DD format")

    def ask_player_gender():
        player_gender_input = input("Enter gender: ")
        return player_gender_input

    def ask_player_elo():
        player_elo_input = input("Enter elo: ")
        return player_elo_input

    def ask_player_elo_help():
        print("The value of the elo must be a float")

    def ask_player_full_name():
        player_full_name = input("Enter the full name of the participant: ")
        return player_full_name

    def player_has_been_added(player_name):
        print(f"{player_name} has succesfully been added into the tournament.")

    def player_has_been_added_help(player_name):
        print(f"{player_name} couldn't be found.")
        print("Either not in the database, or not in the right format (must be :'Lastname Firstname').")

    def tournament_can_start():
        print("Sucessfully added 8 players, the tournament can now start")

    def generating_first_turn_matchs():
        print('generating first turn matchs ...')

    def generating_matchs():
        print('generating matchs ...')

    def show_user_matchup(match1, match2, match3, match4):
        print(f'Match 1: {match1[0].last_name} {match1[0].first_name} VS {match1[1].last_name} {match1[1].first_name}')
        print(f'Match 2: {match2[0].last_name} {match2[0].first_name} VS {match2[1].last_name} {match2[1].first_name}')
        print(f'Match 3: {match3[0].last_name} {match3[0].first_name} VS {match3[1].last_name} {match3[1].first_name}')
        print(f'Match 4: {match4[0].last_name} {match4[0].first_name} VS {match4[1].last_name} {match4[1].first_name}')

    def ask_user_match_result(match_count):
        match_result = input(f"Match {match_count} resultat: ")
        return match_result

    def enter_score_instructions():
        print("Enter 0 for a draw, 1 if player1 won and 2 if player2 won")

    def enter_score_instructions_help():
        print("Enter 0 for a draw, 1 if player_01 won and 2 if player_2 won")
        print("")
        print("Exemple :")
        print("Match 1: X vs Y")
        print("Match 1 resultat: 1")
        print("X won")

    def a_player_won(player_last_name, player_first_name):
        print(f"{player_last_name} {player_first_name} won")

    def draw(match):
        print(f"Match {match} was a draw")
