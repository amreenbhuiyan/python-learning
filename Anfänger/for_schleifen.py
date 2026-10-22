#for loop = execute a block of code a fixed number of times.
#You can iterate over a range, string, sequence, etc.


#1 bis 10 zählen
#for x in range(1, 11):
#    print(x)

#Umgekhrt 10,9,....1   
#for x in reversed(range(1, 11)):
#    print(x)   

# 2er Schritten --> zählt 1,3, 5,7,9
#for x in range(1, 11, 2):
#    print(x)

#credit_card = "1234-5678-9012-3456"

#for x in credit_card:
#    print(x)

# count to 20 
for x in range(1 , 21):
    if x ==  13: 
        continue #skip 13... eine zahl auslassen damit
    # mit break werden wir aus schleife rausgeworfen 
    else:
        print(x)