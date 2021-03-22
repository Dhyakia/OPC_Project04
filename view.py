class View:

    def __init__():
        pass

    # Main related
    def ask_main_menu():
        logic_start = input("Do you want to create a [T]ournament or [A]dd a new player ?\n")
        return logic_start

    # Tournament related
    def ask_tournament_name():
        tournament_name_input = input("Enter the name: ")
        return tournament_name_input

    def ask_tournament_location():
        tournament_location_input = input("Enter the location: ")
        return tournament_location_input

    def ask_tournament_date():
        tournament_date_input = input("Enter the date: ")
        return tournament_date_input

    def ask_tournament_duration():
        tournament_duration_input = input("[Default is: 1 day] Enter the duration : ")
        return tournament_duration_input

    def ask_tournament_number_of_turns():
        tournament_number_of_turns_input = input("[Default is: 4 rounds] Enter the number of rounds: ")
        return tournament_number_of_turns_input

    def ask_tournament_speed():
        tournament_speed_input = input("Enter the speed format: ")
        return tournament_speed_input

    def speed_help():
        print("Speed format must be 'bullet', blitz' or 'swift play'")

    def ask_tournament_info():
        tournament_info_input = input("TO remark's: ")
        return tournament_info_input

    # Player related
    def ask_player_last_name():
        player_last_name_input = input("Enter last name: ")
        return player_last_name_input

    def ask_player_first_name():
        player_first_name_input = input("Enter first name: ")
        return player_first_name_input

    def ask_player_date_of_birth():
        player_date_of_birth_input = input("Enter birthdate: ")
        return player_date_of_birth_input

    def ask_player_gender():
        player_gender_input = input("Enter gender: ")
        return player_gender_input

    def ask_player_elo():
        player_elo_input = input("Enter elo: ")
        return player_elo_input

    def elo_help():
        print("The value of the elo must be a float")
