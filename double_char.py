input_line = input()
while input_line != "End":
    if input_line == "SoftUni":
        input_line = input()
        continue
    final_word = ""
    for ch in range(len(input_line)):
        final_word += (input_line[ch]) * 2
    print(final_word)
    input_line = input()