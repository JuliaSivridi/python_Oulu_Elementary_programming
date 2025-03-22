inventory = [("donkey", 12), ("Moomin mug", 1), ("poleax", 4)]

def select_quantity(product):
    return product[1]

print(select_quantity(inventory[0]))
for name, qty in inventory:
    print(f"Storage contains {qty} x {name}")

inventory.sort(key=select_quantity, reverse=True)
print(inventory)
