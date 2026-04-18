def find_floor_ceil(nums, target):
    low, high = 0, len(nums) - 1
    floor_val = -1
    ceil_val = -1

    while low <= high:
        mid = (low + high) // 2

        if nums[mid] == target:
            return nums[mid], nums[mid]

        elif nums[mid] > target:
            ceil_val = nums[mid]
            high = mid - 1

        else:
            floor_val = nums[mid]
            low = mid + 1

    return floor_val, ceil_val


# ---- CLI TEST ----
if __name__ == "__main__":
    nums = list(map(int, input("Enter sorted array: ").split()))
    target = int(input("Enter target: "))

    floor_val, ceil_val = find_floor_ceil(nums, target)
    print("Floor:", floor_val)
    print("Ceil:", ceil_val)
