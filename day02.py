from enum import Enum
from lib.handle_input import read_input

class Play(Enum):
    ROCK = 1
    PAPER = 2
    SCISSORS = 3

class Result(Enum):
    WIN = 6
    DRAW = 3
    LOSE = 0

p1_translation = {
    'A': Play.ROCK,
    'B': Play.PAPER,
    'C': Play.SCISSORS,
    'X': Play.ROCK,
    'Y': Play.PAPER,
    'Z': Play.SCISSORS
}

def format_data(input_data):
    return input_data.rstrip('\n').split('\n')

def part1():
    rounds = format_data(read_input('data/day02.txt'))
    score = 0
    for game_round in rounds:
        opponent_code, player_code = game_round.split(' ')
        opponent, player = p1_translation[opponent_code], p1_translation[player_code]
        score += calculate_round(opponent, player)
    return score

def calculate_round(opponent, player):
    outcome = play_round(opponent, player)
    return outcome.value + player.value

def play_round(opponent, player):
    if opponent.name == 'ROCK':
        if player.name == 'ROCK':
            return Result.DRAW
        if player.name == 'SCISSORS':
            return Result.LOSE
        if player.name == 'PAPER':
            return Result.WIN
    if opponent.name == 'SCISSORS':
        if player.name == 'ROCK':
            return Result.WIN
        if player.name == 'SCISSORS':
            return Result.DRAW
        if player.name == 'PAPER':
            return Result.LOSE
    if opponent.name == 'PAPER':
        if player.name == 'ROCK':
            return Result.LOSE
        if player.name == 'SCISSORS':
            return Result.WIN
        if player.name == 'PAPER':
            return Result.DRAW
    raise ValueError('Input not a valid RPS play')


def main():
    print('The given strategy will score {}'.format(part1()))

if __name__ == '__main__':
    main()