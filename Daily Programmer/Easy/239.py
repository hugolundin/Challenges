def solution(value):
    if value == 1:
        print(value)
    else:
        change = [0, -1, 1][value % 3]
        print("{value} {change}".format(value=value, change=change))
        solution((value + change) // 3)
