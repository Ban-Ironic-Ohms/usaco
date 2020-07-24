#opening file
file_in = open(r"C:\Users\Micah\Desktop\Personal\Python\usaco\Word Processor\2.in")

#getting vars
metadata = file_in.readline()
total_words = metadata.split()[0]
chars_per_line = metadata.split()[1]
chars_per_line = int(chars_per_line)

essay = file_in.readline()

#getting words
words = essay.split()

#making the lines
current_chars = 0
lines = []
currentline = ""

for item in words:

    if len(item) <= (chars_per_line - current_chars):
        currentline = currentline + item + " "
        current_chars += len(item)

    elif len(item) >= (chars_per_line - current_chars):
        lines.append(currentline)
 
        currentline = ""
        current_chars= 0
        currentline = currentline + item + " "
        current_chars += len(item)

    if item == words[-1]:
        lines.append(item + " ")

unspaced = [sub[:-1] for sub in lines]

print(unspaced)