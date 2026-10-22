username = input("Enter your name:")

if len(username) > 12:
    print("nicht größer als 12")
elif username.find(" ") != -1:
    print("kein Space")
elif not username.isalpha():
    print("keine zahlen")

else:
    print("valid part3")

if username == "Fatihhan":
    print("block")

else:
    print("ignore")
