from prettytable import PrettyTable


class RoundViews:

    def __init__(self):
        self.table = PrettyTable()

        self.rounds_header = [
            "Match #",
            "Name P1",
            "Rank P1",
            "Score P1",
            "Name P2",
            "Rank P2",
            "Score P2"
        ]

        self.results_header = [
            "Tournament ranking",
            "Name",
            "Final Score",
            "Global ranking"
        ]

    def display_matches(self, matches):
        """Display matches for current round as table
        @param matches: list of matches tuples
        """
        self.table.clear()
        self.table.header = self.rounds_header

        for i in range(len(matches)):
            row = list(matches[i])
            row.insert(0, str(i + 1))

            self.table.add_row(row)

        print(self.table)
