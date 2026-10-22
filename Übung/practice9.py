telefon = [["1" , "2" , "3"],
           ["4", "5" ,"6"],
           ["7" ,"8" ,"9"],
           ["*", "0", "#"]]

#print(telefon)
for x in telefon:
    for zahlen in x:
        print(zahlen, end=" ")
    print()