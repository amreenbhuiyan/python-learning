#Shopping cart programm
#item price und quantity

item = input("Item:")
price = float(input("Price:"))
quantity = int(input("Quantity:"))

gesamt = price * quantity

print(f"Was für Item: {item}")
print(f"Wie viel Para: {price}€")
print(f"Wie viel quantity: {quantity}")
print(f"Totalpreis: {gesamt} €")

