def twoSum(nums, target):
        d = {}
        idx=[]
        for i, x in enumerate(nums):
            d[x] = i
        for num in nums:
            if target-num in d:
                idx.append(d[num])
                idx.append(d[target-num])
                return idx
        return []

print(twoSum([2,7,11,15], 9))
humans = [9,2,6]

for i in range(len(l)):
    l[i] = 0
    print(l[i])


for i, human in enumerate(humans):
    print(i)
    print(": ")
    print(human)

