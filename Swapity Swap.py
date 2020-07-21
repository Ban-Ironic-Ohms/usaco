#open file and read lines
file_in = open(r"C:\Users\Micah\Desktop\Personal\Python\usaco\Swapity Swap\1.in")

metadata = file_in.readline()
metadata = metadata.split()
n = metadata[0]
K = metadata[1]
K = int(K)


#getting all swaps
swaps = []

swap_num = 1

while swap_num < K:
    swaps.append((file_in.readline())
    swap_num += 1

print(swaps)