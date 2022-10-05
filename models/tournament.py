class Tournament:
    """Use to create an instance of a tournament"""
    def __init__(self, tournament_name=None,
                 location=None,
                 tournament_date=None,
                 number_of_tours=4,
                 time_control=None,
                 description=None,
                 players_ids=None,
                 list_of_tours=None,
                 tournament_id=None
                 ):

        self.tournament_name = tournament_name
        self.location = location
        self.tournament_date = tournament_date
        self.number_of_tours = number_of_tours
        self.time_control = time_control
        self.description = description
        self.players_ids = players_ids
        self.list_of_tours = list_of_tours
        self.tournament_id = tournament_id

    def __repr__(self):
        return f"{self.tournament_name} - {self.location}\n\n {self.list_of_tours}\n"


class Tour:

    # TOUR_NUMBER = 1

    def __init__(self, name=None, begin_time=None, end_time=None, list_of_finished_matchs=None):
        self.name = name
        self.begin_time = begin_time
        self.end_time = end_time
        self.list_of_finished_matchs = list_of_finished_matchs
        self.list_of_tours = []

    def __repr__(self):
        return f"{self.name} - Début : {self.begin_time}. Fin : {self.end_time}."


class Match:

    MATCH_NUMBER = 1

    def __init__(self, player_1=None, player_2=None, score_player_1=0, score_player_2=0):
        self.name = "Match " + str(Match.MATCH_NUMBER)
        self.player_1 = player_1
        self.player_2 = player_2
        self.score_player_1 = score_player_1
        self.score_player_2 = score_player_2

    def __str__(self):
        return f"{self.name} : {self.player_1} --CONTRE-- {self.player_2}."
