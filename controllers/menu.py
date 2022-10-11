from models.players import Player
from models.tournament import Tournament
from views.menu import MenuViews


class MenuController:

    def __init__(self):
        self.menu_view = MenuViews()
        self.tour_cont = TournamentController()

    def main_menu_start(self):
        """Main menu selector :
        Redirects to respective submenus"""

        self.menu_view.app_title()
        self.menu_view.main_menu()
        self.menu_view.input_prompt()

        user_input = input()

        match user_input:
            case "1":
                self.new_tournament()
            case "2":
                self.resume_tournament()
            case "3":
                pass  # self.new_player()
            case "4":
                pass  # self.update_player()
            case "5":
                pass  # self.reports_menu()
            case "exit":
                exit()
            case _:
                self.menu_view.input_error()
                self.main_menu_start()

    def new_tournament(self):
        """Create new tournament, serialize and save to DB"""
        self.menu_view.create_tournament_header()
        tournament_info = []
        options = [
            "name",
            "location",
            "description"
        ]

        for item in options:
            self.menu_view.input_prompt_text(item)
            user_input = input()

            if user_input == "back":
                self.main_menu_start()

            else:
                tournament_info.append(user_input)

        tournament_info.append(self.input_time_control())
        tour_players = self.select_players(8)

        self.menu_view.review_tournament(tournament_info, tour_players)
        user_input = input().lower()

        if user_input == "y":
            tournament = Tournament(
                tournament_id=0,
                name=tournament_info[0],
                location=tournament_info[1],
                start_date="Not started",
                end_date="TBD",
                description=tournament_info[2],
                time_control=tournament_info[3],
                players=tour_players,
                current_round=1,
                rounds=[]
            )
            tournament.save_tournament_db()
            self.menu_view.tournament_saved()

            self.menu_view.start_tournament_prompt()
            user_input = input()

            if user_input == "y":
                self.tour_cont.start_tournament(tournament)
            elif user_input == "n":
                self.main_menu_start()

        elif user_input == "n":
            self.main_menu_start()

    def input_time_control(self):
        """Select time control for new tournament
        @return: time control (str)
        """
        self.menu_view.time_control_options()
        self.menu_view.input_prompt()
        user_input = input()

        if user_input == "1":
            return "Bullet"
        elif user_input == "2":
            return "Blitz"
        elif user_input == "3":
            return "Rapid"
        elif user_input == "back":
            self.main_menu_start()
        else:
            self.menu_view.input_error()
            self.input_time_control()

    def select_players(self, players_total):
        """Select players for new tournament
        @param players_total: number of players (int)
        @return: list of selected players
        """
        players = Player.load_player_db()
        id_list = []
        for i in range(len(players)):
            id_list.append(players[i]["id"])

        tour_players = []

        i = 0
        while i < players_total:
            self.menu_view.select_players(players, i+1)
            self.menu_view.input_prompt()
            user_input = input()

            if user_input == "back":
                self.main_menu_start()

            elif not user_input.isdigit():
                self.menu_view.input_error()

            elif int(user_input) in id_list:
                index = id_list.index(int(user_input))
                tour_players.append(players[index])
                id_list.remove(id_list[index])
                players.remove(players[index])
                i += 1

            else:
                self.menu_view.player_already_selected()

        return tour_players

    def resume_tournament(self):
        """Select existing tournament to resume"""
        tournament_list = Tournament.load_tournament_db()

        self.menu_view.select_tournament(tournament_list)
        self.menu_view.input_prompt()
        user_input = input()

        if user_input == "back":
            self.main_menu_start()

        for i in range(len(tournament_list)):
            if user_input == str(tournament_list[i]["id"]):
                t = tournament_list[i]
                t = Tournament(
                    t["id"],
                    t["name"],
                    t["location"],
                    t["start_date"],
                    t["end_date"],
                    t["description"],
                    t["time_control"],
                    t["current_round"],
                    t["players"],
                    t["rounds"],
                    t["rounds_total"]
                )
                self.tour_cont.start_tournament(t)
