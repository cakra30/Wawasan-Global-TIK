import turtle as tur
tur.bgcolor('black')
tur.speed(9999999999999999999999999999999999999999999999999999999999999)
tur.hideturtle()

colors = ["blue", "purple", "blue", "purple"]

for i in range (120):
    for c in colors:
        tur.color(c)
        tur.circle(200-i,100)
        tur.lt(90)
        tur.circle(200-i,100)
        tur.end_fill()

tur.mainloop()