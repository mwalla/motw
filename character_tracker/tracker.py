import os
import pickle
from pprint import pprint as pp
from sys import exit
from .utils import get_int_input


class Tracker(object):
    """Tracker for multiple Monster of the Week game characters.

    """

    def __init__(self):
        self.characters = {}
        if os.path.isfile(os.path.join("characters", "characters.pkl")):
            self.load_characters()

    def chose_character(self):
        char_cd = {i: name for i, name in enumerate(list(self.characters.keys()), 1)}
        print()
        print("Your characters:")
        pp(char_cd)
        while True:
            choice = get_int_input("character choice")
            if choice in list(char_cd.keys()):
                return self.characters[char_cd[choice]]
            else:
                print(f'"{choice}" is not a valid choice.')

    def save_characters(self):
        with open(
            os.path.join(
                os.getcwd(), "character_tracker", "characters", "characters.pkl"
            ),
            "wb",
        ) as f:
            pickle.dump(self.characters, f)

    def load_characters(self):
        try:
            with open(
                os.path.join(
                    os.getcwd(), "character_tracker", "characters", "characters.pkl"
                ),
                "rb",
            ) as f:
                self.characters = pickle.load(f)
                return 1
        except FileNotFoundError:
            print("You haven't created any characters yet.")

    def quit(self):
        self.save_characters()
        exit()


if __name__ == "__main__":
    pass
