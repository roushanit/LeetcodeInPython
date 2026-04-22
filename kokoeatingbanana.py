import math

def total_hours(piles, speed):
    hours = 0
    for bananas in piles:
        hours += math.ceil(bananas / speed)
    return hours

def min_eating_speed(piles, h):
    low = 1
    high = max(piles)
    ans = float('inf')

    while low <= high:
        mid = (low + high) // 2
        hours = total_hours(piles, mid)

        if hours <= h:
            ans = mid
            high = mid - 1
        else:
            low = mid + 1

    return ans
    
piles = [3, 6, 7, 11]
h = 8
print(min_eating_speed(piles, h))  # Output: 4    
