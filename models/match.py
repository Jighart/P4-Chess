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
