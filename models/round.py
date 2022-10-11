class Round:

    def __init__(self, name, start_time, end_time):
        self.name = name
        self.start_time = start_time
        self.end_time = end_time
        self.matches = []

    def set_round(self):
        """Return round info as list"""
        return [
            self.name,
            self.start_time,
            self.end_time,
            self.matches
        ]

    def get_match_pairing(self, player_1, player_2):
        """Set match paring as tuple"""
        match = (
            f"{player_1['first_name']} {player_1['last_name']}",
            player_1["rank"],
            player_1["score"],
            f"{player_2['first_name']} {player_2['last_name']}",
            player_2["rank"],
            player_2["score"]
        )
        self.matches.append(match)

