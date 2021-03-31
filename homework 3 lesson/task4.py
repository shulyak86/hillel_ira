list_of_six = [100, 106, 112, 118, 124, 130, 136, 142, 148, 154, 160, 166, 172, 178, 184, 190, 196]
for i, number in enumerate(list_of_six):
   if number <= 150 and (float(number/5) - int(number/5) == 0):
       print(number)
   continue



