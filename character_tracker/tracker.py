import pickle
from pprint import pprint as pp
from pkg_resources import resources_stream, resource_exists
from sys import exit
from .utils import get_int_input

character_file = resources_stream(__name__, 'character_tracker/character/characters.pkl')


class Tracker(object):
    """Tracker for multiple Monster of the Week game characters.

    Saves and loads characters in pickle format.
    """

    def __init__(self):
        self.characters = {}
        if resource_exists(__name__, 'character_tracker/character/characters.pkl'):
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
        pickle.dump(self.characters, character_file)

    def load_characters(self):
        try:
            self.characters = pickle.load(character_file)
            return 1
        except FileNotFoundError:
            print("You haven't created any characters yet.")

    def quit(self):
        self.save_characters()
        exit()


if __name__ == "__main__":
    pass
