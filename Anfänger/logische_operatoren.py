#logical operator= evaluate multiple condition(or, and, not)
#1)or = at least one condition must be True 
#2)and = both condition must be True 
#3)not = inverts the condition (not False not True)

#1)

#temp = 36
#is_raining = False

#if temp > 35 or temp < 0 or is_raining:
#    print("The outdoor event is cancelled")
#else:
#    print("The outdoor event is still scheduled")
#2) and
#temp = -5
#is_sunny = True
#if temp >= 28 and is_sunny:
#    print("It is HOT outside.")
#    print("It is Sunny")
#elif temp <= 0 and is_sunny:
#    print("It is cold outside.")
#    print("It is WINDY")

#3) not

temp = 20
is_sunny = True

if temp >= 28 and is_sunny:
    print("It is HOT outside.")
    print("It is Sunny")
elif temp <= 0 and not is_sunny:
    print("It is cold outside.")
    print("It is WINDY")
else:
    print("dont care")

    
