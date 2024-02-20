

from turtle import*
from colorsys import*
bgcolor("black")
tracer(5)
pensize(1.5)
def square(x):
    for i in range(30):
        forward(x)
        right(100)
    forward(x)

    for j in range(30):
        backward(x)
        right(60)
    backward(x)

n=30
for i in range (20):
    color(hls_to_rgb(20,1-i/n,1))
    for j in range(5):
        square(5+(i*7))        
        
hideturtle()
done()
