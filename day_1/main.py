def solution():
    input_file = open("input.txt", "r")
    input_list = input_file.read().split("\n")
    numbers_list = list(map(lambda x: int(x), input_list))
    numbers_set = set(numbers_list)
    target_sum = 2020

    for num in numbers_list:
        looking_for = target_sum - num
        if looking_for in numbers_set:
            return looking_for * num
