from tourny.model.match import Match


class Round:
    """Class round. It's a round."""

    def __init__(self, matchs_list):
        self.matchs_list = matchs_list

    def round_start_data(self, round_name, round_start_time):
        self.name = round_name
        self.start = round_start_time

    def round_end_data(self, round_end_time):
        self.end = round_end_time

    @classmethod
    def database_to_tournaments_list_rounds_list_format(cls, tournament_rounds_list_serialized):
        """De-serialize round data inside a tournament, returns a rounds object."""
        rounds_data = []
        for rounds in tournament_rounds_list_serialized:
            match1 = Match.match_player_deserializer(rounds[0])
            match2 = Match.match_player_deserializer(rounds[1])
            match3 = Match.match_player_deserializer(rounds[2])
            match4 = Match.match_player_deserializer(rounds[3])
            round_name = rounds[4]
            round_start = rounds[5]

            try:
                round_end = rounds[6]
            except IndexError:
                round_end = ""

            round = cls([match1, match2, match3, match4])
            round.round_start_data(round_name, round_start)
            round.round_end_data(round_end)
            rounds_data.append(round)

        return rounds_data

    def tournament_rounds_list_serializer(tournament_rounds_list):
        """Serialize a round object."""
        rounds_data = []
        for a_round in tournament_rounds_list:
            a_round_list = []
            for a_match in a_round.matchs_list:
                match = Match.match_player_serializer(a_match)
                a_round_list.append(match)

            round_name = a_round.name
            a_round_list.append(round_name)

            round_start = a_round.start
            a_round_list.append(round_start)
            try:
                round_end = a_round.end
                a_round_list.append(round_end)
            except AttributeError:
                round_end = ''

            rounds_data.append(a_round_list)

        return rounds_data
