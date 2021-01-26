cows = input()
ids1 = input()
ids1 = ids1.split()
ids = []
even_ids = []
odd_ids = []

total = 0

for i in ids1:
    ids.append(int(i))

for num in ids:
    if num % 2 != 1:
        even_ids.append(num)
    else:
        odd_ids.append(num)

num_of_even = len(even_ids)
num_of_odd = len(odd_ids)

if abs(num_of_even - num_of_odd) < 2:
    print(int(cows))
    exit()
    
if num_of_even > num_of_odd:
    longer = even_ids
    shorter = odd_ids
else:
    longer = odd_ids
    shorter = even_ids
#print(shorter)
#print(longer)
for i in range(len(shorter)):
    even_ids.pop(0)
    total += 1
    odd_ids.pop(0)
    total += 1

while True:
    try:
        longer.pop(0)
        longer.pop(0)
        total += 1
        #print(f"removed 2, total is now {total}")
    except IndexError:
        break
    try:
        longer.pop(0)
        longer.pop(0)
        longer.pop(0)
        total += 1
        #print(f"removed 1, total is now {total}")
    except IndexError:
        break

print(total)    