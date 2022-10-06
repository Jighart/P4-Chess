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
        return f"{self.first_name} {self.last_name} ({self.tournament_score} points)"

    def serialized_player(self):
        player_infos = {}
        player_infos['Nom'] = self.last_name
        player_infos['Prénom'] = self.first_name
        player_infos['Date de naissance'] = self.birthdate
        player_infos['Sexe'] = self.gender
        player_infos['Classement'] = self.ranking
        player_infos['Score'] = self.tournament_score
        player_infos['Id du joueur'] = self.player_id
        return player_infos

