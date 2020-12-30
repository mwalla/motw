from .character import Character
from .tracker import Tracker
from pprint import pprint as pp
from .utils import get_int_input, validate_function_choice


class Game(object):
    """For playing a round of Monster of the Week.

    """

    def __init__(self):
        self.tracker = Tracker()
        self.character = None
        self.options = None
        self.option_cd = None

    def create_character(self):
        new = Character()
        new.character_setup()
        self.tracker.characters[new.name] = new
        self.tracker.save_characters()

    def choose_character(self):
        if not self.tracker.characters:
            if not self.tracker.load_characters():
                self.create_character()
        char_cd = {
            i: name for i, name in enumerate(list(self.tracker.characters.keys()), 1)
        }
        pp(char_cd)
        while True:
            choice = get_int_input("character choice")
            if choice in list(char_cd.keys()):
                self.character = self.tracker.characters[char_cd[choice]]
                break
            else:
                print(f'"{choice}" is not a valid choice.')

    def set_options(self):
        self.options = {
            "Investigate a Mystery": self.character.investigate_a_mystery,
            "Read a Bad Situation": self.character.read_a_situation,
            "Act Under Pressure": self.character.act_under_pressure,
            "Kick Some Ass": self.character.kick_some_ass,
            "Use Magic": self.character.use_magic,
            "Big Magic": self.character.big_magic,
            "Protect Someone": self.character.protect,
            "Manipulate Someone": self.character.manipulate_someone,
            "Help Out": self.character.help_out,
            "Harm": self.character.do_harm,
            "Recovery": self.character.recovery,
            "Spend Luck": self.character.spend_luck,
            "Level Up": self.character.level_up,
            "Remind Me": self.character.remind_me,
            "Main Menu": self.main_menu,
            "Save": self.tracker.save_characters,
            "Save and Quit": self.tracker.quit,
        }
        self.option_cd = {
            i: option for i, option in enumerate(list(self.options.keys()), 1)
        }

    def play_a_round(self):
        if not self.character:
            self.choose_character()
        self.set_options()
        while True:
            pp(self.option_cd)
            choice = get_int_input("choice")
            validate_function_choice(
                choice=choice,
                valid_choices=list(self.option_cd.keys()),
                options=self.options,
                option_cd=self.option_cd,
            )

    def main_menu(self):
        options = {
            "Create a Character": self.create_character,
            "Choose a Character": self.choose_character,
            "Play a Round": self.play_a_round,
            "Save and Quit": self.tracker.quit,
        }
        option_cd = {i: option for i, option in enumerate(list(options.keys()), 1)}
        while True:
            print()
            pp(option_cd)
            choice = get_int_input("choice")
            validate_function_choice(
                choice=choice,
                valid_choices=list(option_cd.keys()),
                options=options,
                option_cd=option_cd,
            )


if __name__ == "__main__":
    pass
