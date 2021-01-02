import json
from pkg_resources import resource_stream
from sys import exit


def get_int_input(something):
    while True:
        level = input(f"Enter your {something}:\n")
        if level == "q":
            exit()
        try:
            level = int(level)
            return level
        except ValueError:
            print("Please enter a number.")


def get_str_input(something):
    while True:
        input_ = input(f"Tell me {something}\n")
        if input_ == "q":
            exit()
        else:
            return input_


def validate_function_choice(choice, valid_choices, options, option_cd):
    if choice in valid_choices:
        options[option_cd[choice]]()
        print()
    else:
        print(f'"{choice}" not a valid choice.')


def validate_option_choice(choice, valid_choices, chosen):
    if choice in valid_choices:
        chosen.append(choice)
        return 0
    else:
        print(f'"{choice}" is not a valid choice.')
        return 1


def load_resource(kind):
    resource = resource_stream(__name__, f"archetypes/{kind}.json")
    string = resource.read()
    info = json.loads(string)
    return info
