file_in = open(r"C:\Users\Micah\Desktop\Personal\Python\usaco\demo\1.in")

def split(word): 
    return [char for char in word]

line_num = 1
elements = []
for line in file_in:
    add = []
    if line[:-1] != "..........":
        add.append(line[:-1])
        add.append(line_num)
        elements.append(add)
    line_num += 1

place = []
for i in elements:
    row = split(i[0])
    column = 1
    for cord in row:
        if cord != ".":
            place.append(cord)
            place.append(i[1])
            place.append(column)
        column += 1
print(place)