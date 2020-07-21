#open file and read lines
file_in = open(r"C:\Users\Micah\Desktop\Personal\Python\usaco\Swapity Swap\1.in")

metadata = file_in.readline()
metadata = metadata.split()
n = metadata[0]
K = metadata[1]
K = int(K)
n = int(n)

swap1 = file_in.readline()
swap2 = file_in.readline()

cows = []
i = 1

while i <= n:
    cows.append(i)
    i += 1

def swap(one, two, list):
    try:
        one = int(one)
        one -= 1
        two = int(two)
        two -= 1
    except ValueError:
        print("Oh no! not a valid input")
        exit

    first = list[one]
    second = list[two]

    list[one] = second
    list[two] = first

    print(cows)

i = 1
while i <= K:
    a = swap1.split()[0] #2
    b = swap1.split()[1] #5
    c = swap2.split()[0] #3
    d = swap2.split()[1] #7
    swap(a, b, cows)
    swap(c, d, cows)
    i += 1

