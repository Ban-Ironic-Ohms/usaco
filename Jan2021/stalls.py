cows = "4" #input()
heights_in = "1 2 3 4" #input()
stalls_in ="1 2 3 4" #input()

heights_in = heights_in.split()
stalls_in = stalls_in.split()

heights = []
stalls = []

for i in heights_in:
    heights.append(int(i))
for i in stalls_in:
    stalls.append(int(i))

heights.sort()
stalls.sort()

array = []

for cow in heights:
    for tall in stalls:
        add = []
        add.append(cow)
        add.append(tall)
        array.append(add)

print(array, len(array))