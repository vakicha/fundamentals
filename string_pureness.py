number_of_input_strings = int(input())
flag = True
for _ in range(number_of_input_strings):
    flag = True
    input_string = input()
    for ch in range(len(input_string)):
        char = input_string[ch]
        if char == "," or char == "_" or char == ".":
            print(f"{input_string} is not pure!")
            flag = False
            break
    if flag:
        print(f"{input_string} is pure.")

