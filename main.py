import random
import games
import os
import time


def clear():
    time.sleep(1)
    os.system('cls' if os.name == 'nt' else 'clear')


def main():
    top_games = games.get_games()
    score = 0
    progress = 0

    random.shuffle(top_games)

    while True:
        gameA = top_games[progress]
        gameB = top_games[progress + 1]

        print(f'Compare A: {gameA["name"]}')
        print(f'Compare B: {gameB["name"]}')

        guess = input(
            'Which game is higher on the Top 20 list (\'a\' or \'b\'): ').lower()
        if gameA['position'] < gameB['position'] and guess == 'a':
            score += 1
            clear()
            print(f'Correct! Current Score: {score}')
        elif gameB['position'] < gameA['position'] and guess == 'b':
            score += 1
            clear()
            print(f'Correct! Current Score: {score}')
        else:
            clear()
            print(f'Sorry that\'s incorrect. Final score: {score}')
            break

        progress += 1


if __name__ == '__main__':
    main()
