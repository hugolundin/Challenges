import pytest

# http://adventofcode.com/2016/day/1

def solution(_file):
    with open(_file, 'r') as instructions:
        instructions = [x.strip() for x in instructions.read().split(',')]
        
        for instruction in instructions:
            pass

def test_solution():
    pass