import math

def sum_by_d(arr, div):
    total = 0
    for num in arr:
        total += math.ceil(num / div)
    return total

def smallest_divisor(arr, limit):
    low = 1
    high = max(arr)

    while low <= high:
        mid = (low + high) // 2

        if sum_by_d(arr, mid) <= limit:
            high = mid - 1
        else:
            low = mid + 1

    return low

arr = [1, 2, 5, 9]
limit = 6
print(smallest_divisor(arr, limit))  # Expected output: 5    
