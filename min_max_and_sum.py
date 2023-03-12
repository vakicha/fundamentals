input_line = [int(num) for num in input().split()]


def max_min_sum(list_int):
    max_int = max(input_line)
    min_int = min(input_line)
    sum_int = sum(input_line)
    print(f'The minimum number is {min_int}')
    print(f"The maximum number is {max_int}")
    print(f"The sum number is: {sum_int}")


max_min_sum(input_line)
