class Player:

    def __init__(self, last_name=None,
                 first_name=None,
                 birthdate=None,
                 gender=None,
                 ranking=None,
                 tournament_score=0,
                 player_id=0
                 ):
        self.last_name = last_name
        self.first_name = first_name
        self.birthdate = birthdate
        self.gender = gender
        self.ranking = ranking
        self.tournament_score = tournament_score
        self.player_id = player_id

    def __str__(self):
        return f"{self.last_name} {self.first_name}"

    def __repr__(self):
        return f"{self.last_name} {self.first_name}, classement : {self.ranking}"
