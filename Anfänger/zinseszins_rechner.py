principle = 0
rate = 0
time = 0

#while principle <= 0:
while True:
    principle = float(input("Anzahl von Direktoren:"))
    if principle <= 0:
        print("Direktor kann nicht weniger oder gleich als 0 sein.")
#new
    else:   
        break 
    
#while rate <= 0:
while True:
    rate = float(input("Interest rate:"))
    if rate <= 0:
        print("Interest Rate kann nicht weniger oder gleich als 0 sein.")
#new    
    else: 
        break
    
#while time <= 0:
while True:
    time = int(input("Enter the time in years :"))
    if time <= 0:
        print("Time kann nicht weniger oder gleich als 0 sein.")
#new
    else:
        break       

total = principle * pow((1 + rate / 100), time) 

print(principle)
print(rate)
print(time)
print(total)