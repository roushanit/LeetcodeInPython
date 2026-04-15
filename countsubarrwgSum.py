def count_subarrays_with_sum_k(arr, k):
    prefix_sum = 0
    count = 0
    freq = {0: 1}   # VERY important

    for num in arr:
        prefix_sum += num

        # Check if (prefix_sum - k) exists
        if (prefix_sum - k) in freq:
            count += freq[prefix_sum - k]

        # Update frequency
        freq[prefix_sum] = freq.get(prefix_sum, 0) + 1

    return count


# 🔹 Test
print("Count of subarrays:", count_subarrays_with_sum_k([1, 2, 3, -2, 5, 1, -1, 2], 3))
