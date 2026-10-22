#format spefifiers = {value:flags} format a value absed in what flags are inserted 
# .(number)f = round to that many decimal places (fixed point)
# :(number) =allocate that spaces
# :03 allocate and zero pad that many spaces 
# :< = left justify 
# :> = right justify 
# :^ = center align
# :+ = use a plus sign to indicate positive value 
# := = place sign to leftmost position 
# :  = insert a space before positive numbers
# :, = comma seperator 

#price1 = 3.12345
#price2 = -987.65
#price3 = 12.34

price1 = 3000.12345
price2 = -9870.65
price3 = 1200.34
#{value:flags}
print(f"Preis 1 is {price1:.2f}") #sondern 3.12 gibt er aus .2f
print(f"Preis 2 is {price2:.1f}") #gibt -987.6 aus .1f
#print(f"Preis 3 is {price3:.3f}.") #gibt 12.340 aus .3f
#print(f"Preis 3 is {price3:10}")
#print(f"Preis 3 is {price3:010}") #0000012.34
#print(f"Preis 3 is {price3:<10}") 
#print(f"Preis 3 is {price3:>10}") 
#print(f"Preis 3 is {price3:^10}") # Preis 3 is   12.34 
#print(f"Preis 3 is {price3:+}") #steht vor der Zahl +
print(f"Preis 3 is {price3:+,.2f}") 