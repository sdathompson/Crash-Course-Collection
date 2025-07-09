# Given an array with 4 elements, find the maximum
# product of 3 elements

def max_product(arr):
    arr.sort()
    return max(arr[0] * arr[1] * arr[-1],
               arr[-1] * arr[-2] * arr[-3])

print(max_product([10, 3, 5, 6, 20]))

