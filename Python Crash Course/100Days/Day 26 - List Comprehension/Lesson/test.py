
result = set()

with open("numbers1.txt") as file1:
    int_f1 = [int(x.strip()) for x in file1.readlines()]

with open("numbers2.txt") as file2:
    int_f2 = [int(x.strip()) for x in file2.readlines()]

    for num in int_f1:
        for nums in int_f2:
            if num == nums:
                result.add(num)

print(list(result))