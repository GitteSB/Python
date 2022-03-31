print("Hello, welcome to Nerdi Coffee!!!")
# Lav en variable som er navnet
name =input ("What is your name?\n")

if name == "Ben":
    print("You're not welcome here!")
    exit()
else:
    print( "Hello " + name + " Thank you so much for coming in today")

menu = "Black coffee, Espresso, Latte, Hot Chocolate"

print( name + " What would you like today? Here's our menu for the day\n" + menu)

order = input()

print("Sounds good " + name + " we'll have that " + order + " ready for you soon")

price = 8

number_coffee = input("How many would "+ order + " you like? \n")
# lave en string til int
total = price * int(number_coffee)

# lave en int tilbage til en str
print ( "Thank you. Your total is:" + str(total) + "$" )

 




