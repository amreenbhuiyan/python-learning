#name = input("Enter your full name:")
phone_number = input("Enter your full phone_number:")

#result = len(name)
#result = name.find(" ")  #Abstand kommt nach  6ten Buchstabe 

#result = name.rfind("e")  #letzte Position
#result = name.capitalize() # erste Buchstanbe wird Groß geschrieben
#result = name.upper() #alle Buchstaben werden groß geschrieben
#result = name.lower() #alle Buchstaben werden klein
#result = name.isdigit()
#result = name.isalpha() #schaut ob es ein Wort isst. wort true , Zahl False
#result = phone_number.count("-") # 1-234-567-891 ->3 mal "-"
result = phone_number.replace("-", " ") # alle - "" ersetzt

print(result)