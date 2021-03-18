

class Controller():

    def __init__(self):
        print("TOrga has started")

    def first_round_match_generator(player_rank_list):
        players_rankings_ordered = sorted(player_rank_list, reverse=True)
        middle = len(players_rankings_ordered)//2
        top_half_ranking_players = players_rankings_ordered[:middle]
        bottom_half_ranking_players = players_rankings_ordered[middle:]

        first_turn_match_1 = [top_half_ranking_players[0], bottom_half_ranking_players[0]]
        first_turn_match_2 = [top_half_ranking_players[1], bottom_half_ranking_players[1]]
        first_turn_match_3 = [top_half_ranking_players[2], bottom_half_ranking_players[2]]
        first_turn_match_4 = [top_half_ranking_players[3], bottom_half_ranking_players[3]]

        return first_turn_match_1, first_turn_match_2, first_turn_match_3, first_turn_match_4
