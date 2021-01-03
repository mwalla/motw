import pickle
from pkg_resources import resource_stream, resource_exists, resource_filename
from sys import exit


class Tracker(object):
    """Tracker for multiple Monster of the Week game characters.

    Saves and loads characters in pickle format.
    """

    def __init__(self):
        self.characters = {}
        try:
            self.character_file = resource_stream(__name__, "pickle/characters.pkl")
        except FileNotFoundError:
            self.character_file = None
        self.character_file_name = resource_filename(
            __name__, "pickle/characters.pkl"
        )
        if resource_exists(__name__, "pickle/characters.pkl"):
            self.load_characters()

    def save_characters(self):
        with open(self.character_file_name, "wb") as f:
            pickle.dump(self.characters, f)

    def load_characters(self):
        if not self.character_file:
            return
        try:
            self.characters = pickle.load(self.character_file)
            return 1
        except FileNotFoundError:
            print("You haven't created any characters yet.")
        except EOFError:
            print("You haven't created any characters yet.")

    def quit(self):
        self.save_characters()
        exit()


if __name__ == "__main__":
    pass
