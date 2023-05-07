incoming_data = input()
force_book = {}

while incoming_data != "Lumpawaroo":
    if "|" in incoming_data:
        repeat = False
        side, force_user = incoming_data.split(' | ')
        for user in force_book.values():
            if force_user in user:
                repeat = True
                break
        if not repeat:
            if side not in force_book.keys():
                force_book[side] = [force_user]
            else:
                force_book[side].append(force_user)
    elif "->" in incoming_data:
        force_user, side = incoming_data.split(' -> ')
        for key, users in force_book.items():
            if force_user in users:
                force_book[key].remove(force_user)
        if side not in force_book.keys():
            force_book[side] = [force_user]
        else:
            force_book[side].append(force_user)
        print(f"{force_user} joins the {side} side!")
    incoming_data = input()
for force, members in force_book.items():
    if len(force_book[force]) > 0:
        print(f"Side: {force}, Members: {len(force_book[force])}")
        for member in force_book[force]:
            print(f"! {member}")
