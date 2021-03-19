class Ask_user:

    def tournament_name(tournament_name):
        # must be a string
        user_input_tournament_name = input("Enter the tournament's name: ")
        return user_input_tournament_name

    def tournament_location(tournament_location):
        # must be a string
        user_input_tournament_location = input("Enter the tournament's location: ")
        return user_input_tournament_location

    def tournament_date(tournament_date):
        # will need to format the date
        user_input_tournament_tournament_date = input("Date: ")
        return user_input_tournament_tournament_date

    def tournament_duration(tournament_duration):
        # must be an int
        user_input_tournament_duration = input("Enter the duration: ")
        return user_input_tournament_duration

    def tournament_number_of_turns(tournament_number_of_turns):
        # must be an int
        user_input_tournament_number_of_turns = input("Enter the number of rounds: ")
        return user_input_tournament_number_of_turns

    def tournament_speed(tournament_speed):
        # must be string with a date format
        user_input_tournament_speed = input("Format: ")
        return user_input_tournament_speed

    def tournament_info(tournament_info):
        # must be a string
        user_input_tournament_infos = input("Organisator notes: ")
        return user_input_tournament_infos
