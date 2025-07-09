# Every number in the decimal system can be expressed as
# a sum of its digits multiplied by powers of 10.

# abcd = a*10^3 + b*10^2 + c*10^1 + d*10^0

# We can separate the digits and rewrite this as:
# abcd = a + b + c + d + (a*999 + b*99 + c*9)
# abcd = a + b + c + d + (a*111 + b*11 + c*1)

# This implies that any number can be expressed as the sum of its digits plus a multiple of 9
# So, if we take modulo with 9 on each side,
# abcd % 9 = (a + b + c + d) % 9 + 0

# This means that the remainder when abcd is divided by 9 is equal to
# the remainder where the sum of its digits (a + b + c + d) is divided by 9

def single_dig_sum(int):
    # split_int = []
    # value = int
    # while value > 0:
    #     digit = value % 10
    #     value = value // 10
    #     split_int.append(digit)
    # sum_of_num = sum(split_int)

    return print(int % 9)







single_dig_sum(5674)



