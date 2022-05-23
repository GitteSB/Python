# Exercise 1
from cmath import pi


print("The volume of a sphere with radius r us 4/3pi'r^2. What us the volume of a sphere with r = 5")

r = 5.0
p = pi
x = 4/3
volume = x*pi*(r**2)

print(volume)

print("Exercise 2")


book = 24.95
discount = 0.4
shipping1 = 3
shipping_rest = 0.75
copies = 60
rest_copies = 59


all_discount= (book*copies)*discount
print(all_discount)

wholesale = all_discount+(rest_copies*shipping_rest)+shipping1
print(wholesale)


print("Exercise 3")
print("Run at 2 paces")

