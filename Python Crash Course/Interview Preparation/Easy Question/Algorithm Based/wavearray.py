# Sort an array in a wave-like form.
# Rearrange arr[0] with arr[1], arr[2] with arr[3], etc.

def sortInWave(arr):

    n = len(arr)

    for i in range(0, n-1, 2):
        arr[i], arr[i + 1] = arr[i + 1], arr[i]

    return print(arr)

sortInWave([1, 2, 3, 4, 5])