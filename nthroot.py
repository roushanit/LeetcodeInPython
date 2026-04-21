def power(base: int, exp: int, limit: int) -> int:
    result = 1
    for _ in range(exp):
        result *= base
        if result > limit:
            return result
    return result


def nth_root(n: int, m: int) -> int:
    low, high = 1, m

    while low <= high:
        mid = low + (high - low) // 2
        val = power(mid, n, m)

        if val == m:
            return mid
        elif val < m:
            low = mid + 1
        else:
            high = mid - 1

    return -1


print(nth_root(3, 27))  # Output: 3
