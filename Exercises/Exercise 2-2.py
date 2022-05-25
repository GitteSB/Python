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

leave_at = (6*60)+52
easy_pace = 8.15
tempo = 7.12
miles_easy = 2
miles_tempo = 3

back = leave_at +((easy_pace*miles_easy)+(tempo*miles_tempo))
home_at = back/60

print(home_at)