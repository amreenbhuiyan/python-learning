import time

#time.sleep(11)

#print("Fatihhan dead")

my_time = int(input("Enter the time:"))

#for x in reversed(range(0, my_time)): #option 1 rückwärts zählen
#for x in range(my_time, 0 , -1):     #option 2
#    print(x)
#    time.sleep(1)
    
#print("ding dong")

for x in range(my_time, 0, -1):
    sec = x % 60 #Rest 11 % 60 = 11
    min = int(x / 60) % 60
    hours = int(x / 3600)
    print(f"{hours:02}:{min:02}:{sec:02}")
    time.sleep(1)
    
print("RUN")