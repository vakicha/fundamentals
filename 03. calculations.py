name_of_function = input()
number_1 = int(input())
number_2 = int(input())


def calculations(n1, n2):
    if name_of_function == "multiply":
        return number_1 * number_2
    if name_of_function == "divide":
        return number_1 // number_2
    if name_of_function == "add":
        return number_1 + number_2
    if name_of_function == "subtract":
        return number_1 - number_2


print(calculations(number_1, number_2))
