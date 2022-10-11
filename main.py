from pathlib import Path
from controllers.menu import MenuController

if __name__ == "__main__":
    Path("database/").mkdir(exist_ok=True)
    MenuController().main_menu_start()
