def removeElement(nums, val):
    a = len(nums)
    for i, num in enumerate(nums):
        if num != val and i < a:
            nums.append(num)
    nums = nums[a:]
    print(nums)
    return len(nums)
