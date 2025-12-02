import os
import time

szoveg = ['o','o','o','o','o','o','o','o','o','o','o','o','o','o','o','x']

count = len(szoveg)-1
pos = szoveg.index('x')

for _ in range(100):
    szoveg[pos] = 'o'
    if(pos==count):
        pos = 0
    else:
        pos += 1
        szoveg[pos] = 'x'

    szo = ''
    for kar in szoveg:
        szo = szo + kar
    print(szo)
    time.sleep(250/1000)
    os.system('cls')