input_integer = [int(digit) for digit in input()]


def odd_even(digits):
    odd = 0
    even = 0
    for num in digits:
        if num % 2 == 0:
            even += num
        else:
            odd += num
    print(f" Odd sum = {odd}, Even sum = {even}")


odd_even(input_integer)
