import random
import games
import os
import time
import art


def clear(secs=0):
    time.sleep(secs)
    os.system('cls' if os.name == 'nt' else 'clear')


def main():
    top_games = games.get_games()
    score = 0
    progress = 0

    random.shuffle(top_games)

    while True:
        gameA = top_games[progress]
        gameB = top_games[progress + 1]

        print(art.logo)
        print(f'Compare A: {gameA["name"]}')
        print(art.vs)
        print(f'Compare B: {gameB["name"]}')

        guess = input(
            'Which game is higher on the Top 20 list (\'a\' or \'b\'): ').lower()
        if gameA['position'] < gameB['position'] and guess == 'a':
            score += 1
            print(f'\nCorrect! Current Score: {score}')
            clear(secs=1)
        elif gameB['position'] < gameA['position'] and guess == 'b':
            score += 1
            print(f'\nCorrect! Current Score: {score}')
            clear(secs=1)
        else:
            clear()
            print(f'Sorry that\'s incorrect. Final score: {score}')
            break

        progress += 1


if __name__ == '__main__':
    main()
