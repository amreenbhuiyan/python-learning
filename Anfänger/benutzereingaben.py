#input = A function that prompts the user to enter data 
#Return the entered datat as a string

name = input("What is your name?: ")
age = int(input("How old are you?: ")) #Variante 2: int()neben input()

#age = int(age) # Variante 1

age = age + 1 

print(f"HELLO {name}!")
print(f"You are {age} years old.")