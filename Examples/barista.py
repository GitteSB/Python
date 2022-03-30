print("Hello, welcome to Nerdi Coffee!!!")
# Lav en variable som er navnet
name =input ("What is your name?\n")

if name == "Ben":
    print("You're not Welcome here")
    exit()
else:
    #brug variablen name
    print( "Hello " + name + " Thank you so much for coming in today")
    
    
menu = "Black coffee, Espresso, Latte, Hot Chocolate"

print( name + " What would you like today? Here's our menu for the day\n" + menu)

order = input()

print("Sounds good " + name + " we'll have that " + order + " ready for you soon")

price = 8

number_coffee = input("How many would "+ order + " you like? \n")

total = price * int(number_coffee)
 
print (" That will be", total )


