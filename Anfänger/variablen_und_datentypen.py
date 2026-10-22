#Variables -->string"",float, integer, boolean


#1) String
first_name = "Azra"
#print(first_name)
#f-string..type an f and then set a quote--> is a format 
print(f"Fatihhan + {first_name}")
food = "Sushi"
print(f"Azra likes {food}")

#2) Integer
age = 26
print(f"Azra ist {age} Jahre alt.")
num_of_children = 1
print(f"Azra has {num_of_children} child.")

#3) float
price = 10.99
gpa = 3.2
print(f"The price is {price}€.")
print(f"Your gpa is: {gpa}")

#4)boolean

is_animal = False
print(f"Is it a cat?: {is_animal}")

if is_animal:
    print("You are an animal.")
else:
    print("You are not an animal.")