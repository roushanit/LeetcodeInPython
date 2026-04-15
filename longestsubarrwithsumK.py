def longest_subarray_with_sum_k(arr, k):
    prev_sum = {}   # hashmap to store prefix sum -> index
    total_sum = 0
    max_len = 0

    for i in range(len(arr)):
        total_sum += arr[i]

        # Case 1: if total_sum itself equals k
        if total_sum == k:
            max_len = i + 1

        # Case 2: if (total_sum - k) seen before
        if (total_sum - k) in prev_sum:
            length = i - prev_sum[total_sum - k]
            max_len = max(max_len, length)

        # Store prefix sum only if not already present
        if total_sum not in prev_sum:
            prev_sum[total_sum] = i

    return max_len
    

print("Longest subarray length:", longest_subarray_with_sum_k([1, 2, 3, -2, 5, 1, -1, 2], 3))    
