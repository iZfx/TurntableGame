import turtle
import random

# 创建窗口
window = turtle.Screen()
window.title('大转盘')
window.bgcolor("white")
window.setup(width=600, height=600)

# 创建转盘图形
pen = turtle.Turtle()
pen.shape("square")
pen.color("blue")
pen.penup()
pen.goto(0, -250)

colors = ["red", "orange", "yellow", "green", "blue", "purple"]
sectors_num = len(colors)
sector_angle = 360 / sectors_num
for i in range(sectors_num):
    pen.speed(0)
    pen.color(colors[i])
    pen.begin_fill()
    pen.circle(250, sector_angle)
    pen.left(sector_angle)
    pen.end_fill()


def rotate():
    angle = random.randint(0, 360)
    pen.setheading(angle)

    for _ in range(10):
        pen.speed(1)
        pen.circle(250, sector_angle)


window.listen()
window.onkeypress(rotate, "space")

while True:
    window.update()
    window.mainloop()

