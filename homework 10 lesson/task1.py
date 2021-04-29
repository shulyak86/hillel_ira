def vawi_stroki():
    a = str
    file = open("vawi stroki.txt", "w")
    while a:
        a = input('vvedite vawi stroki:')
        file.write(a + '\n')
    file.close()


vawi_stroki()
