from datetime import datetime

from views.round import RoundViews
from views.menu import MenuViews


class TournamentController:

    def __init__(self):
        self.menu_view = MenuViews()
        self.round_view = RoundViews()
        self.timer = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    def start_tournament(self, t):
        """Tournament (t) main structure
        Start from first round or resume tournament according to round number
        Set start and end timers and save to DB
        """
        if t.current_round == 1:
            t.start_date = self.timer
            t.update_timer(t.start_date, 'start_date')

            self.first_round(t)
            t.current_round += 1
            t.update_tournament_db()

            while t.current_round <= t.rounds_total:
                self.next_rounds(t)
                t.current_round += 1
                t.update_tournament_db()

        elif 1 < t.current_round <= t.rounds_total:
            while t.current_round <= t.rounds_total:
                self.next_rounds(t)
                t.current_round += 1
                t.update_tournament_db()

            t.end_date = self.timer
            t.update_timer(t.end_date, 'end_date')
            self.tournament_end(t)

        elif t.current_round > t.rounds_total:
            self.tournament_end(t)
