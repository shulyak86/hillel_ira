i = 0
print('random_number is')
while i < 3:
    i = i + 1
    a = input('Please enter an  number:')
    if int(a) == random.randint(0, 10):
        print('You won!')
    else:
        print('You lose!')
