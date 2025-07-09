def sum_array(arr):
    sum = 0
    if not arr:
        return 0
    for i in range(len(arr) - 1, -1):
        add = arr[i] + arr[i + 1]
        sum += add
    print(sum)

sum_array([2, 4, 5, 6, 7])