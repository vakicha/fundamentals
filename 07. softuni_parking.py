number_of_actions = int(input())
parking = {}
for act in range(number_of_actions):
    incoming_data = input().split()
    command = incoming_data[0]
    user_name = incoming_data[1]
    if command == "register":
        license_plate = incoming_data[2]
        if user_name in parking:
            print(f'ERROR: already registered with plate number {license_plate}')
        else:
            print(f'{user_name} registered {license_plate} successfully')
            parking[user_name] = license_plate
    elif command == "unregister":
        if user_name not in parking:
            print(f"ERROR: user {user_name} not found")
        else:
            print(f"{user_name} unregistered successfully")
            del parking[user_name]
for user, reg_num in parking.items():
    print(f"{user} => {reg_num}")
