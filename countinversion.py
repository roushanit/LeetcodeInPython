def merge_and_count(arr, left, mid, right):
    temp = []
    i = left
    j = mid + 1
    inv_count = 0

    while i <= mid and j <= right:
        if arr[i] <= arr[j]:
            temp.append(arr[i])
            i += 1
        else:
            temp.append(arr[j])
            inv_count += (mid - i + 1)  # key step
            j += 1

    while i <= mid:
        temp.append(arr[i])
        i += 1

    while j <= right:
        temp.append(arr[j])
        j += 1

    for k in range(len(temp)):
        arr[left + k] = temp[k]

    return inv_count


def merge_sort(arr, left, right):
    inv_count = 0
    if left < right:
        mid = (left + right) // 2

        inv_count += merge_sort(arr, left, mid)
        inv_count += merge_sort(arr, mid + 1, right)
        inv_count += merge_and_count(arr, left, mid, right)

    return inv_count


def count_inversions_optimal(arr):
    return merge_sort(arr, 0, len(arr) - 1)


# Test
arr = [5, 3, 2, 1, 4]
print(count_inversions_optimal(arr))  # Output: 7
