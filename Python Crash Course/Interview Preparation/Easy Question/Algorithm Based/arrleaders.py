# Given an array, find the leader.
# An element is a leader if it is greater than or equal to all elements
# to its right

# This means that the rightmost element is always a leader

def arr_leader(arr):
    result = []
    n = len(arr)

#TODO: Scan all elements from right to left in an array, keeping track of the maximum
    max_right = arr[-1]
    result.append(result)

    for i in range(n - 2, -1, -1):
#TODO: When the maximum changes its value, add it to the result
        if arr[i] >= max_right:
            max_right = arr[i]
            result.append(arr[i])
#TODO: Reverse the result
    result.reverse()

    return print(result)

arr_leader([16, 17, 4, 3, 5, 2])
