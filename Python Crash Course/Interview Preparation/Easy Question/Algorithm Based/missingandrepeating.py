# Unsorted array. Array elements range from 1 to len(arr)
# There's a set that has numbers in it from 1 to len(arr)
# There is also a number that occurs twice in the array
# Find these two numbers
def miss_repeat(arr):
#TODO: Create a frequency array of size n+1 initialized with 0s.
    n = len(arr)
    freq_arr = [0] * (n + 1)
    repeating = -1
    missing = -1

#TODO: Traverse the input array and increment the frequency count for each element
# at its corresponding index in frequency array
    for i in range(n):
        freq_arr[arr[i]] += 1

#TODO: Traverse the frequency array from index 1 to n. indices with a frequency of 0
# is our missing number. indices with a frequency of 2 is our repeating number.
    for i in range(1, n + 1):
        if freq_arr[i] == 0:
            missing = i
        elif freq_arr[i] == 2:
            repeating = i
    return print([repeating, missing])
#TODO: Return repeating and missing numbers


miss_repeat([3, 1, 3])