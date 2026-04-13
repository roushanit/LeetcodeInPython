def sort_012(arr):
    low = 0          # Boundary for 0s (next position to place 0)
    mid = 0          # Current element being examined
    high = len(arr) - 1  # Boundary for 2s (next position to place 2)
    
    while mid <= high:
        if arr[mid] == 0:
            # Swap with low, move both low and mid forward
            arr[low], arr[mid] = arr[mid], arr[low]
            low += 1
            mid += 1
        elif arr[mid] == 1:
            # 1 is already in correct position, just move mid
            mid += 1
        else:  # arr[mid] == 2
            # Swap with high, move high backward (don't move mid!)
            arr[mid], arr[high] = arr[high], arr[mid]
            high -= 1
    
    return arr

# Example
arr = [2, 0, 1, 2, 1, 0, 0, 2, 1]
print(sort_012(arr))  # Output: [0, 0, 0, 1, 1, 1, 2, 2, 2]
