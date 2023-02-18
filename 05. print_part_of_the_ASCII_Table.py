start_number = int(input())
finish_number = int(input())

for character in range(start_number, finish_number + 1):
    char = chr(character)
    print(char, end=" ")
