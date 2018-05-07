# https://www.reddit.com/r/dailyprogrammer/comments/7yyt8e/20180220_challenge_352_easy_making_imgurstyle/

def solution(number):

    result = ""

    while True:
        if number == 1:
            result += "1"
            break
        else:
            result += str(number % 62)
            number = number // 62
    
    print(result[::-1])

def test_solution():
    pass
