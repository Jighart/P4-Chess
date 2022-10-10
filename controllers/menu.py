from models.players import Player
from models.tournament import Tournament
from views.menu import MenuViews


class MenuController:

    def __init__(self):
        self.menu_view = MenuViews()

    def main_menu_start(self):
        """Main menu selector :
        Redirects to respective submenus"""

        self.menu_view.main_menu()
        self.menu_view.input_prompt()
        user_input = input().lower()

        match user_input:
            case "1":
                pass  # self.new_tournament()
            case "2":
                pass  # self.resume_tournament()
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

