import turtle
t = turtle.Turtle()
t.speed(20)

colors = ['red' , 'orange' , 'yellow' , 'green' , 'blue' , 'indigo' , 'violet']
turtle.bgcolor('black')
for i in range(700):
    t.color(colors[i % 7])
    t.circle(100)
    t.right(700)
turtle.done()