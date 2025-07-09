# You have an array and an integer k.
# If arr[idx] = k, insert a duplicate element beside it
# Truncate the array to retain size

def insert_dupe(arr, k):
#TODO: Count how many times k appears.
    n = len(arr)
    k_count = arr.count(k)

#TODO: Create two pointers: 1 points to current_arr[-1] and the other points to sum(arr[-1], k)

    current_end = n - 1
    write_idx = n + k_count - 1

#TODO: Starting from the last element, it copies each element to its new position.
# If the element is k, places another k next to it
    while current_end >= 0 and write_idx >= 0:
        if write_idx < n:
            arr[write_idx] = arr[current_end]
        write_idx -= 1

        if arr[current_end] == k:
            if write_idx< n:
                arr[write_idx] = k

        write_idx -= 1

    current_end -= 1
    return arr