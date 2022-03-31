print("Hello, welcome to Nerdi Coffee!!!")
# Lav en variable som er navnet
name =input ("What is your name?\n")
<<<<<<< HEAD
 if name == "Ben":
     print("You're not welcome here!")
     exit()
else:
#brug variablen
    print( "Hello " + name + " Thank you so much for coming in today")

=======

if name == "Ben":
    print("You're not Welcome here")
    exit()
else:
    #brug variablen name
    print( "Hello " + name + " Thank you so much for coming in today")
    
    
>>>>>>> 3b7397027e2c462df299ca430cabfcfd2e4d52a2
menu = "Black coffee, Espresso, Latte, Hot Chocolate"

print( name + " What would you like today? Here's our menu for the day\n" + menu)

order = input()

print("Sounds good " + name + " we'll have that " + order + " ready for you soon")

price = 8

number_coffee = input("How many would "+ order + " you like? \n")
# lave en string til int
total = price * int(number_coffee)
<<<<<<< HEAD
# lave en int tilbage til en str
print ( "Thank you. Your total is:" + str(total) + "$" )
=======
 
print (" That will be", total)
>>>>>>> 3b7397027e2c462df299ca430cabfcfd2e4d52a2


