def search_rotated_with_duplicates(nums, target):
    low, high = 0, len(nums) - 1

    while low <= high:
        mid = (low + high) // 2

        if nums[mid] == target:
            return True

        # handle duplicates
        if nums[low] == nums[mid] == nums[high]:
            low += 1
            high -= 1
            continue

        # right half sorted
        if nums[mid] <= nums[high]:
            if nums[mid] <= target <= nums[high]:
                low = mid + 1
            else:
                high = mid - 1

        # left half sorted
        else:
            if nums[low] <= target <= nums[mid]:
                high = mid - 1
            else:
                low = mid + 1

    return False


# ---- CLI TEST ----
if __name__ == "__main__":
    nums = list(map(int, input("Enter rotated sorted array: ").split()))
    target = int(input("Enter target: "))

    found = search_rotated_with_duplicates(nums, target)
    print("Found:", found)
