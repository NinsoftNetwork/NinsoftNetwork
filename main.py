import turtle
import random


# 屏保
t = turtle.Pen()
turtle.bgcolor('black')
colors = ['red', 'yellow', 'blue', 'green', 'orange', 'purple', 'white', 'gray']
for n in range(50):
    # 选择随机的颜色
    t.pencolor(random.choice(colors))
    # 随机
    size = random.randint(10, 100000000)
    # 随机坐标
    x = random.randint((-300), 300)
    y = random.randint((-300), 300)
    t.penup()
    t.goto(x, y)
    t.pendown()
    for m in range(size):
        t.forward((m * 2))
        # 可以试试可以更改角度看看哦
        t.left(91)
