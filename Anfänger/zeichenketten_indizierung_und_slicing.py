#indexing= accesing elements of a sequence using[] (indexing operator)
# [start: end: step]

credit_number = "1234-5678-9012-3456"

#print(credit_number[1])  # aarys [0] wäre 1
#print(credit_number[0 : 4]) # die ersten 4 Zahlen
#print(credit_number[5: ]) # 1234 kommen nicht vor rest schon
#print(credit_number[-1]) #-1 ist von hinten also 6
#print(credit_number[: : 3]) # zählt jede sritte Zahl

#last_digits = credit_number[-4:]
#print(f"XXXX-XXXX-XXXX : {last_digits}")

credit_number = credit_number[::-1]
print(credit_number)


