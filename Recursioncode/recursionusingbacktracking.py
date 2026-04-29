def head_recursion(n):
    if n == 0:
        return
    head_recursion(n - 1)   # recursion first
    print(n, end=" ")


# Test
n = 4
print("Head Recursion Output:")
head_recursion(n)


def tail_recursion(n):
    if n == 0:
        return
    print(n, end=" ")       # work first
    tail_recursion(n - 1)


# Test
n = 4
print("\nTail Recursion Output:")
tail_recursion(n)
