number_of_wagons = int(input())
list_of_wagons = [0 for wagons in range(number_of_wagons)]
input_command = input()
while input_command != "End":
    command = input_command.split()[0]
    if command == "add":
        number_of_ppl = int(input_command.split()[1])
        list_of_wagons[-1] += number_of_ppl
    elif command == "insert":
        wagon_index = int(input_command.split()[1])
        number_of_ppl = int(input_command.split()[2])
        list_of_wagons[wagon_index] += number_of_ppl
    elif command == "leave":
        wagon_index = int(input_command.split()[1])
        number_of_ppl = int(input_command.split()[2])
        list_of_wagons[wagon_index] -= number_of_ppl
    input_command = input()
print(list_of_wagons)
