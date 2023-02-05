number_of_input_lines = int(input())
for _ in range(number_of_input_lines):
    input_number = int(input())
    if input_number == 88:
        print("Hello")
    elif input_number == 86:
        print("How are you?")
    elif input_number < 88:
        print("GREAT!")
    elif input_number > 88:
        print("Bye.")
