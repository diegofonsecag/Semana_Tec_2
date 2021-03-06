"""Cannon, hitting targets with projectiles.

Modificaciones:

1. Diego: Aumentaremos la velocidad del proyectil y de los blancos.
2. Marisa: Cambiaremos el color del proyectil, los blancos y del fondo.
3. Santiago: Haremos que el juego nunca termine.

"""

from random import randrange
from turtle import *
from freegames import vector

ball = vector(-200, -200)
speed = vector(0, 0)
targets = []

def tap(x, y):
    "Respond to screen tap."
    if not inside(ball):
        ball.x = -199
        ball.y = -199
        speed.x = (x + 200) / 25
        speed.y = (y + 200) / 25

def inside(xy):
    "Return True if xy within screen."
    return -200 < xy.x < 200 and -200 < xy.y < 200

def draw():
    "Draw ball and targets."
    clear()
    # Aquí cambiamos el color del fondo a negro
    bgcolor('black')
    for target in targets:
        goto(target.x, target.y)
        # Aquí cambiamos el color de los blancos de azul a morado
        dot(20, 'purple')

    if inside(ball):
        goto(ball.x, ball.y)
        # Aquí cambiamos el color del proyectil de rojo a naranja
        dot(6, 'orange')

    update()


def move():
    "Move ball and targets."
    if randrange(15) == 0:
        y = randrange(-150, 150)
        target = vector(200, y)
        targets.append(target)

    for target in targets:
        # Aquí aumentamos la velocidad de los blancos de 0.5 a 2.5
        target.x -= 2.5

    if inside(ball):
        # Aquí reducimos el efecto de la gravedad de la pelota, aumentando su velocidad.
        speed.y -= 0.15
        ball.move(speed)

    dupe = targets.copy()
    targets.clear()

    for target in dupe:
        if abs(target - ball) > 13:
            targets.append(target)

    draw()

    # Aquí creamos que el mapa sea continuo, y así el juego infinito
    for target in targets:
        if not inside(target):
            targets.remove(target)
            #return

    ontimer(move, 50)

setup(420, 420, 370, 0)
hideturtle()
up()
tracer(False)
onscreenclick(tap)
move()
done()
