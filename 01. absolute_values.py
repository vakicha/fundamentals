# incoming_nums = input().split()
# abs_float_nums = []
# for float_nums in incoming_nums:
#     abs_float_nums.append(abs(float(float_nums)))
# print(abs_float_nums)

input_line = list(map(float, input().split()))
result = [abs(num) for num in input_line]
print(result)
