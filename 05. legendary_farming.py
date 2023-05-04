input_data = input().split()
container = {"shards": 0, "fragments": 0, "motes": 0}
obtained = False
while True:
    for index in range(0, len(input_data), 2):
        name = input_data[index + 1].lower()
        quantity = int(input_data[index])
        if name not in container:
            container[name] = 0
        container[name] += quantity
        if container["shards"] >= 250:
            print(f"Shadowmourne obtained!")
            container["shards"] -= 250
            obtained = True
        if container["fragments"] >= 250:
            print(f"Valanyr obtained!")
            container["fragments"] -= 250
            obtained = True
        if container["motes"] >= 250:
            print(f"Dragonwrath obtained!")
            container["motes"] -= 250
            obtained = True
        if obtained:
            break
    if obtained:
        break
    input_data = input().split()
for name_element, quant in container.items():
    print(f"{name_element}: {container[name_element]}")
