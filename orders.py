number_of_orders = int(input())
total_price_of_all_orders = 0
for _ in range(number_of_orders):
    price_per_capsule = float(input())
    days = int(input())
    needed_capsules = int(input())
    if 0.01 > price_per_capsule or price_per_capsule > 100:
        continue
    elif 1 > days or days > 31:
        continue
    elif 1 > needed_capsules or needed_capsules > 2000:
        continue
    price = price_per_capsule * days * needed_capsules
    total_price_of_all_orders += price
    print(f"The price for the coffee is: ${price:.2f}")
print(f"Total: ${total_price_of_all_orders:.2f}")
