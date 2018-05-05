# https://www.reddit.com/r/dailyprogrammer/comments/3r7wxz/20151102_challenge_239_easy_a_game_of_threes/

def solution(value):
    if value == 1:
        print(value)
    else:
        change = [0, -1, 1][value % 3]
        print("{value} {change}".format(value=value, change=change))
        solution((value + change) // 3)
