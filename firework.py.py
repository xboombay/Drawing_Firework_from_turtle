import turtle
tao = turtle.Pen()

def small():
    tao.pencolor("blue")
    for i in range(60):
        tao.forward(60)
        tao.left(133)

def big():
    tao.pencolor("purple")
    for i in range(100):
        tao.penup()
        tao.goto(200,210)
        tao.pendown()
        tao.forward(100)
        tao.left(133)

small()
big()
