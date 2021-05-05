win = int(input('please enter number of wins: '))
draw = int(input('please enter number of draws: '))
loss = int(input('please enter number of losses: '))


def count_points(win, draw, loss):
    points = win * 3 + draw
    return points

print(count_points(win, draw, loss))
