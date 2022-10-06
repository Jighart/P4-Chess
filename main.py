from pathlib import Path
from views.menu import MainMenu

if __name__ == "__main__":
    Path("database/").mkdir(exist_ok=True)
    MainMenu().display_main_menu()
