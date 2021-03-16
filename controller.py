import model as md
import view

# Add few players to "database"
player1 = md.Player("Rimonteil", "Antoine", "01.08.1889", "Male", 1200.0)
player2 = md.Player("Rakkas", "Thomas", "06.12.1983", "Male", 1500.0)
player3 = md.Player("Martin", "Isabelle", "21.08.1783", "Female", 800.5)
player4 = md.Player("Nguyen", "Denis", "11.10.1990", "Male", 800.0)
player5 = md.Player("Bontet", "Capucine", "07.07.1907", "Female", 2250.0)
player6 = md.Player("Lacroix", "Camille", "14.02.1405", "Female", 3300.5)
player7 = md.Player("Kapela", "Kevin", "05.08.2001", "Male", 720.5)
player8 = md.Player("Mark", "Marky", "28.03.2010", "Male", 440.0)

# add player
if view.create_new_player_option.lower == "y":
    print("ok")

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

# Enough players added, the tournament can start
if len(number_of_tournament_player) == 8:
    tournament_start = True

# Generate pairs for the first round
if tournament_start is True:
    tournament_players_ranking_list = [tplayer1, tplayer2, tplayer3, tplayer4,
                                       tplayer5, tplayer6, tplayer7, tplayer8]

    round_start = True
    round_counter = 1

    def first_turn_pair_generator(tournament_players_ranking_list):
        players_rankings_ordered = sorted(tournament_players_ranking_list, reverse=True)
        top_half_ranking_players = players_rankings_ordered[:len(players_rankings_ordered)//2]
        bottom_half_ranking_players = players_rankings_ordered[len(players_rankings_ordered)//2:]

        turn_1_match_1 = [top_half_ranking_players[0], bottom_half_ranking_players[0]]
        turn_1_match_2 = [top_half_ranking_players[1], bottom_half_ranking_players[1]]
        turn_1_match_3 = [top_half_ranking_players[2], bottom_half_ranking_players[2]]
        turn_1_match_4 = [top_half_ranking_players[3], bottom_half_ranking_players[3]]

        return turn_1_match_1, turn_1_match_2, turn_1_match_3, turn_1_match_4

    round_1 = first_turn_pair_generator(tournament_players_ranking_list)

    match_1 = round_1[0]
    match_2 = round_1[1]
    match_3 = round_1[2]
    match_4 = round_1[3]

    round_start = False

    # When the matches are over, user press something
    round_over = True
    round_counter = round_counter + 1

    # enter the results [Win = 1pts, Loose = 0pts, Draw = 0.5pts]
    if round_over is True:

        def match_resultat(match, score):
            if score == match[0][0]:
                match[0][1] += 1
                return match

            elif score == match[1][0]:
                match[1][1] += 1
                return match

            elif score.lower() == "draw":
                match[0][1] = match[0][1] + 0.5
                match[1][1] = match[1][1] + 0.5
                return match

            else:
                print("You must enter the full name of the participant winner or 'draw'")

        # user input
        match_1_user_input = "Thomas Rakkas"
        match_1_final = match_resultat(match_1, match_1_user_input)

        # user input
        match_2_user_input = "Capucine Bontet"
        match_2_final = match_resultat(match_2, match_2_user_input)

        # user input
        match_3_user_input = "Draw"
        match_3_final = match_resultat(match_3, match_3_user_input)

        # user input
        match_4_user_input = "draw"
        match_4_final = match_resultat(match_4, match_4_user_input)

        round_1_final = match_1_final, match_2_final, match_3_final, match_4_final
