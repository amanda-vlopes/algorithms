def find_duplicate(nums):
    nums.sort()

    for index in range(0, len(nums) - 1):
        if type(nums[index]) is str or nums[index] < 0:
            return False
        if nums[index] == nums[index + 1]:
            return nums[index]

    return False


print(find_duplicate([1, 2, 2, 3, 4]))
