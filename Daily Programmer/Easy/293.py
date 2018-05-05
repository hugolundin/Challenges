import pytest

# https://www.reddit.com/r/dailyprogrammer/comments/5e4mde/20161121_challenge_293_easy_defusing_the_bomb/

def solution(wires):
    wires = [x.strip() for x in wires.split(',')]
    
    rules = {'white'  : ['purple', 'red', 'green', 'orange'],
             'black'  : ['black', 'purple', 'red'],
             'purple' : ['black', 'red'],
             'red'    : ['green'],
             'green'  : ['orange', 'white'],
             'orange' : ['red', 'black']
    }

    for i in range(0, len(wires) - 1):
        if wires[i+1] not in rules[wires[i]]:
            return False

    return True

def test_solution():
    assert(solution('white, red, green, white') == True)
    assert(solution('white, orange, green, white') == False)