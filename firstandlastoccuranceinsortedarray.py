def lower_bound(nums, target):
    low, high = 0, len(nums) - 1
    lb = -1

    while low <= high:
        mid = (low + high) // 2

        if nums[mid] >= target:
            lb = mid
            high = mid - 1
        else:
            low = mid + 1

    return lb


def upper_bound(nums, target):
    low, high = 0, len(nums) - 1
    ub = -1

    while low <= high:
        mid = (low + high) // 2

        if nums[mid] > target:
            ub = mid
            high = mid - 1
        else:
            low = mid + 1

    return ub


def search_range(nums, target):
    lb = lower_bound(nums, target)

    # target not present
    if lb == -1 or nums[lb] != target:
        return [-1, -1]

    ub = upper_bound(nums, target)

    # if no element greater than target, last index is end of array
    if ub == -1:
        return [lb, len(nums) - 1]

    return [lb, ub - 1]


# ---- CLI TEST ----
if __name__ == "__main__":
    nums = list(map(int, input("Enter sorted array: ").split()))
    target = int(input("Enter target: "))

    result = search_range(nums, target)
    print("First and Last Occurrence:", result)
