# There's an array of length N with prices of stocks
# You traverse down the array for each index, checking the min so far
# Update the result if we get a minimum that's bigger than the current max

def max_profit(prices):
    min_so_far = prices[0]
    result = 0
    for buy in range(1, len(prices)):
        # min_so_far is the minimum between the current stored minimum
        # and the current part of the array
        min_so_far = min(min_so_far, prices[buy])

        # result is the max between the current stored result
        # and the profit calculations (current stock price - current minimum)
        result = max(result, prices[buy] - min_so_far)

    return print(result)

max_profit([7, 10, 1, 3, 6, 9, 2])
max_profit([7, 6, 4, 3, 1])
max_profit([1, 3, 6, 9, 11])
