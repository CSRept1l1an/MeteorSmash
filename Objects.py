from colorama import Fore, Style


def spaceship(spaceship_x, boardW):
    spaces_before = " " * spaceship_x
    spaces_before2 = " " * spaceship_x
    spaces_after = " " * (boardW - spaceship_x - 2)
    spaces_after2 = " " * (boardW - spaceship_x - 3)
    spaceship_line = ("# " + spaces_before + Fore.YELLOW + "A" + Style.RESET_ALL + spaces_after + "#" + "\n" + "#" +
                      spaces_before2 + Fore.YELLOW + "/H\\" + Style.RESET_ALL + spaces_after2 + "#" + "\n" + "# " +
                      spaces_before + Fore.YELLOW + "^" + Style.RESET_ALL + spaces_after + "#")
    print(spaceship_line)


def bullet_creator(bullets, boardW):
    for bullet in bullets:
        bullet_line = ("#" + " " * (bullet["x"] - 1) + Fore.RED + "|" + Style.RESET_ALL +
                       " " * (boardW - bullet["x"]) + "#")
        print(bullet_line)


def meteor_creator(meteors, boardW):
    for meteor in meteors:
        meteor_line = ("#" + " " * meteor["x"] + Fore.CYAN + "*" + Style.RESET_ALL +
                       " " * (boardW - meteor["x"] - 1) + "#")
        print(meteor_line)


def game_board(boardW, boardH, spaceship_x, bullets, meteors, score):
    top_border = "# " * (boardW // 2 + 2)

    print(top_border)  # Top border

    for row in range(1, boardH - 1):  # Adjusted range to exclude top and bottom borders
        if any(bullet["y"] == row for bullet in bullets):
            bullet_creator([bullet for bullet in bullets if bullet["y"] == row], boardW)
        elif any(meteor["y"] == row for meteor in meteors):
            meteor_creator([meteor for meteor in meteors if meteor["y"] == row], boardW)
        else:
            side_borders = "#" + " " * boardW + "#"
            print(side_borders)

    spaceship(spaceship_x, boardW)
    print(f"Score: {score}")
    print(top_border)
