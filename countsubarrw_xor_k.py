def count_subarrays_with_xor_k(arr, k):
    xr = 0
    count = 0
    freq = {0: 1}   # important

    for num in arr:
        xr ^= num   # prefix XOR

        # Check if required XOR exists
        required = xr ^ k
        if required in freq:
            count += freq[required]

        # Update frequency
        freq[xr] = freq.get(xr, 0) + 1

    return count


# 🔹 Test
arr = [4, 2, 2, 6, 4]
k = 6

print("Count of subarrays:", count_subarrays_with_xor_k(arr, k))
