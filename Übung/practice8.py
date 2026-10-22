#shopping cart programm

foods = []
prices = []
total = 0

while True:
    food = input("Enter food (q to quit): ")
    if food.lower() == "q":
        break
    else:
        price = float(input("Enter price (q to quit): € "))
        foods.append(food)
        prices.append(price)

for food in foods:
    print(food)
    
for price in prices:
    total += price

print(total)