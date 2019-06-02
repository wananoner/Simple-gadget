import turtle

def drawSnake(rad, angle, len, neckrad):
    for i in range(len):
        turtle.circle(rad, angle)
        turtle.circle(-rad, angle)
    turtle.circle(rad, angle/2)
    turtle.fd(rad)
    turtle.circle(neckrad+1, 180)
    turtle.fd(rad*2/3)

def main():
    turtle.setup(1300, 800, 0, 0)
    pythonsize = 30
    turtle.pensize(pythonsize)
    turtle.pencolor("blue")
    turtle.seth(56)
    drawSnake(30, -50, 5, pythonsize/2)

main()

'''
turtle.seth(0)
turtle.fd(100)
turtle.seth(120)
turtle.fd(100)
turtle.seth(240)
turtle.fd(100)
'''
