import time
import random
import msvcrt
from colorama import init
from Objects import game_board
from Functions import clear_console, check_collision

init(autoreset=True)  # Initialize colorama

boardW = 25
boardH = 25

# Define constants for scoring
SCORE_PER_HIT = 10

collision = 1  # Adjust the collision range as needed


def main():
    spaceship_x = boardW // 2 - 1
    bullets = []
    meteors = []
    meteor_spawn_interval = 10  # Increase this value to reduce meteor spawn frequency
    meteor_spawn_counter = 0
    score = 0

    while True:
        clear_console()

        game_board(boardW, boardH, spaceship_x, bullets, meteors, score)

        if msvcrt.kbhit():
            key = msvcrt.getch()

            if key == b'q':
                break
            elif key == b'a' or key == b'\xe0K' or key == b'A':  # Left arrow key or 'a'
                spaceship_x = max(spaceship_x - 1, 0)
            elif key == b'd' or key == b'\xe0M' or key == b'D':  # Right arrow key or 'd'
                spaceship_x = min(spaceship_x + 1, boardW - 3)
            elif key == b's':
                new_bullet = {"x": spaceship_x + 2, "y": boardH - 2}  # Move 1 point to the right
                bullets.append(new_bullet)

        # Update bullets' positions and handle collisions with meteors
        bullets = [{"x": bullet["x"], "y": bullet["y"] - 1} for bullet in bullets if bullet["y"] > 0]

        # Remove bullets and meteors that collided
        bullets_to_remove = []
        for bullet in bullets:
            for meteor in meteors:
                if check_collision(bullet, meteor, collision):
                    bullets_to_remove.append(bullet)
                    meteors.remove(meteor)
                    score += SCORE_PER_HIT

        for bullet in bullets_to_remove:
            bullets.remove(bullet)

        # Update meteors' positions and spawn new ones
        meteor_spawn_counter += 1
        if meteor_spawn_counter >= meteor_spawn_interval:
            new_meteor = {"x": random.randint(0, boardW - 1), "y": 0}
            meteors.append(new_meteor)
            meteor_spawn_counter = 0

        meteors = [{"x": meteor["x"], "y": meteor["y"] + 1} for meteor in meteors if meteor["y"] < boardH - 1]

        time.sleep(0.2)  # Adjust the delay to control the speed of the spaceship, bullets, and meteors


if __name__ == "__main__":
    main()
