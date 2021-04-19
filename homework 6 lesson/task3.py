my_list = ['a', 'b', 'c', 'd', 'e']

#  output: {0: 'a', 1: 'b', 2: 'c', 3: 'd', 4: 'e'}

d = {x: y for x in range(5) for y in my_list[x]}

print(d)
