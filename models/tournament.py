from tinydb import TinyDB


class Tournament:

    def __init__(self, tournament_id, name, location, start_date, end_date, description, time_control, current_round,
                 players, rounds, rounds_total=4):
        self.tournament_id = tournament_id
        self.name = name
        self.location = location
        self.start_date = start_date
        self.end_date = end_date
        self.description = description
        self.time_control = time_control
        self.current_round = current_round
        self.rounds_total = rounds_total
        self.players = players
        self.rounds = rounds

        self.tour_db = TinyDB('database/tournaments.json')

    def serialize_tournament(self):
        """Return serialized tournament info"""
        return {
            "id": self.tournament_id,
            "name": self.name,
            "location": self.location,
            "start_date": self.start_date,
            "end_date": self.end_date,
            "description": self.description,
            "time_control": self.time_control,
            "current_round": self.current_round,
            "rounds_total": self.rounds_total,
            "players": self.players,
            "rounds": self.rounds,
        }

    def save_tournament_db(self):
        """Save new tournament to database
        Set tournament ID as document ID
        """
        db = self.tour_db
        self.tournament_id = db.insert(self.serialize_tournament())
        db.update({'id': self.tournament_id}, doc_ids=[self.tournament_id])

    @staticmethod
    def load_tournament_db():
        """Load tournament database
        @return: list of tournaments
        """
        db = TinyDB('database/tournaments.json')
        db.all()
        tournaments_list = []
        for item in db:
            tournaments_list.append(item)

        return
