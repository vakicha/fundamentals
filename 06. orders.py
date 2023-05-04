incoming_data = input()
products_dict = {}
while incoming_data != "buy":
    name = incoming_data.split()[0]
    if name in products_dict:
        products_dict[name][0] = float(incoming_data.split()[1])
        products_dict[name][1] += int(incoming_data.split()[2])
    else:
        products_dict[name] = [float(incoming_data.split()[1]), int(incoming_data.split()[2])]
    incoming_data = input()
for name, price in products_dict.items():
    print(f"{name} -> {(price[0] * price[1]):.2f}")
