def factorial_division(first_number, second_number):
    first_factorial = first_number
    second_factorial = second_number
    for n in range(first_number - 1, 0, -1):
        first_factorial *= n
    for n in range(second_number - 1, 0, -1):
        second_factorial *= n
    dev = (first_factorial / second_factorial)
    return dev


number1 = int(input())
number2 = int(input())
print(f"{factorial_division(number1, number2):.2f}")
