def nextPermutation(nums):
    n = len(nums)
    ind = -1

    # Step 1: find pivot
    for i in range(n - 2, -1, -1):
        if nums[i] < nums[i + 1]:
            ind = i
            break

    # Step 2: if no pivot, reverse whole array
    if ind == -1:
        nums.reverse()
        return nums

    # Step 3: find next greater element
    for i in range(n - 1, ind, -1):
        if nums[i] > nums[ind]:
            nums[i], nums[ind] = nums[ind], nums[i]
            break

    # Step 4: reverse suffix
    nums[ind + 1:] = reversed(nums[ind + 1:])

    return nums
#passingsomevalueinarraytoseeoutputofcode    
print(nextPermutation([2,1,5,4,3,0,0]))    
