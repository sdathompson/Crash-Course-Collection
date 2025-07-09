# Given a binary array arr[] consisting of only 0s and 1s,
# find the length of the longest contiguous sequence of either 1s or 0s in the array.

def binary(arr):
    max_count, count = 0, 1
    n = len(arr)
    for i in range(1, n):
        if arr[i] == arr[i - 1]:
            count += 1
        else:
            max_count = max(max_count, count)
            count = 1

    return max(max_count, count)

print(binary([0, 1, 0, 1, 1, 1, 1]))