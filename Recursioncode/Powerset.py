def powerset(s):
    result = []

    def solve(curr, idx):
        if idx >= len(s):
            result.append(curr)
            return

        # include
        solve(curr + s[idx], idx + 1)

        # exclude
        solve(curr, idx + 1)

    solve("", 0)
    return result


# Test
print(powerset("abc"))
