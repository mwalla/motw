from pprint import pprint as pp
from character_tracker.character import Character
from character_tracker.utils import validate_option_choice, get_int_input


class Expert(Character):
    def __init__(self):
        super().__init__()

    def get_me_some_gear(self):
        limit = int(self.info["gear"]["limit"])
        pp(self.info["gear"], width=120)
        print(
            f"Chose {limit} gear options.\nEnter the number associated with each chosen gear separately."
        )
        valid_choices = [
            int(choice)
            for choice in list(self.info["gear"].keys())
            if choice != "limit"
        ]
        for _ in range(limit):
            while True:
                choice = get_int_input(f"what gear you'd like to chose")
                if not validate_option_choice(
                    choice=choice, valid_choices=valid_choices, chosen=self.gear
                ):
                    break

    def show_me_the_moves(self):
        limit = int(self.info["moves"]["limit"])
        pp(self.info["moves"], width=120)
        print(
            f"Chose {limit} expert moves.\nEnter the number associated with each chosen move separately."
        )
        valid_choices = [
            int(choice)
            for choice in list(self.info["moves"].keys())
            if choice != "limit"
        ]
        for _ in range(limit):
            while True:
                choice = get_int_input("what move you'd like to chose")
                if not validate_option_choice(
                    choice=choice, valid_choices=valid_choices, chosen=self.moves
                ):
                    break

    def make_me_a_haven(self):
        limit = int(self.info["haven"]["limit"])
        pp(self.info["haven"], width=120)
        print(
            f"Chose {limit} options for your haven.\nEnter the number associated with each chosen option separately."
        )
        valid_choices = [
            int(choice)
            for choice in list(self.info["haven"].keys())
            if choice != "limit"
        ]
        for _ in range(limit):
            while True:
                choice = get_int_input("what option you would like to chose")
                if not validate_option_choice(
                    choice=choice, valid_choices=valid_choices, chosen=self.haven
                ):
                    break

    def remind_me(self):
        output = {
            "moves": {},
            "haven": {},
            "gear": {},
        }
        for move in self.moves:
            name, _, description = self.info["moves"][str(move)].partition(":")
            output["moves"][name] = description
        for have in self.haven:
            name, _, description = self.info["haven"][str(have)].partition(":")
            output["haven"][name] = description
        for item in self.gear:
            name, _, description = self.info["gear"][str(item)].partition(":")
            output["gear"][name] = description
        pp(output)
        pp(
            {
                key: val
                for key, val in self.__dict__.items()
                if isinstance(val, int) or isinstance(val, str)
            },
            depth=1,
        )
