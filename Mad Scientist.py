#opening files
file_in = open(r'C:\Users\Micah\Desktop\Personal\Python\usaco\Mad Scientest\3.in')
n = file_in.readline()
A = file_in.readline()
B = file_in.readline()

#initalizing and conforming
n = int(n)
toggles = []
i = 0

#finding all mismatched cows
while i < n:
    if A[i] != B[i]:
        toggles.append(i)
    i += 1

#checks if sequential toggles are a thing
#if so, it removed the first element in the list
#this is a hacky way of getting a gibberish list but a correct length
for toggle in toggles:
    if toggle + 1 in toggles:
        toggles.remove(0)

print(len(toggles))

file_in.close()