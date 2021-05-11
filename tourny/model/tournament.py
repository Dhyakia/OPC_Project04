from tourny.model.player import Player
from tourny.model.round import Round
from tourny.model.match import Match
from tourny.model.tinydb import tournaments_table, save_table


class Tournament:
    """Tournament class. It's a tournament."""

    NUMBER_OF_TOURNAMENT_PLAYER = 8

    def __init__(self, name, location, date, duration=int(1), number_of_turns=4, speed='',
                 tournament_info='', players_list=[], rounds_list=[]):
        self.name = name
        self.location = location
        self.date = date
        self.duration = duration
        self.number_of_turns = number_of_turns
        self.speed = speed
        self.tournament_info = tournament_info
        self.tournament_players_list = players_list
        self.rounds_list = rounds_list

    @classmethod
    def database_to_tournaments_list(cls, serialiazed_tournaments):
        """Takes in the tournaments from the database and return a list of tournaments object."""
        tournaments_list = []
        all_serialized_tournament = list(serialiazed_tournaments)
        for tournament in all_serialized_tournament:
            tournament_data = cls.tournament_data_deserializer(tournament)
            tournaments_list.append(tournament_data)

        return tournaments_list

    @classmethod
    def tournament_data_deserializer(cls, serialized_tournament):
        """De-serialize a tournament and return a tournament object."""
        name = serialized_tournament['Name']
        location = serialized_tournament['Location']
        date = serialized_tournament['Date']
        duration = serialized_tournament['Duration']
        number_of_turns = serialized_tournament['Number_of_turns']
        speed = serialized_tournament['Speed']
        tournament_info = serialized_tournament['Tournament_info']
        tournament_players = Player.database_to_tournaments_list_players_list_format(
            serialized_tournament['Tournaments_players'])
        tournament_rounds = Round.database_to_tournaments_list_rounds_list_format(
            serialized_tournament['Tournaments_rounds'])

        tournament = cls(name, location, date, duration, number_of_turns, speed, tournament_info,
                         tournament_players, tournament_rounds)

        return tournament

    def tournament_to_database(self):
        """Serialize a tournament, then add it to the tournament table."""
        serialiazed_tournament = {
            'Name': self.name,
            'Location': self.location,
            'Date': self.date,
            'Duration': self.duration,
            'Number_of_turns': self.number_of_turns,
            'Speed': self.speed,
            'Tournament_info': self.tournament_info,
            'Tournaments_players': Player.tourmanent_player_list_serializer(self.tournament_players_list),
            'Tournaments_rounds': Round.tournament_rounds_list_serializer(self.rounds_list)
        }

        tournaments_table.insert(serialiazed_tournament)

    @classmethod
    def saved_tournament_to_memory(cls, serialiazed_tournaments):
        """De-serialize a tournament, return it as an saved tournament if possible."""
        all_serialized_tournament = list(serialiazed_tournaments)
        for tournament in all_serialized_tournament:
            tournament_data = cls.tournament_data_deserializer(tournament)

        try:
            return tournament_data
        except UnboundLocalError:
            pass

    def tournament_to_database_save(self):
        """Serialize a tournament, then add it to the save table."""
        serialiazed_tournament = {
            'Name': self.name,
            'Location': self.location,
            'Date': self.date,
            'Duration': self.duration,
            'Number_of_turns': self.number_of_turns,
            'Speed': self.speed,
            'Tournament_info': self.tournament_info,
            'Tournaments_players': Player.tourmanent_player_list_serializer_save(
                self.tournament_players_list),
            'Tournaments_rounds': Round.tournament_rounds_list_serializer(
                self.rounds_list)
        }

        save_table.insert(serialiazed_tournament)
