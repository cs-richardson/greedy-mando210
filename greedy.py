"""
"""
# Miki Ando

change = float(input("How much change is owed? "))
coin = 0

change = change * 100

remainder = change % 25
coin = (change - remainder) / 25
change = remainder

remainder = change % 10
coin = coin + (change - remainder) / 10
change = remainder

remainder = change % 5
coin = coin + (change - remainder) / 5
change = remainder

remainder = change % 1
coin = coin + (change - remainder) / 1

coin = str(int(coin))
print ("You have " + coin + " coins")
