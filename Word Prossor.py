#opening file
file_in = open(r"C:\Users\Micah\Desktop\Personal\Python\usaco\Word Processor\1.in")

#getting vars
metadata = file_in.readline()
total_words = metadata.split()[0]
chars_per_line = metadata.split()[1]

essay = file_in.readline()

#getting words
words = essay.split()

#making the lines
current_chars = 0
line1 = ""
currentline = line1
for item in words:
    if len(item) < (chars_per_line - current_chars):
        currentline = currentline + " " + item
    elif len(item) > (chars_per_line - current_chars):
        currentline = 

