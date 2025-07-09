# Reverse an array in window size of k

def rev_sub(arr, k):
    # Left pointer
    i = 0
    # Right pointer
    n = len(arr)

    while i < n:
        # While left pointer is less than the length of the list
        # Left pointer intialization
        left = i
        # Right pointer - takes the min from either i + windowsize - 1 (to prevent OOR)
        # or the len(arr) - 1
        right = min(i + k - 1, n - 1)
        while left < right:
            arr[left], arr[right] = arr[right], arr[left]
            left += 1
            right -= 1
        i += k
    if k == 1:
        return arr
