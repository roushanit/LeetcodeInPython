def longestConsecutive(nums):
    my_set = set(nums)

    longest = 0

    for num in my_set:
        # start only if it's the beginning of a sequence
        if num - 1 not in my_set:
            x = num
            count = 1

            while x + 1 in my_set:
                x += 1
                count += 1

            longest = max(longest, count)

    return longest


# 🔹 Test input
nums = [1, 99, 101, 98, 2, 5, 3, 100, 1]

# 🔹 Run
result = longestConsecutive(nums)
print("Longest consecutive sequence length:", result)
