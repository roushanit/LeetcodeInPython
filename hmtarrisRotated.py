def find_k_rotation(arr):
    low, high = 0, len(arr) - 1
    ans = float('inf')
    index = -1

    while low <= high:
        mid = (low + high) // 2

        # Case 1: already sorted
        if arr[low] <= arr[high]:
            if arr[low] < ans:
                ans = arr[low]
                index = low
            break

        # Left half is sorted
        if arr[low] <= arr[mid]:
            if arr[low] < ans:
                ans = arr[low]
                index = low
            low = mid + 1

        # Right half is sorted
        else:
            if arr[mid] < ans:
                ans = arr[mid]
                index = mid
            high = mid - 1

    return index
    
arr = [3, 4, 5, 6, 2]
print(find_k_rotation(arr))   # Output: 3    
