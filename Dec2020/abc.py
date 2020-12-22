ints = input()
ints = ints.split()
nums = []
for i in ints:
    nums.append(int(i))

A = 0
B = 0
C = 0

allsum = 0
ab = 0
bc = 0
cd = 0

for i in nums:
    if i > allsum:
        allsum = i

nums.sort()

A = nums[0]
B = nums[1]

C = allsum - A - B

print(A, B, C)