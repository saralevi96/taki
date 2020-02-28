<<<<<<< HEAD
def removeElement(nums, val):
    a = len(nums)
    for i, num in enumerate(nums):
        if num != val and i < a:
            nums.append(num)
    nums = nums[a:]
    print(nums)
    return len(nums)


print(removeElement([3,2,2,3], 3))
=======
print("Git test")
>>>>>>> eccb585d685840919c9e69bdf167466829263a9c
