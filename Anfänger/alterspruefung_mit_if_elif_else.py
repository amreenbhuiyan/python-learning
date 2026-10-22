# if  = Do some code only IF some condition is True 
# Else do something else 

age = int(input("Enter your age:"))

if age >= 80:
    print(f"Its time to die.")
elif age >= 18: 
    print(f"You are too old.")
    print(f"Its time to die.")
else: 
    print(f"You are too young.")