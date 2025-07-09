# Given an integer, remove that element from an array

# Remove all occurences of the element in-place and return the number of elements
# which are not equal to ele

def remove_ele(arr, ele):
    # Track the count of elements not equal to ele
    j = 0

    # Iterate though the array
    for i in arr:
    # If index is not equal to the ele, set index j = index and j++
        if arr[i] != ele:
            #arr[j] creates a sub-array
            arr[j] = arr[i]
            j += 1
    #Return j
    return print(j)

remove_ele([3, 2, 2, 3], 3)
