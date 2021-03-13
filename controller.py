import model as md

# create tournament with required specifications
new_tournament = md.Tournament("Chess & Cheese", "City's chess club", "20.04.21",
                               duration=1, number_of_turns=4, speed="blitz",
                               tournament_infos="New player & veteran are welcome")

print('')

# add 8 players
tplayer1 = md.Player("Rimonteil", "Antoine", "01.08.1889", "Male", 1200)
tplayer2 = md.Player("Rimonteil", "Thomas", "06.12.1983", "Male", 1500)
tplayer3 = md.Player("Martin", "Isabelle", "21.08.1783", "Female", 800)
tplayer4 = md.Player("Nguyen", "Denis", "11.10.1990", "Male", 800)
tplayer5 = md.Player("Bontet", "Capucine", "07.07.1907", "Female", 2250)
tplayer6 = md.Player("Lacroix", "Camille", "14.02.1405", "Female", 3300)
tplayer7 = md.Player("Kapela", "Kevin", "05.08.2001", "Male", 720)
tplayer8 = md.Player("Marky", "Marc", "28.03.2010", "Male", 440)

print('')

# generate pairs (1/5, 2/6, 3/7, 4/8)
# 1. Order player by their rank
# 2. Divide in 2 half, one with the top players, the other with the lower-ranking players
# 3. First player of each list against each other, second player of each list against each other, and so on
tournament_players_ranking_list = [tplayer1.elo, tplayer2.elo, tplayer3.elo, tplayer4.elo,
                                   tplayer5.elo, tplayer6.elo, tplayer7.elo, tplayer8.elo]


def first_turn_pair_generator(tournament_players_ranking_list):
    players_rankings_ordered = sorted(tournament_players_ranking_list, reverse=True)
    top_half_ranking_players = players_rankings_ordered[:len(players_rankings_ordered)//2]
    bottom_half_ranking_players = players_rankings_ordered[len(players_rankings_ordered)//2:]

    # A loop may be more elegant there
    match1 = [top_half_ranking_players[0], bottom_half_ranking_players[0]]
    match2 = [top_half_ranking_players[1], bottom_half_ranking_players[1]]
    match3 = [top_half_ranking_players[2], bottom_half_ranking_players[2]]
    match4 = [top_half_ranking_players[3], bottom_half_ranking_players[3]]

    return match1, match2, match3, match4


print(first_turn_pair_generator(tournament_players_ranking_list))
