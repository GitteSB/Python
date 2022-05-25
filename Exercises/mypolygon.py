"""
import turtle
import math

firkant = turtle.Turtle()
print(firkant)

for i in range(4):
    firkant.fd(100)
    firkant.lt(90)

turtle.mainloop()
"""
"""
def polygon(t,n,length):
    angle = 360/n
    for i in range(n):
        t.fd(length)
        t.lt(angle)

polygon(firkant, 7, 70)
"""
import turtle
import math

bob= turtle.Turtle()
print(bob)

def circle(t,r):
    circumference = 2*math.pi * r
    n = 50
    length = circumference / n
    polygon(t, n, length)



turtle.mainloop()