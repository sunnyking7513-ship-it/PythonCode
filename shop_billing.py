```python
from datetime import datetime

print("=" * 45)
print("          SHOP BILLING SYSTEM")
print("=" * 45)

shop_name = "SUNNY GENERAL STORE"
items = []
total = 0

print(f"\nWelcome to {shop_name}!")
print("Enter product details below.")
print("Type 'done' when all products are added.\n")

while True:
    name = input("Product name: ").strip()

    if name.lower() == "done":
        break

    if not name:
        print("Product name cannot be empty!\n")
        continue

    try:
        price = float(input("Price per item (Rs.): "))
        quantity = int(input("Quantity: "))

        if price <= 0 or quantity <= 0:
            print("Price and quantity must be greater than zero!\n")
            continue

    except ValueError:
        print("Please enter a valid price and quantity!\n")
        continue

    amount = price * quantity

    items.append({
        "name": name,
        "price": price,
        "quantity": quantity,
        "amount": amount
    })

    total += amount
    print(f"Added: {name} - Rs. {amount:.2f}\n")

if items:
    print("\n" + "=" * 55)
    print(f"              {shop_name}")
    print("=" * 55)
    print("Date:", datetime.now().strftime("%d-%m-%Y %I:%M %p"))
    print("-" * 55)
    print(f"{'Product':<18}{'Price':>10}{'Qty':>8}{'Amount':>12}")
    print("-" * 55)

    for item in items:
        print(
            f"{item['name'][:18]:<18}"
            f"{item['price']:>10.2f}"
            f"{item['quantity']:>8}"
            f"{item['amount']:>12.2f}"
        )

    print("-" * 55)
    print(f"{'TOTAL AMOUNT':<36} Rs. {total:.2f}")
    print("=" * 55)

    print("\nThank you for shopping with us!")
else:
    print("\nNo products added. Bill was not generated.")