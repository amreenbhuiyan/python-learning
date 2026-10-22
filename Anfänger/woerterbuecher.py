capital = {"Deutschland": "Berlin",
           "Italien": "Rom"}

#print(capital.get("Italien"))
#print(capital.get("Spanien"))

#if capital.get("Spanien"):
#    print("exits")
#else:
#    print("it doesn´t exits")
    
#capital.update({"Österreich": "Wien"})

#capital.pop("Italien")
#capital.popitem()
#capital.clear()

#key = capital.keys()

#for key in capital.keys():
#    print(key)

#value = capital.values()

#for value in capital.values():
#    print(value)
for key, value in capital.items():
    print(f"{key}:{value}")