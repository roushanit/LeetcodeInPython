def search_rotated(nums, target):
    low, high = 0, len(nums) - 1

    while low <= high:
        mid = (low + high) // 2

        if nums[mid] == target:
            return mid

        # Right half is sorted
        if nums[mid] <= nums[high]:
            if nums[mid] <= target <= nums[high]:
                low = mid + 1
            else:
                high = mid - 1

        # Left half is sorted
        else:
            if nums[low] <= target <= nums[mid]:
                high = mid - 1
            else:
                low = mid + 1

    return -1


# ---- CLI TEST ----
if __name__ == "__main__":
    nums = list(map(int, input("Enter rotated sorted array: ").split()))
    target = int(input("Enter target: "))

    index = search_rotated(nums, target)
    print("Index:", index)
