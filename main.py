"""
Tournaments specs :
    Name
    Location
    Date
        From 1 to multiple days
    Nombre of turns
        Where Default = 4
    Turns
        List that store the TURNS
    Players 
        List that store the 8 PLAYERS (player data + player score)
    Time setup
        Bullet / Blitz / "Coup rapide"
    Description
        Tournament's creator remarks
    

Player specs :
    Last name
    First name
    Date of birth
    Gender
    Ranking
        A positive number


Turns specs :
    Name (Round1, Round2, ...)
    Matchs
        List that store the MATCHS (tuples)
    Start
        Date & hours - Must auto fill
    End
        Date & hours - Must auto fill
    

Matchs specs :
    Match info 
        2 players + score for each
        Gets updated at the end of a match (add score)
    A match return a tuple, that contains 2 lists
        each list store the player_info + player_score


In recap :
    a TOURNAMENT is a LIST of TURNS
    a TURN is a LIST of 4 MATCHS
    a MATCH is a TUPLE composed of 2 TOURNAMENT_PLAYER
    a PLAYER is a list composed of PLAYER_INFO + PLAYER_SCORE

Point system :
    px_score = ask for input : 
        Win = 1
        Draw = 0.5
        Loose = 0 


How to form pairs :
    1. Class play per rank
    2. Cut : Top half (T) / Lower half (L)
    3. Pair the top player of each half, and so on (P1/P5, P2/P6, ...)
    4. Once all the maths played & score entered, class player per total points
    5. Pair P1 with P2, P3 with P4, ... and so on
    6. If P1 already played with P2, then play vs P3
    7. Repeat from [4.]


### OTHER INFOS ###
The program must follow the MVC standard ---> Must be cut in 3 parts:
    - Model
        * Data control; fetch data from database
    - View
        * What is seen;
    - Control
        * Where the logic happens;

Always ue a class instead of a dictionary
Use flake8 with [max_line = 119]
Redact a README.md


Program logic :
    Use a menu to navigate

    - Add a player
    - Modify a player ranking

    - Create a new tournament
        1. Select "Create new tournament"
        2. Add 8 players
        3. Computer setup pairs for the first round
        4. When the turns end, add results
        5. Repeat step.3 and step.4 until every turns have been played AND tournament is over
        6. Tournament is over, results are shown in a clean manner

    - Save the current tournament
    - Load an older tournament results

    - Show list of ALL players
        - by alphabetical order
        - by ranking
    - Show list of ALL player [IN THE CURRENT TOURNAMENT]
        - by alphabetical order
        - by ranking
    - Show list of ALL tournaments
    - Show list of ALL turns in a tournament
    - Show list of ALL matchs in a tournament
"""