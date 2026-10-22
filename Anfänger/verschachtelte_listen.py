#array2
fruits =    ["apple", "orange", "banana", "coconut"]
vagetable = ["celery" , "carrots" , "potatoes"]
meats =     ["chicken", "fish", "turkey"]

groceries = [fruits, vagetable, meats]

#fruits[0] = "pineapple"
#print(groceries[2][1]) #2 pfeilunten zu meats 1 -> fish
#print(groceries[2][1]) 

for x in groceries:
    for food in x:
        print(food, end=" ") #gibt genau in blöcken mit abstand 
    print()