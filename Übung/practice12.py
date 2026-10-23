menu = {"pizza": 8.99, "burger": 5.49, "salad": 4.99, "soda": 1.99}

cart = []
total = 0

for key, value in menu.items():
    print(f"{key}: ${value:.2f}")

while True:
    item = input("What would you like to order? (type 'q' to quit) ").lower()
    if item == "q":
        break
    elif item in menu:
        cart.append(item)
        total += menu[item]
        print(f"{item} added to cart. Total: ${total:.2f}")
    else:
        print("Sorry, we don't have that item.")

print(f"Final order: {cart}")
print(f"Total: ${total:.2f}")

