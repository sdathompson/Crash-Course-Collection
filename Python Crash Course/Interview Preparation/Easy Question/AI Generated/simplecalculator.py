# Take a list of numbers and returns a dictionary
# with the sum, average, and max


def calc(numbers):
    total_sum = 0
    total_average = 0.0
    total_max = 0
    result = dict()
    for num in numbers:
        total_sum = sum(numbers)
        total_average = total_sum / len(numbers)
        total_max = max(numbers)

    result['sum'] = total_sum
    result['average'] = total_average
    result['max'] = total_max
    return result


print(calc([1,3,5,7]))

#     return result
#







