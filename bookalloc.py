def is_feasible(arr, k, max_pages):
    students = 1
    current_sum = 0

    for pages in arr:
        if current_sum + pages > max_pages:
            students += 1
            current_sum = pages
        else:
            current_sum += pages

    return students <= k


def allocate_min_pages(arr, k):
    # Edge case
    if k > len(arr):
        return -1

    low = max(arr)       # At least one book must be assigned
    high = sum(arr)      # One student takes all books
    result = high

    while low <= high:
        mid = low + (high - low) // 2  # Safe mid

        if is_feasible(arr, k, mid):
            result = mid
            high = mid - 1  # Try smaller max
        else:
            low = mid + 1   # Increase limit

    return result


# 🔥 Test it
arr = [10, 5, 20]
k = 2
print(allocate_min_pages(arr, k))  # Expected: 20
