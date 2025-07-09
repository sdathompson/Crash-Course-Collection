# Rotate array element to the left by d.

# if d = 2, the first two elements get sent to the end and the third element is pushed to the front

def rot_arr(arr,d):
    n = len(arr)
    # If the d > size of array
    d %= n
    # Use a range instead of an array if you want to compare two arrays
    rotated = arr[d:] + arr[:d]
    print(rotated)


rot_arr([1, 2, 3, 4, 5, 6], d = 2)
rot_arr([2, 1, 3], d = 4)


