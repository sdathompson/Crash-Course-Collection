# Given an array, move all 0s to the end
# without disrupting the order of non-zeros

def move_zero(arr):
    zero_arr = []
    for i in arr:
        if arr[i] == 0:
            popped_zero = arr.pop(i)
            zero_arr.append(popped_zero)
    for i in zero_arr:
        arr.append(i)
    return print(arr)

move_zero([1, 2, 0, 4, 3, 0, 5, 0])




