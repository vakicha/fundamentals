budget = float(input())
price_of_flour = float(input())
price_of_liter_milk = price_of_flour * 1.25
price_of_eggs = price_of_flour * 0.75
price_for_one_bread = price_of_eggs + price_of_flour + price_of_liter_milk / 4
colored_eggs = 0
bread_count = 0
while price_for_one_bread < budget:
    budget -= price_for_one_bread
    bread_count += 1
    colored_eggs += 3
    if bread_count % 3 == 0:
        colored_eggs -= bread_count - 2
print(f"You made {bread_count} loaves of Easter bread! Now you have {colored_eggs} eggs and {budget:.2f}BGN left.")


