# Add the array together and add one to the product
def add_one(arr):

    carry = 1

    n = len(arr)

    for i in range(n - 1, -1, -1):
        # Sum of end plus the carry
        sum = arr[i] + carry
        arr[i] = sum % 10
        carry = sum // 10

    if carry:
        # insert elements at a particular position
        arr.insert(0, carry)

    return arr

add_one([1,2,4])
add_one([9, 9, 9])

