
cows = 6
cows = int(cows)
'''
pos = []
for i in range(cows):
    pos.append(input())
'''

pos = ['E 3 5', 'N 5 3', 'E 4 6', 'E 10 4', 'N 11 2', 'N 8 1']

virt = []
hor = []

for i in pos:
    i = i.split()
    if i[0] == 'N':
        virt.append([i[1], i[2]])
    else:
        hor.append([i[1], i[2]])

wherestopped = []

def isinf(cord, dir, challenge):
    if dir == 'V':
        relcord = int(cord[0]) + int(cord[1])
        for i in challenge:
            reli = int(i[0]) + int(i[1])
            if reli > relcord:
                distance = int(i[1])-int(cord[1])
                wherestopped.append(["V",cord, distance])
                return False
    if dir == 'H':
        relcord = int(cord[0]) + int(cord[1])
        for i in challenge:
            reli = int(i[0]) + int(i[1])
            if reli > relcord:
                distance = int(i[0])-int(cord[0])
                wherestopped.append(["H",cord, distance])
                return False
    return True



infinits = []

for i in virt:
    if isinf(i, 'V', hor) == False:
        virt.remove(i)

for i in hor:
    if isinf(i, 'H', virt) == False:
        hor.remove(i)

for i in virt:
    infinits.append(i)
for i in hor:
    infinits.append(i)
codes = []
for i in infinits:
    codes.append(str(i[0])+ ' ' +str(i[1]))


distances = []
spaces = []

for i in wherestopped:
    code = ""
    for e in i[1]:
        code = code + e + " "
    code = code[:-1]
    distances.append(code)
    spaces.append(i[2])

print(wherestopped)

q = 0
for i in range(cows):
    tester = pos[q]
    tester = tester.split()
    tester = tester[1:3]
    tester = tester[0] + " " +tester[1]

    if tester in codes:
        print("Infinity")
    if tester in distances:
        index = distances.index(tester)
        print(spaces[index])
    q += 1
