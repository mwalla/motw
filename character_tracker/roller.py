import random
from .phrases import good, bad, okay

NUM_DICE = 2
NUM_SIDES = 6


class Roller:
    def __init__(self, skill: str, skill_adjustment: int):
        self.dice = [random.randint for _ in range(NUM_DICE)]
        self.phrase = None
        self.skill = skill
        self.skill_adjustment = skill_adjustment
        self.result = None
        self.output = ""

    def roll(self):
        self.result = [roll(1, NUM_SIDES) for roll in self.dice]

    def get_phrase(self):
        total = sum(self.result) + self.skill_adjustment
        if total < 7:
            phrase = random.sample(bad, 2)
            self.phrase = (", ".join(phrase) + "!").capitalize()
            return
        elif 7 <= total < 10:
            phrase = random.sample(okay, 2)
            self.phrase = (", ".join(phrase) + ".").capitalize()
            return
        else:
            phrase = random.sample(good, 2)
            self.phrase = (", ".join(phrase) + "!").capitalize()
            return

    def get_result_string(self):
        adj_str = " +" if self.skill_adjustment >= 0 else " "
        self.output += "--".join(["\u2304"] * 10)
        self.output += f"""
Roll: {', '.join([str(x) for x in self.result])}
Total: {sum(self.result)}
{' ' * 5}{adj_str}{self.skill_adjustment} {self.skill}
{' ' * 6}{'-' * 4}
Final: {sum(self.result) + self.skill_adjustment}
{self.phrase}
"""
        self.output += "--".join(["^"] * 10)

    def main(self):
        self.roll()
        self.get_phrase()
        self.get_result_string()
        return sum(self.result) + self.skill_adjustment, self.output


if __name__ == "__main__":
    pass
