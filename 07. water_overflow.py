number_of_incoming_liters = int(input())
capacity = 255
water_count = 0
for water_flow in range(number_of_incoming_liters):
    current_incoming = int(input())
    if current_incoming > capacity:
        print("Insufficient capacity!")
        continue
    water_count += current_incoming
    capacity -= current_incoming
print(water_count)
