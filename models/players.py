from tinydb import TinyDB


class Player:

    def __init__(self, player_id, last_name, first_name, birthdate, gender, rank):
        self.player_id = player_id
        self.last_name = last_name
        self.first_name = first_name
        self.birthdate = birthdate
        self.gender = gender
        self.rank = rank
        self.score = 0
        self.opponents = []

        self.players_db = TinyDB('database/players.json')

    def __str__(self):
        return f"{self.first_name} {self.last_name} ({self.score} points)"

    def serialize_player(self):
        """Return serialized player info"""
        return {
            "id": self.player_id,
            "last_name": self.last_name,
            "first_name": self.first_name,
            "date_of_birth": self.birthdate,
            "gender": self.gender,
            "rank": self.rank,
            "score": self.score,
            "opponents": self.opponents
        }

    def save_players_db(self):
        """Save new player to database
        Set player ID as document ID
        """
        players_db = self.players_db
        self.player_id = players_db.insert(self.serialize_player())
        players_db.update({'id': self.player_id}, doc_ids=[self.player_id])

    def update_player_db(self, info, option):
        """Update player info (from user input) in database
        @param info: user input (str, or int inf "rank")
        @param option: update info category
        """
        db = self.players_db
        if option == "rank":
            db.update({option: int(info)}, doc_ids=[self.player_id])
        else:
            db.update({option: info}, doc_ids=[self.player_id])

    @staticmethod
    def load_player_db():
        """Load player database
        @return: list of players
        """
        players_db = TinyDB('database/players.json')
        players_db.all()
        players = []
        for item in players_db:
            players.append(item)

        return players
