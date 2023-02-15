number = int(input())
# for index in range(1, number + 1):
#     special_condition = False
#     str_index = str(index)
#     digit_sum = 0
#     for char in str_index:
#         digit_sum += int(char)
#     if digit_sum == 5 or digit_sum == 7 or digit_sum == 11:
#         special_condition = True
#     print(f"{index} -> {special_condition}")
for index in range(1, number + 1):
    is_special = False
    digits = index
    sum_digits = 0
    while digits > 0:
        sum_digits += digits % 10
        digits = digits // 10
    if sum_digits == 5 or sum_digits == 7 or sum_digits == 11:
        is_special = True
    print(f"{index} -> {is_special}")







