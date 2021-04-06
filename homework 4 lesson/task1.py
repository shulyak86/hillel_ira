import math
x = input('skolko kilometrov v pervyi den?')
y = input('skolko kilometrov vsego probezhal?')
day = (int(y)/int(x))**(10/11)
print(math.ceil(day))


