incoming_data = input()
phonebook = {}
while True:
    if '-' not in incoming_data:
        flag = True
        break
    else:
        name, number = incoming_data.split('-')
        phonebook[name] = number
    incoming_data = input()
for names in range(int(incoming_data)):
    checked_name = input()
    if checked_name in phonebook.keys():
        print(f"{checked_name} -> {phonebook[checked_name]}")
    else:
        print(f"Contact {checked_name} does not exist.")

