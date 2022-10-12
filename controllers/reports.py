from models.tournament import Tournament
from views.menu import MenuViews
from views.reports import Reports


class ReportsController:

    def __init__(self):
        self.menu_view = MenuViews()
        self.reports_view = Reports()

    def all_players_name(self, players):
        """Player report (sorted by last name)
        @param players: list of players
        """
        players = sorted(players, key=lambda x: x.get('last_name'))
        self.reports_view.display_players(players, "by name")

