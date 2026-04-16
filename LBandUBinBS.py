def lower_bound(nums, target):
    n = len(nums)
    lb = n
    low, high = 0, n - 1

    while low <= high:
        mid = (low + high) // 2

        if nums[mid] >= target:
            lb = mid
            high = mid - 1
        else:
            low = mid + 1

    return lb


def upper_bound(nums, target):
    n = len(nums)
    ub = n
    low, high = 0, n - 1

    while low <= high:
        mid = (low + high) // 2

        if nums[mid] > target:
            ub = mid
            high = mid - 1
        else:
            low = mid + 1

    return ub


# ====== INPUT PART ======
nums = list(map(int, input("Enter sorted array: ").split()))
target = int(input("Enter target: "))

# ====== FUNCTION CALL ======
lb = lower_bound(nums, target)
ub = upper_bound(nums, target)

# ====== OUTPUT ======
print("Lower Bound Index:", lb)
print("Upper Bound Index:", ub)
