THEM_ROCK = "A"
THEM_PAPER = "B"
THEM_SCISSORS = "C"
ME_ROCK = "X"
ME_PAPER = "Y"
ME_SCISSORS = "Z"
P2_LOSS = "X"
P2_DRAW = "Y"
P2_WIN = "Z"

wins = [
    [THEM_ROCK, ME_PAPER],
    [THEM_PAPER, ME_SCISSORS],
    [THEM_SCISSORS, ME_ROCK]
]

draws = [
    [THEM_ROCK, ME_ROCK],
    [THEM_PAPER, ME_PAPER],
    [THEM_SCISSORS, ME_SCISSORS]
]

losses = [
    [THEM_ROCK, ME_SCISSORS],
    [THEM_PAPER, ME_ROCK],
    [THEM_SCISSORS, ME_PAPER]
]

BASE_SCORE = {
    ME_ROCK: 1,
    ME_PAPER: 2,
    ME_SCISSORS: 3
}


def score_part1(play):
    result = BASE_SCORE[play[1]]
    if play in wins:
        return result + 6
    elif play in draws:
        return result + 3
    elif play in losses:
        return result
    else:
        raise "Shouldn't ever get here!"


def score_part2(play):
    if play[1] == P2_LOSS:
        qq = losses
        return score_part1(get_play_based_on_outcome(play, losses))
    elif play[1] == P2_DRAW:
        return score_part1(get_play_based_on_outcome(play, draws))
    elif play[1] == P2_WIN:
        return score_part1(get_play_based_on_outcome(play, wins))


def get_play_based_on_outcome(play, outcome):
    my_play = [x for x in outcome if x[0] == play[0]][0]
    return my_play


def get_strategy_guide():
    with open("day2_input.txt") as f:
        strategy_guide = [x.strip().split(" ") for x in f.readlines()]
    return strategy_guide


def part_1():
    strategy_guide = get_strategy_guide()
    print(sum(score_part1(play) for play in strategy_guide))


def part_2():
    strategy_guide = get_strategy_guide()
    print(sum(score_part2(play) for play in strategy_guide))


if __name__ == "__main__":
    part_1()
    part_2()
