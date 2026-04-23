def aggressiveCows(stalls, k):
    stalls.sort()
    n = len(stalls)

    def canPlace(dist):
        count = 1
        last_pos = stalls[0]

        for i in range(1, n):
            if stalls[i] - last_pos >= dist:
                count += 1
                last_pos = stalls[i]
            
            if count >= k:
                return True

        return False

    low = 1
    high = stalls[-1] - stalls[0]
    res = -1

    while low <= high:
        mid = (low + high) // 2

        if canPlace(mid):
            res = mid
            low = mid + 1   # maximize distance
        else:
            high = mid - 1

    return res


# -------- RUN --------
stalls = [1, 2, 4, 8, 9]
k = 3
print(aggressiveCows(stalls, k))  # Expected: 3
