# Rearrange an array into alternate positive negative manner
# without change the relative order

# Extra positive/negative numbers appear at the end of the array

# The array should start with a positive number. 0 is positive


#TODO: Separate the numbers into positive and negative arrays

#TODO: Alternately place numbers from each array back into the original array

#TODO: Place any remaining positive or negative numbers at the end

def pos_neg(arr):
    pos = []
    neg = []

    for num in arr:
        if num >= 0:
            pos.append(num)
        else:
            neg.append(num)

    pos_idx = 0
    neg_idx = 0
    i = 0

    while pos_idx < len(pos) and neg_idx < len(neg):
        # Positive number check
        if i % 2 == 0:
            arr[i] = pos[pos_idx]
            pos_idx += 1
        else:
            arr[i] = neg[neg_idx]
            neg_idx += 1

    while pos_idx < len(pos):
        arr[i] = pos[pos_idx]
        i += 1

    while neg_idx < len(neg):
        arr[i] = neg[neg_idx]
        i += 1

