#initalizing file
file_in = open(r"C:\Users\Micah\Desktop\Personal\Python\usaco\Triangles\3.in")
strn = file_in.readline()

n = int(strn)

cordnum = 1
cords = []

#establishing cords
while cordnum < n:
    cords.append(file_in.readline())
    cordnum += 1

#making a maximum cordinate
mincord = [str(10**10), str(10**10)]
print(mincord[1])

#making all X and Y cords
x = []
y = []

for i in cords:
    i.split()
    x.append(i[0])
    y.append(i[1])

#establishing bottom left cord
for cord in cords:
    cord = cord.split()
    if cord[0] < mincord[0] and cord[1] < mincord[1]:
        if cord[0] in x and cord[1] in y:
            print(cord, "is lower!")
            mincord = cord
        else:
            print(cord, "has no x or y pairs")
    else:
        print(cord, "is higher")
    
print(mincord)
