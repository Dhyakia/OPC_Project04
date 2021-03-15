import model as md

# Add few players to "database"
player1 = md.Player("Rimonteil", "Antoine", "01.08.1889", "Male", 1200.0)
player2 = md.Player("Rakkas", "Thomas", "06.12.1983", "Male", 1500.0)
player3 = md.Player("Martin", "Isabelle", "21.08.1783", "Female", 800.5)
player4 = md.Player("Nguyen", "Denis", "11.10.1990", "Male", 800.0)
player5 = md.Player("Bontet", "Capucine", "07.07.1907", "Female", 2250.0)
player6 = md.Player("Lacroix", "Camille", "14.02.1405", "Female", 3300.5)
player7 = md.Player("Kapela", "Kevin", "05.08.2001", "Male", 720.5)
player8 = md.Player("Marky", "Marc", "28.03.2010", "Male", 440.0)

# Create tournament
new_tournament = md.Tournament(name="Chess & Cheese",
                               location="City's chess club",
                               date="20.04.21",
                               duration=1,
                               number_of_turns=4,
                               speed="blitz",
                               tournament_infos="New player & veteran are welcome")

# From database's player into tournament's player
number_of_tournament_player = []


def add_tournament_player(player):
    tournament_player_name = (player.first_name + ' ' + player.last_name)
    tournament_player_score = float(0)
    number_of_tournament_player.append("p")
    return [tournament_player_name, tournament_player_score]


tplayer1 = add_tournament_player(player1)
tplayer2 = add_tournament_player(player2)
tplayer3 = add_tournament_player(player3)
tplayer4 = add_tournament_player(player4)
tplayer5 = add_tournament_player(player5)
tplayer6 = add_tournament_player(player6)
tplayer7 = add_tournament_player(player7)
tplayer8 = add_tournament_player(player8)

# Enought players added ? The tournament can start
if len(number_of_tournament_player) == 8:
    tournament_start = 1

# Generate pairs for the first round

if tournament_start == 1:
    tournament_players_ranking_list = [tplayer1, tplayer2, tplayer3, tplayer4,
                                       tplayer5, tplayer6, tplayer7, tplayer8]

    round_start = 1

    def first_turn_pair_generator(tournament_players_ranking_list):
        players_rankings_ordered = sorted(tournament_players_ranking_list, reverse=True)
        top_half_ranking_players = players_rankings_ordered[:len(players_rankings_ordered)//2]
        bottom_half_ranking_players = players_rankings_ordered[len(players_rankings_ordered)//2:]

        players_pair1 = [top_half_ranking_players[0], bottom_half_ranking_players[0]]
        players_pair2 = [top_half_ranking_players[1], bottom_half_ranking_players[1]]
        players_pair3 = [top_half_ranking_players[2], bottom_half_ranking_players[2]]
        players_pair4 = [top_half_ranking_players[3], bottom_half_ranking_players[3]]

        return players_pair1, players_pair2, players_pair3, players_pair4

    round_1 = first_turn_pair_generator(tournament_players_ranking_list)
    print(round_1)
    round_start = 0

    # When the round is over, user press something
    round_over = 1

    # enter the results [Win = 1pts, Loose = 0pts, Draw = 0.5pts]
    if round_over == 1:
        # PLAYER_1 vs PLAYER_2
        # ...
        pass
