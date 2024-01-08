import os


def clear_console():
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')


def check_collision(obj1, obj2, collision):
    return abs(obj1["x"] - obj2["x"]) <= collision and abs(obj1["y"] - obj2["y"]) <= collision
