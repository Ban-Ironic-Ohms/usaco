flowers = input() 
petals = input()

flowers = int(flowers)
petals = petals.split()
p=[]
for i in petals:
    p.append(int(i))

averages = flowers

def isav(nums):
    total = 0
    for i in nums:
        total += i
    av = total/len(nums)
    if av in nums:
        return True
    else:
        return False

size = 1
total = 1

it = 1
while it != flowers:
    total += it+1
    it += 1

start = 0
end = size

for i in range(total-flowers):
    if size < (flowers-1):
        test = p[start:(end+1)]

        if isav(test) == True:
            averages += 1
            start += 1
            end += 1
        elif isav(test) == False:
            start += 1
            end += 1         
    if  end >= flowers:
        size += 1
        start = 0
        end = size


if isav(p) == True:
    averages +=1

print(averages)