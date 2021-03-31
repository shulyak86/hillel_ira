# chesses Kon6))))
goriz = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
enumerate(goriz)
vertic = ['1', '2', '3', '4', '5', '6', '7', '8']
enumerate(vertic)
vawe_na4alo= input('Please enter a letter and number for your Horse (start):')
vaw_konez= input('Please enter a letter and number for your Horse (end):')
list(str(vawe_na4alo).split())
list(str(vaw_konez).split())
ind_gor = goriz.index(vawe_na4alo[0])
ind_ver = vertic.index(vawe_na4alo[1])
if vaw_konez[0] == goriz[int(ind_gor) + 1] and (vaw_konez[1] == vertic[int(ind_ver) + 2] or vaw_konez[1] == vertic[int(ind_ver) - 2]):
    print('yes')
elif vaw_konez[0] == goriz[int(ind_gor) - 1] and (vaw_konez[1] == vertic[int(ind_ver) + 2] or vaw_konez[1] == vertic[int(ind_ver) - 2]):
    print('yes')
elif vaw_konez[0] == goriz[int(ind_gor) + 2] and (vaw_konez[1] == vertic[int(ind_ver) + 1] or vaw_konez[1] == vertic[int(ind_ver) - 1]):
    print('yes')
elif vaw_konez[0] == goriz[int(ind_gor) - 2] and (vaw_konez[1] == vertic[int(ind_ver) + 1] or vaw_konez[1] == vertic[int(ind_ver) - 1]):
    print('yes')
else:
    print('No!')

