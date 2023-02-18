number_of_input_lines = int(input())
total_sum = 0
if number_of_input_lines > 20:
    exit()
for _ in range(number_of_input_lines):
    current_str = input()
    total_sum += ord(current_str)
print(f"The sum equals: {total_sum}")

