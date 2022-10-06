class Round:

    # ROUND_NUMBER = 1

    def __init__(self, name=None, start_time=None, end_time=None, list_of_finished_matchs=None):
        self.name = name
        self.start_time = start_time
        self.end_time = end_time
        self.list_of_finished_matchs = list_of_finished_matchs
        self.list_of_Rounds = []

    def __repr__(self):
        return f"{self.name} - Début : {self.start_time}. Fin : {self.end_time}."

    def serialized(self):
        round_infos = {}
        round_infos['Nom'] = self.name
        round_infos['Début'] = self.start_time
        round_infos['Fin'] = self.end_time
        round_infos['Matchs'] = self.list_of_finished_matchs
        return round_infos

