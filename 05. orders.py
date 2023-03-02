product = input()
quantity = float(input())


def menu(prod, quan):
    if product == "coffee":
        return quantity * 1.50
    if product == "coke":
        return quantity * 1.40
    if product == "water":
        return quantity * 1.00
    if product == "snacks":
        return quantity * 2.00


print(f"{menu(product, quantity):.2f}")
