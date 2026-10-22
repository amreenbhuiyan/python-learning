#collection = single variables used to store multiple values
# List = [] ordered and changeable. Duplicates Ok 
# Set = {} unordered and immutable, but Add/Remove Ok. No duplicates 
#Tuple = () ordered and unchangeable. Duplicates ok. Faster


#List
fruits = ["apple", "cherry", "fatihhan", "coconut"]
#print(dir(fruits))

#print(help(fruits))
#print(len(fruits))
#print("Jackfruit" in fruits) # boolean der dir sagt True / False falls es in der Liste vorhanden ist

#print(f"MEINS und nicht deins: {fruit}")
#print(fruit[::2])

#for fruit in fruits:
#   print(fruit)

#fruits[0] = "pineapple" 
#fruits.append("pineapple") #append + in der liste adden
#fruits.remove("Fatihhan")
#fruits.insert(0, "pineapple")
#fruits.sort()
#fruits.reverse()
#fruits.clear()
#print(fruits.index("apple"))
print(fruits.count("fatihhan"))

#print(fruits[0])
for fruit in fruits:
    print(fruit)
