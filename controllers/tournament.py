from datetime import datetime

from models.players import Player
from models.round import Round
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

    def first_round(self, t):
        """First round (r): top players vs. bottom players
        Get pairings and set round to save to DB"""
        r = Round("Round 1", self.timer, "TBD")
        t.sort_players_by_rank()
        top_players, bottom_players = t.split_players()
        self.round_view.round_headers(t, r.start_time)

        for i in range(t.rounds_total):
            r.get_match_pairing(top_players[i], bottom_players[i])
            top_players[i], bottom_players[i] = self.update_opponents(top_players[i], bottom_players[i])

        self.round_view.display_matches(r.matches)

        self.round_view.round_over()
        self.menu_view.input_prompt()
        user_input = input().lower()
        scores_list = []

        if user_input == "ok":
            r.end_time = self.timer
            t.rounds.append(r.set_round())
            t.merge_players(top_players, bottom_players)

            self.end_of_round(scores_list, t, r.matches)

        elif user_input == "back":
            self.back_to_menu()

    def next_rounds(self, t):
        """Next rounds: set possible pairings
        Get pairings and set round to save to DB"""
        r = Round(("Round " + str(t.current_round)), self.timer, "TBD")
        t.sort_players_by_score()
        self.round_view.round_headers(t, r.start_time)

        available_list = t.players
        players_added = []

        k = 0
        while k < t.rounds_total:
            if available_list[1]["id"] in available_list[0]["opponents"]:
                try:
                    available_list, players_added = \
                        self.match_other_option(available_list, players_added, r)
                    t.players = players_added

                except IndexError:
                    available_list, players_added = \
                        self.match_first_option(available_list, players_added, r)
                    t.players = players_added

            elif available_list[1]["id"] not in available_list[0]["opponents"]:
                available_list, players_added = \
                    self.match_first_option(available_list, players_added, r)
                t.players = players_added

            k += 1

        self.round_view.display_matches(r.matches)

        self.round_view.round_over()
        self.menu_view.input_prompt()
        user_input = input().lower()
        scores_list = []

        if user_input == "ok":
            r.end_time = self.timer
            t.rounds.append(r.set_round())
            self.end_of_round(scores_list, t, r.matches)

        elif user_input == "back":
            self.back_to_menu()

    def match_first_option(self, available_list, players_added, r):
        """Main pairing option
        @param available_list: list of players not set in match for current round
        @param players_added: list of players already in match for current round
        @param r: current round
        @return: updated lists
        """
        r.get_match_pairing(available_list[0], available_list[1])
        available_list[0], available_list[1] = self.update_opponents(available_list[0], available_list[1])

        available_list, players_added = self.update_player_lists(
            available_list[0],
            available_list[1],
            available_list,
            players_added
        )

        return available_list, players_added

    def match_other_option(self, available_list, players_added, r):
        """Alternative pairing option
        @param available_list: list of players not set in match for current round
        @param players_added: list of players already in match for current round
        @param r: current round
        @return: updated lists
        """
        r.get_match_pairing(available_list[0], available_list[2])
        available_list[0], available_list[2] = self.update_opponents(available_list[0], available_list[2])

        available_list, players_added = self.update_player_lists(
            available_list[0],
            available_list[2],
            available_list,
            players_added
        )

        return available_list, players_added

    def end_of_round(self, scores_list: list, t, matches):
        """End of round : update player scores
        @param t: current tournament
        @param scores_list: list of scores
        @param matches: list of matches for current round
        @return: players list with updated scores
        """
        for i in range(t.rounds_total):
            self.round_view.score_options(i + 1, matches)
            response = self.input_scores()
            scores_list = self.get_score(response, scores_list)

        t.players = self.update_scores(t.players, scores_list)

        if t.current_round > t.rounds_total:
            self.tournament_end(t)

        return t.players

    def input_scores(self):
        """Score input"""
        self.round_view.score_input_prompt()
        response = input()
        return response

    def get_score(self, response, scores_list: list):
        """Input scores for each match in current round
        @param response: user input (str)
        @param scores_list: list of scores
        @return: updated list of scores
        """
        match response:
            case "0":
                scores_list.extend([0.5, 0.5])
                return scores_list
            case "1":
                scores_list.extend([1.0, 0.0])
                return scores_list
            case "2":
                scores_list.extend([0.0, 1.0])
                return scores_list
            case "back":
                self.back_to_menu()
            case _:
                self.menu_view.input_error()
                self.input_scores()

    @staticmethod
    def update_scores(players, scores_list: list):
        """Update player scores
        @param players: list of players
        @param scores_list: list of scores
        @return: list of players with updated scores
        """
        for i in range(len(players)):
            players[i]["score"] += scores_list[i]

        return players

    @staticmethod
    def update_player_lists(player_1, player_2, available_list, players_added):
        """Update player lists:
        Add unavailable player to respective list
        Remove available player form respective list
        @param player_1: player 1 (dict)
        @param player_2: player 2 (dict)
        @param available_list: list of players not set in match for current round
        @param players_added: list of players already in match for current round
        @return: list of available players, list of unavailable players
        """
        players_added.extend([player_1, player_2])
        available_list.remove(player_1)
        available_list.remove(player_2)

        return available_list, players_added

    @staticmethod
    def update_opponents(player_1, player_2):
        player_1["opponents"].append(player_2["id"])
        player_2["opponents"].append(player_1["id"])

        return player_1, player_2

    def tournament_end(self, t):
        """End of tournament : display final results
        Offer user to update ranks
        @param t: current tournament dict
        """
        t.sort_players_by_rank()
        t.sort_players_by_score()

        self.round_view.display_results(t)

        self.menu_view.update_rank()
        user_input = input()

        players = t.players

        if user_input == "n":
            self.back_to_menu()

        elif user_input == "y":
            while True:
                self.update_ranks(players)

    def update_ranks(self, players):
        """Update player ranks and save to DB
        @param players: tournament player list
        """
        self.menu_view.select_players(players, "to update")
        self.menu_view.input_prompt()
        user_input = input()

        if user_input == "back":
            self.back_to_menu()

        for i in range(len(players)):
            if int(user_input) == players[i]["id"]:
                p = players[players.index(players[i])]
                p = Player(
                    p['id'],
                    p['last_name'],
                    p['first_name'],
                    p['date_of_birth'],
                    p['gender'],
                    p['rank']
                )

                self.menu_view.rank_update_header(p)
                self.menu_view.input_prompt_text("new rank")
                user_input = input()

                if user_input == "back":
                    self.back_to_menu()

                else:
                    p.update_player_db(int(user_input), "rank")
                    players[i]["rank"] = int(user_input)

                    return players

    @staticmethod
    def back_to_menu():
        from controllers.menu import MenuController
        MenuController().main_menu_start()
