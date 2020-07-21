file_in = open("breedflip.in")

n = file_in.readline()
A = file_in.readline()
B = file_in.readline()

toggles = []

for i in n:
    if A[i] != B[i]:
        toggles.append(i)

file_in.close()