# Remove duplicates from a sorted array

# Rearrange the array so that all distinct elements
# appear at the beginning in sorted order

# Return the length of this distinct sorted subarray

def remove_dupes(arr):
    diff_num = set()
    idx = 0

    for i in range(len(arr)):
        if arr[i] != diff_num:
            diff_num.add(arr[i])
            arr[idx] = arr[i]
            idx += 1
    unique_list = list(set(diff_num))

    return print(unique_list, idx)

remove_dupes([2, 2, 2, 2, 2])

