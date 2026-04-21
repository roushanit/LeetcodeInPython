def sqrt_floor(n: int) -> int:
    if n < 2:
        return n

    low, high = 1, n
    ans = 1

    while low <= high:
        mid = low + (high - low) // 2

        # Safe check to avoid overflow (good habit even if Python handles big ints)
        if mid <= n // mid:
            ans = mid
            low = mid + 1
        else:
            high = mid - 1

    return ans
    
print(sqrt_floor(27))    
