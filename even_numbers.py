number_of_lines = int(input())
for n in range(1, number_of_lines + 1):
    input_line = int(input())
    if input_line % 2 != 0:
        print(f"{input_line} is odd!")
        break
else:
    print("All numbers are even.")
