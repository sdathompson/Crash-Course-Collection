# Given an array find the third-largest element
# All the elements in the array are distinct integers

# Input: arr[] = {1, 14, 2, 16, 10, 20}
# Output: 14
# Explanation: Largest element is 20, second largest element is 16 and third largest element is 14
#
# Input: arr[] = {19, -10, 20, 14, 2, 16, 10}
# Output: 16
# Explanation: Largest element is 20, second largest element is 19 and third largest element is 16

def third_max(arr):
    arr.sort()
    return arr[-3]

print(third_max([1, 14, 2, 16, 10, 20]))
print(third_max([19, -10, 20, 14, 2 ,16, 10]))


