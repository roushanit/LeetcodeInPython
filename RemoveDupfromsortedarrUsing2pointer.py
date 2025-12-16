def removeDuplicates(nums):
    n = len(nums)

    if n == 1:
        return 1

    i = 0
    j = i + 1

    while j < n:
        if nums[j] != nums[i]:
            i += 1
            nums[i], nums[j] = nums[j], nums[i]
        j += 1

    return i + 1


nums = [1, 1, 1, 2, 3, 4, 4, 6, 6, 7, 9, 9, 9, 10, 11]
k = removeDuplicates(nums)

print(k)
print(nums[:k])

