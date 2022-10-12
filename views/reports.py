from prettytable import PrettyTable


class Reports:

    def __init__(self):

        self.table = PrettyTable()

        self.player_report_field_names = [
            "ID",
            "Last name",
            "First name",
            "Gender",
            "Date of birth",
            "Rank"
        ]

        self.tournament_report_field_names = [
            "ID",
            "Name",
            "Location",
            "Description",
            "Start date",
            "End date",
            "Time control",
            "Last round played",
            "Players (ID : Name)",
        ]

        self.matches_report_field_names = [
            "Name P1",
            "Rank P1",
            "Score P1",
            " ",
            "Name P2",
            "Rank P2",
            "Score P2"
        ]

        self.rounds_report_field_names = [
            "Round #",
            "Started at",
            "Ended at",
            "Matches"
        ]

    def display_players(self, players, sorting):
        """Display player report (all sorting types)"""
        self.table.clear()
        self.table.field_names = self.player_report_field_names
        self.table.align = "l"

        for i in range(len(players)):
            self.table.add_row([
                players[i]["id"],
                players[i]["last_name"],
                players[i]["first_name"],
                players[i]["gender"],
                players[i]["date_of_birth"],
                players[i]["rank"]
            ])

        print(f"\n\n\n- All players ({sorting}) -\n")
        print(self.table)
